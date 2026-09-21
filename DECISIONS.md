# DECISIONS — PRJ-000003 — Ações Judiciais

## DEC-000001 — 20/09/2026 — Uma ação judicial por Estratégia Autônoma
Cada ação judicial relevante deve possuir estratégia própria, permitindo pesquisa, estado, fases e atualização independentes.

## DEC-000002 — 20/09/2026 — Dossiê teórico-prático padronizado
Cada estratégia buscará um dossiê mínimo com cabimento, competência, fatos/documentos, fontes, procedimento, jurisprudência, riscos e ferramentas práticas.

## DEC-000003 — 20/09/2026 — Publicação tripla — SUPERADA
Decisão histórica que previa Markdown, HTML e JSON para conteúdo editorial. **Superada** pela política posterior de JSON condicional.

## DEC-000005 — 21/09/2026 — Markdown + HTML; JSON somente quando necessário
Todo texto editorial/publicável usa Markdown como fonte textual canônica e HTML como publicação. JSON/JSONL só é criado quando houver finalidade estruturada real e consumidor de máquina identificado; não é espelho automático do conteúdo editorial.

## DEC-000004 — 20/09/2026 — Autonomia temática entre projetos
O superendividamento pode ser estudado também no PRJ-000004, mas Ações Judiciais conserva fonte da verdade e conclusões próprias.


## DEC-20260920-CONTACT-STACK — Stack canônica do Fale Conosco

**Decisão:** a expressão “seguir o mesmo padrão do Fale Conosco do Classe e Massas” inclui a stack técnica **Forminit + EmailJS**.

A implementação FormSubmit criada anteriormente é classificada como divergência técnica. Ela não deve ser tratada como solução final nem receber estado E2E_VERIFICADO.

**Migração obrigatória:** configurar Forminit isolado para `acoesjudiciais2026@gmail.com`, configurar EmailJS para confirmação ao remetente e testar o fluxo completo antes do fechamento.
