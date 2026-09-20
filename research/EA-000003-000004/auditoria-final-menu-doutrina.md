# Auditoria final — Menu Doutrina — Ações Judiciais

**Data:** 20/09/2026  
**Estratégia:** EA-000003-000004 — Menu Doutrina — correção arquitetural

## Decisão arquitetural

Doutrina passou a ser área pública própria.

A separação adotada é:

- **Legislação:** normas e atos;
- **Jurisprudência:** precedentes e teses;
- **Doutrina:** livros, capítulos e artigos com função interpretativa e sistematizadora;
- **Fontes:** camada transversal de proveniência e acesso.

## Implementação

Criados:
- `doutrina/index.md`;
- `doutrina/index.html`;
- `doutrina/index.json`.

Menu global final:

**Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Fale Conosco**

A página inicial de Doutrina publica quatro referências já verificadas para Superendividamento:
1. *Comentários à Lei 14.181/2021: a atualização do CDC em matéria de superendividamento*;
2. *Superendividamento dos consumidores: aspectos materiais e processuais*;
3. capítulo *Superendividamento do consumidor à luz da Lei 14.181, de 1º de julho de 2021*;
4. artigo da Revista CNJ sobre o papel do Poder Judiciário na aplicação da Lei do Superendividamento.

A página preserva os limites de uso: não atribui teses específicas a texto integral não consultado e não trata doutrina como precedente.

## Auditoria técnica

- páginas HTML públicas: **12**;
- links internos verificados: **159**;
- links com fragmento/âncora: **11**;
- destinos internos quebrados: **0**;
- fragmentos quebrados: **0**;
- páginas com Menu global divergente: **0**;
- marcadores de governança interna encontrados na UI: **0**;
- trio Markdown/HTML/JSON de Doutrina: **presente**;
- Mapa do Site contém Doutrina: **sim**;
- `aria-current="page"` em Doutrina: **correto**;
- cards doutrinários publicados: **4**;
- link da Doutrina para o dossiê de Superendividamento: **presente**;
- navegação mobile horizontal rolável: **preservada**.

## Deploy

O último commit que alterou a camada pública foi `232f154d943cd2e57fdf6bc5f7d022b1b600a41e` — “Adicionar Doutrina ao Mapa do Site”.

GitHub Pages:
- workflow: `35537406550`;
- resultado: **success**.

Os commits posteriores até o fechamento foram de governança interna e não alteraram a camada pública auditada.

## Estado final

`CONCLUIDA`
