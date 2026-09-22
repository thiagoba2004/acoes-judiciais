# EA-000003-000020 — Reorganização editorial e arquitetura de navegação do Site Ações Judiciais

**Status:** CONCLUÍDA  
**Dependência:** EA-000002-000008 — Padrão editorial de Atualidade, Análise e Observação para Sites.

## Objetivo
Integrar Notícias, Artigos e Observatório ao Site Ações Judiciais sem duplicar Ações, Guias, Modelos, Jurisprudência, Doutrina, Legislação ou Fontes.

## Plano de Fases
1. **Fase 01/06 [F-000003-000020-001] — Inventário e sobreposição semântica** — mapear conteúdos atuais e possíveis colisões.
2. **Fase 02/06 [F-000003-000020-002] — Arquitetura de informação e decisão de navegação** — testar três itens globais versus hub editorial com subáreas.
3. **Fase 03/06 [F-000003-000020-003] — Integração das estratégias filhas** — receber EA21, EA22 e EA23.
4. **Fase 04/06 [F-000003-000020-004] — Rotas, taxonomia e Mapa do Site** — definir URLs, metadados, cruzamentos e regras de classificação.
5. **Fase 05/06 [F-000003-000020-005] — Implementação pública e workflow** — atualizar Markdown/HTML, menu, rotas e GitHub Pages.
6. **Fase 06/06 [F-000003-000020-006] — Auditoria regressiva e fechamento** — validar desktop/mobile, links, conteúdo, acessibilidade e não redundância.

**Gate de não redundância:** cada conteúdo deve ter uma função editorial primária identificável; páginas temáticas continuam sendo a fonte estável do conhecimento jurídico, enquanto as novas camadas tratam atualização, análise autoral e observação cumulativa.
## Estado de execução — 22/09/2026

- Fase 01/06 — CONCLUÍDA — `inventario-sobreposicao-semantica.md`.
- Fase 02/06 — CONCLUÍDA — `decisao-arquitetura-editorial.md`.
- Fase 03/06 — CONCLUÍDA — estratégias filhas integradas.
- Fase 04/06 — CONCLUÍDA — rotas, taxonomia e Mapa do Site atualizados.
- Fase 05/06 — CONCLUÍDA — hub Publicações e workflow GitHub Pages implementados.
- Fase 06/06 — CONCLUÍDA — auditoria regressiva sem falhas e deploy verificado.

**Dependência do Gerador:** EA-000002-000008 CONCLUÍDA; Gerador 1.11 propagado ao AGENTS local.


## Fechamento — 22/09/2026

A estratégia foi concluída. O menu global passou a incluir **Publicações**, que concentra Notícias, Artigos e Observatório. O deploy final corresponde ao commit `6d161d0656f3053ea56d65b617d98c3a787f46e2` e ao workflow run `35728854051`, concluído com `success`.
