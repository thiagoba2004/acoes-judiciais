# Auditoria de títulos visíveis — Site Público Ações Judiciais

**Data:** 21/09/2026  
**Escopo:** todas as páginas HTML públicas do repositório  
**Motivo:** identificar páginas cujo título existisse apenas no elemento técnico `<title>` do navegador, sem título editorial visível `<h1>`.

## Critério

Cada página pública deve possuir:

1. exatamente um `<title>` não vazio no `<head>`;
2. exatamente um `<h1>` editorial visível e não vazio no corpo;
3. nas páginas de dossiê/ação, o título deve aparecer antes do índice local, preferencialmente em bloco `hero`.

## Universo auditado

Foram auditados **14 arquivos HTML públicos**.

## Achados iniciais

Duas páginas possuíam `<title>` técnico, mas não possuíam `<h1>` visível:

- `acoes/repactuacao-superendividamento.html`;
- `acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.html`.

As fontes Markdown correspondentes já possuíam H1 canônico correto. A falha estava na transformação/publicação HTML.

## Correções

### Repactuação por superendividamento

Foi adicionado bloco `hero` antes do índice local, com:

- eyebrow: Direito do Consumidor;
- H1: Ação de Repactuação de Dívidas por Superendividamento;
- lede introdutório.

### Divórcio litigioso

Foi adicionado bloco `hero` antes do índice local, com:

- eyebrow: Direito de Família;
- H1: Ação de Divórcio Litigioso c/c Partilha de Bens, Guarda, Convivência e Alimentos;
- lede introdutório.

## Regra preventiva

Foram atualizados:

- `AGENTS.md`;
- `SITE_STYLE_GUIDE.md`.

Passa a ser obrigatório auditar separadamente `<title>` técnico e `<h1>` editorial visível. Páginas de dossiê/ação devem exibir o título antes do índice local.

## Reauditoria

Resultado após as correções:

- páginas auditadas: **14**;
- páginas com exatamente um `<title>` não vazio: **14/14**;
- páginas com exatamente um `<h1>` não vazio: **14/14**;
- páginas sem título visível: **0**;
- páginas com H1 duplicado: **0**;
- páginas com title técnico ausente: **0**.

## Deploy

- Superendividamento: workflow `35589228261` — **success**;
- Divórcio litigioso e estado público consolidado com ambas as correções: workflow `35589232271` — **success**;
- commit público consolidado: `9f9d458f1a719c75840b96ad57cc19b85406b28f`.

## Conclusão

**AUDITORIA APROVADA APÓS CORREÇÃO.**

A inconsistência mostrada na captura era real. Havia duas páginas sem título editorial visível, embora o título técnico do navegador estivesse presente. As duas foram corrigidas e o padrão passou a ser normativo no projeto.
