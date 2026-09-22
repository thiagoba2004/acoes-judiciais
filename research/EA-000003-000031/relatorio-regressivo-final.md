# Relatório regressivo pós-correção — EA-000003-000031

**Projeto:** PRJ-000003 — Ações Judiciais  
**Data de corte:** 22/09/2026  
**Origem:** 10 achados A-01 a A-10 da EA-000003-000019.

## Resultado executivo

Os 10 achados da auditoria adversarial foram submetidos a três estratégias corretivas e a uma reauditoria independente:

- EA-000003-000028 — A-01, A-02 e A-08;
- EA-000003-000029 — A-03, A-04, A-07 e A-09;
- EA-000003-000030 — A-05, A-06 e A-10;
- EA-000003-000031 — reauditoria regressiva.

Na data de corte, os 10 achados estão **CORRIGIDOS E REVALIDADOS**.

## Fase 01 — Inventário
10/10 achados possuem estratégia corretiva, artefato de correção e trilha de auditoria.

## Fase 02 — Revalidação
Fontes normativas, jurisprudenciais e institucionais foram revalidadas. Não foi localizada superveniência que invalide as correções realizadas.

## Fase 03 — Paridade e consistência
- 24 HTMLs públicos.
- Todos os HTMLs narrativos possuem par Markdown.
- Exceção funcional: `fale-conosco/recebido.html`.
- Marcadores corretivos A-01 a A-10 presentes de forma coerente nos pares afetados.

### Regressão detectada
A reauditoria encontrou linguagem pública residual de “monitoramento” em seis páginas. A regressão foi corrigida sem alterar o conteúdo jurídico: estados de processo editorial foram substituídos por descrições substantivas para o leitor.

Rechecagem final: zero ocorrências públicas de linguagem de monitoramento ou códigos internos pesquisados.

## Fase 04 — Integridade
- 633 `href` auditados;
- 0 links internos quebrados;
- 0 âncoras locais quebradas;
- 0 âncoras cruzadas quebradas;
- SOURCE_REGISTRY.jsonl: 180 entradas, JSONL válido;
- 0 IDs duplicados;
- 0 URLs ausentes;
- cadeia temporal do Tema 215 preservada por `superseded_by` / `supersedes`;
- 0 automatismos jurídicos pesquisados reintroduzidos.

## Deploy
GitHub Pages run **35763781353**: **completed / success**.  
Commit publicado: `8fc14a7265c3c8a8571d506c4d7dd61693559a5b`.

## Conclusão

O ciclo corretivo específico da EA-000003-000019 está encerrado. Isso significa que **os 10 achados identificados naquele relatório foram tratados e reauditedos**; não equivale a afirmar que o corpus jurídico jamais terá novas superveniências, novos riscos ou novos achados em auditorias futuras.

O projeto retorna ao modo operacional, preservando atualização jurídica contínua e a regra de que novos achados materiais devem gerar manutenção rastreável ou nova Estratégia Autônoma conforme o escopo.
