# AGENTS.md — AÇÕES JUDICIAIS

**project_code:** `PRJ-000003`  
**project_sequence:** `000003`  
**project_alias:** `AJ`  
**project_name:** `Ações Judiciais`  
**project_id legado:** `acoes-judiciais`  
**generated_from_kernel:** `1.4`  
**generator_release:** `1.8`  
**repository:** `thiagoba2004/acoes-judiciais`  
**modules:** `research`, `legal`, `publication`, `software`

## 1. Missão

Manter uma fonte pública, verificável e atualizável de consulta teórica e prática sobre possíveis ações judiciais para pessoas físicas e jurídicas. Cada ação judicial relevante deve ser tratada como Estratégia Autônoma própria, com fontes, plano, estado e entregas recuperáveis.

## 2. Entrada de qualquer pedido

Todo novo pedido deve seguir esta ordem:

```text
REGISTRAR EM REQUEST_LOG.jsonl
↓
CONFIRMAR TECNICAMENTE O REGISTRO
↓
INFORMAR “PEDIDO REGISTRADO.”
↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS
↓
EXECUTAR
```

## 3. Fonte da verdade

1. `AGENTS.md`;
2. `REQUEST_LOG.jsonl`;
3. `STRATEGY_LOG.jsonl`;
4. `PROJECT_STATE.json`;
5. `ROADMAP.md` e planos de fases;
6. `SOURCE_REGISTRY.jsonl` e fontes recuperáveis;
7. arquivos Markdown canônicos de conteúdo;
8. histórico Git comprovado;
9. somente depois, memória/conversa.

## 4. Estratégias e fases

Toda Estratégia Autônoma deve possuir `strategy_code` e `strategy_name` antes da execução substantiva.

Padrão:
```text
EA-000003-EEEEEE
F-000003-EEEEEE-FFF
```

Toda estratégia deve possuir Plano de Fases integralmente numerado, com `phase_number`, `phase_total`, `phase_code`, `phase_name`, estado, objetivo e gate.

## 5. Resposta de continuidade

Quando o usuário perguntar “Onde paramos?” ou equivalente, responder nesta ordem:

```text
PROJETO: PRJ-000003 — Ações Judiciais
ALIAS: AJ
ESTRATÉGIA AUTÔNOMA: <código> — <nome>
FASE: <número>/<total> [<código>] — <nome>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado>
```

## 6. Persistência e verificação

```text
PRODUZIR → SALVAR → VERIFICAR → ATUALIZAR ESTADO → CONTINUAR
```

Nunca afirmar commit, publicação, implantação, jurisprudência verificada ou atualização normativa sem confirmação técnica.

## 7. Módulo research

- distinguir fato encontrado, interpretação e hipótese;
- priorizar fontes primárias e institucionais;
- registrar data de consulta quando a informação puder mudar;
- preservar URL, identificador, documento ou metadados suficientes para recuperação;
- registrar divergências entre fontes;
- não reconstruir citações, números ou datas de memória quando a fonte puder ser recuperada.

## 8. Módulo legal

- distinguir fato comprovado, alegação, interpretação jurídica e conclusão;
- verificar legislação, jurisprudência, súmulas e doutrina crítica antes de usar;
- registrar jurisdição, órgão, processo, data e estado do precedente quando relevantes;
- explicitar competência, legitimidade, prazos, pressupostos, riscos e controvérsias;
- nunca presumir fatos ausentes;
- modelos de peças são pontos de partida e devem indicar variáveis que dependem do caso concreto.

### 8.1. Dossiê mínimo por ação judicial

Cada Estratégia Autônoma de ação judicial deve buscar, quando aplicável:

1. problema jurídico e objetivo;
2. hipóteses de cabimento e não cabimento;
3. legitimidade e competência;
4. fatos e documentos necessários;
5. fundamentos normativos;
6. jurisprudência relevante e divergências;
7. procedimento e marcos processuais;
8. pedidos e alternativas;
9. riscos, defesas previsíveis e ônus probatórios;
10. cálculos/simulações quando pertinentes;
11. checklist prático;
12. modelos reutilizáveis, quando aprovados;
13. data e escopo da última revisão.

## 9. Módulo publication

Para todo texto editorial/publicável:

```text
Markdown (.md) = fonte textual canônica
HTML (.html) = artefato de publicação
JSON (.json) = representação estruturada
```

Alterações materiais devem ser sincronizadas nos três artefatos. Exceções exigem decisão expressa, persistente e versionada.

Se forem publicados Modelos reutilizáveis:

- o botão **COPIAR MODELO** deve ficar imediatamente acima do texto exato a copiar;
- a função copia apenas o Modelo;
- somente a edição vigente fica acessível no Site Público;
- versões anteriores permanecem no Git ou em mecanismo não publicado;
- a verificação deve testar posição do botão, alvo da cópia e ausência de acesso público à edição superada.

## 10. Módulo software

- distinguir IMPLEMENTADO, TESTADO, VERSIONADO, IMPLANTADO e VERIFICADO EM EXECUÇÃO;
- testar alterações de comportamento quando tecnicamente possível;
- preservar compatibilidade, configuração e segurança;
- não confundir arquivo no repositório com site efetivamente publicado.

## 11. Interoperabilidade com outros projetos

O tema “superendividamento” também pode ser estudado no PRJ-000004 — Planejamento Financeiro. A referência cruzada é permitida, mas cada projeto mantém sua própria fonte da verdade, estratégia, análise e conclusão. Não copiar silenciosamente conteúdo entre projetos.

## 12. Fechamento

Antes de declarar uma etapa concluída, confirmar persistência, versão remota, estado, fontes críticas, coerência dos artefatos publicados e próximo passo lógico.

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
