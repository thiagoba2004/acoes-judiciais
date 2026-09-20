# Auditoria arquitetural — ausência do Menu Doutrina

**Data:** 20/09/2026

## Achado

A ausência de **Doutrina** no menu global não decorre de decisão documentada.

## Evidência interna

- O Plano de Fases da EA-000003-000001 possui a **FASE 06/08 — Jurisprudência, doutrina e controvérsias**.
- O gate dessa fase foi registrado como concluído com a criação de `research/EA-000003-000001/camada-doutrinaria-verificada.md`.
- O `SOURCE_REGISTRY.jsonl` contém fontes do tipo `doutrina_livro`, `doutrina_livro_coletivo`, `doutrina_capitulo` e `doutrina_artigo`.
- A EA-000003-000002, ao criar a arquitetura pública, registrou apenas as páginas centrais **Ações, Guias, Modelos, Jurisprudência, Legislação e Fontes**.
- `SITE_ARCHITECTURE.md` reproduz essa arquitetura sem Doutrina.
- Não foi localizada decisão que diga que Doutrina deveria ser absorvida por Fontes ou Jurisprudência.

## Diagnóstico

Trata-se de **lacuna arquitetural de transposição**: a camada de pesquisa jurídica possuía Doutrina como domínio próprio, mas essa dimensão não foi convertida em área pública quando a arquitetura do Site foi construída.

“Fontes” não é substituto conceitual perfeito: Fontes é uma camada transversal de proveniência; Doutrina é uma categoria material de conteúdo jurídico, assim como Legislação e Jurisprudência.

## Consequência

Qualquer decisão futura de criar ou não o Menu Doutrina deve ser expressa. O estado atual não deve ser interpretado como opção arquitetural deliberada.
