#!/usr/bin/env python3
"""APSP runtime adapter.

Generic, dependency-free state machine for project-local strategies.
It does not invent or execute unspecified work. It selects only actions
explicitly authorized by the local plan and persists every transition.
"""

from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
STATE_PATH = ROOT / "APSP_RUNTIME_STATE.json"
PLAN_PATH = ROOT / "APSP_RUNTIME_PLAN.json"

TERMINAL = {"COMPLETED", "BLOCKED", "WAITING_HUMAN_DECISION", "FAILED"}
RECOVERABLE = {"RUNTIME_INTERRUPTED"}

def now():
    return datetime.now(timezone.utc).isoformat()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def save(path, data):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)

def recover_state():
    state = load(STATE_PATH)
    state.setdefault("runtime_status", "IN_PROGRESS")
    state.setdefault("checkpoint", None)
    state.setdefault("next_executable_action", None)
    if state["runtime_status"] in RECOVERABLE:
        previous = state["runtime_status"]
        state["runtime_status"] = "IN_PROGRESS"
        state["checkpoint"] = {
            "at": now(),
            "reason": "runtime_recovered",
            "recovered_from": previous,
        }
        save(STATE_PATH, state)
    return state

def select_next_action():
    state = recover_state()

    if state["runtime_status"] in TERMINAL:
        return {"status": state["runtime_status"], "action": None}

    if not PLAN_PATH.exists():
        state["runtime_status"] = "BLOCKED"
        state["next_executable_action"] = None
        state["checkpoint"] = {
            "at": now(),
            "reason": "no_active_strategy_plan",
        }
        save(STATE_PATH, state)
        return {"status": "BLOCKED", "action": None}

    plan = load(PLAN_PATH)
    completed = set(state.get("completed_phases", []))
    completed_actions = set(state.get("completed_actions", []))
    for phase in plan.get("phases", []):
        if phase.get("phase_code") in completed:
            continue
        for action in phase.get("actions", []):
            if action.get("action_code") in completed_actions:
                continue
            if action.get("status") != "COMPLETED" and action.get("authorized", False):
                if action.get("requires_human_decision", False):
                    state["runtime_status"] = "WAITING_HUMAN_DECISION"
                    state["next_executable_action"] = None
                    state["checkpoint"] = {"at": now(), "reason": "human_decision_required"}
                    save(STATE_PATH, state)
                    return {"status": state["runtime_status"], "action": action}
                state["current_phase"] = phase["phase_code"]
                state["next_executable_action"] = action["action_code"]
                state["checkpoint"] = {"at": now(), "selected": action["action_code"]}
                save(STATE_PATH, state)
                return {"status": "IN_PROGRESS", "action": action}

    state["runtime_status"] = "COMPLETED"
    state["next_executable_action"] = None
    state["checkpoint"] = {"at": now(), "reason": "all_authorized_actions_completed"}
    save(STATE_PATH, state)
    return {"status": "COMPLETED", "action": None}

def verify_and_advance(action_code, success, evidence):
    state = recover_state()
    if not success:
        state["runtime_status"] = "FAILED"
        state["checkpoint"] = {"at": now(), "action": action_code, "evidence": evidence}
        save(STATE_PATH, state)
        return state

    if not PLAN_PATH.exists():
        state["runtime_status"] = "BLOCKED"
        state["checkpoint"] = {
            "at": now(),
            "action": action_code,
            "reason": "no_active_strategy_plan",
        }
        save(STATE_PATH, state)
        return state

    plan = load(PLAN_PATH)
    target = None
    target_phase = None
    for phase in plan.get("phases", []):
        for action in phase.get("actions", []):
            if action.get("action_code") == action_code:
                target = action
                target_phase = phase
                break
        if target is not None:
            break

    if target is None:
        state["runtime_status"] = "FAILED"
        state["checkpoint"] = {
            "at": now(),
            "action": action_code,
            "reason": "action_not_found_in_plan",
        }
        save(STATE_PATH, state)
        return state

    required = set(target.get("evidence_required", []))
    available = set(evidence) if isinstance(evidence, dict) else set()
    missing = sorted(required - available)
    if missing:
        state["runtime_status"] = "BLOCKED"
        state["checkpoint"] = {
            "at": now(),
            "action": action_code,
            "reason": "required_evidence_missing",
            "missing": missing,
        }
        save(STATE_PATH, state)
        return state

    state.setdefault("completed_actions", [])
    if action_code not in state["completed_actions"]:
        state["completed_actions"].append(action_code)

    if target_phase is not None:
        completed_actions = set(state["completed_actions"])
        phase_actions = [
            a.get("action_code")
            for a in target_phase.get("actions", [])
            if a.get("authorized", False) and a.get("action_code")
        ]
        if phase_actions and all(code in completed_actions for code in phase_actions):
            state.setdefault("completed_phases", [])
            phase_code = target_phase.get("phase_code")
            if phase_code and phase_code not in state["completed_phases"]:
                state["completed_phases"].append(phase_code)

    state["last_verified_action"] = action_code
    state["last_evidence"] = evidence
    state["next_executable_action"] = None
    state["checkpoint"] = {"at": now(), "action": action_code, "evidence": evidence}
    state["runtime_status"] = "IN_PROGRESS"
    save(STATE_PATH, state)
    return state

if __name__ == "__main__":
    result = select_next_action()
    print(json.dumps(result, ensure_ascii=False, indent=2))
