# Auditoria corretiva do Relatório do Advogado do Diabo

**Projeto:** PRJ-000003 — Ações Judiciais  
**Data:** 21/09/2026  
**Origem:** REQ-20260921-052  
**Escopo:** execução dos achados adversariais e reauditoria do corpus público.

## 1. Estratégias corretivas

- EA-000003-000008 — Fale Conosco, Privacidade e conformidade informacional;
- EA-000003-000009 — Revisão adversarial do Superendividamento e da interface com indenização trabalhista;
- EA-000003-000010 — Revisão adversarial de Divórcio, Partilha, Guarda, Convivência e Alimentos;
- EA-000003-000011 — Revisão adversarial da Reclamação Trabalhista com Danos Morais;
- EA-000003-000012 — Matriz canônica de jurisprudência, paridade Markdown–HTML e auditoria adversarial;
- EA-000003-000013 — Integridade editorial, proveniência pública e navegação.

## 2. Achados e providências

| Achado adversarial | Providência |
|---|---|
| AJ-ADV-001 — exclusões do superendividamento comprimidas | separação expressa entre art. 54-A, § 3º, e art. 104-A, § 1º, no dossiê e modelo |
| AJ-ADV-002 — Tema 1.236 simplificado | exigência bilateral (“vontade das partes”) e escritura pública explicitadas; ausência de opção válida também indicada |
| AJ-ADV-003 — Fale Conosco com estados contraditórios | Markdown e HTML atualizados para E2E operacional/verificado |
| AJ-ADV-004 — transparência LGPD insuficiente | criado Aviso de Privacidade; integração ao formulário, recibo, Mapa e workflow Pages |
| AJ-ADV-005 — IRR 84 sem estado recursal | “RE Pendente” incorporado ao dossiê, Jurisprudência e matriz canônica |
| AJ-ADV-006 — culpa concorrente misturada às excludentes | separação conceitual e referência ao art. 945 do Código Civil |
| AJ-ADV-007 — Tema 932 excessivamente amplo | recorte de acidente de trabalho e atividade de risco explicitado |
| AJ-ADV-008 — índice de Jurisprudência incompleto | página sincronizada; Tema 215 atualizado e demais temas monitorados incorporados |
| AJ-ADV-009 — “horas extras podem integrar” | condição e consequência jurisprudencial formuladas de modo preciso; PLR separada |
| AJ-ADV-010 — pesquisa negativa não reproduzível | nota de pesquisa com bases, descritores, data de corte e limites criada |
| AJ-ADV-011 — quitação seletiva como possível recomendação | cenários rotulados como analíticos, não recomendações automáticas |
| AJ-ADV-012 — links bibliográficos inadequados | substituídos por fonte editorial/BDJur e metadados atualizados |
| AJ-ADV-013 — Legislação mistura soft law | atos institucionais e soft law separados da legislação |
| AJ-ADV-014 — divergência Markdown/HTML | protocolo de paridade semântica incorporado ao AGENTS e arquitetura; pares críticos sincronizados |
| AJ-ADV-015 — proveniência pública insuficiente | padrão público de rastreabilidade publicado em Fontes |
| AJ-ADV-016 — “uso profissional” na Home | substituído por “estudo, pesquisa e apoio à atuação profissional” |
| AJ-ADV-017 — Mapa com só dois modelos | quatro modelos listados e Privacy incluída |
| AJ-ADV-018 — status longe do precedente | status/data aproximados dos precedentes críticos inseridos e matriz canônica criada |
| AJ-ADV-019 — gravação: licitude confundível com autenticidade | autenticidade, integridade, completude, contexto e preservação adicionados |
| AJ-ADV-020 — modelos copiáveis | todos os quatro blocos marcados como “estrutura-base, não uma petição pronta” |

## 3. Superveniência encontrada durante a própria correção

A auditoria corretiva identificou que o Tema 215 do TST já havia sido julgado em 19/08/2026. A redação anterior, que o tratava como tema apenas afetado/pendente, foi retirada. O dossiê e a página Jurisprudência passaram a refletir a tese atual, com caráter excepcional do foro do domicílio.

## 4. Mudanças estruturais preventivas

- criado `JURISPRUDENCE_MATRIX.md` como fonte canônica de recorte e status de precedentes;
- `AGENTS.md` agora exige auditoria adversarial de fonte, recorte, condições, exceções, alcance, estado processual, data e superveniência;
- pesquisa negativa deve ser datada e reproduzível;
- Markdown e HTML devem manter paridade semântica;
- `SITE_ARCHITECTURE.md` formaliza a separação entre legislação e soft law;
- workflow Pages passou a publicar `privacidade/`.

## 5. Reauditoria técnica

Reauditoria do estado final do repositório:

- HTMLs públicos: **16**;
- páginas com quantidade incorreta de `<title>`: **0**;
- páginas com quantidade incorreta de `<h1>`: **0**;
- links internos para arquivo inexistente: **0**;
- âncoras internas quebradas detectadas: **0**;
- expressão antiga “backend permanece indisponível”: **0**;
- expressão antiga de formulário “em configuração técnica”: **0**;
- formulação unilateral antiga do Tema 1.236: **0**;
- Tema 215 descrito pela situação antiga: **0**;
- mistura antiga “contratação dolosa / luxo” em uma única linha: **0**;
- páginas com modelo: **4/4** com um botão COPIAR MODELO, botão antes do bloco e aviso “estrutura-base, não uma petição pronta”;
- modelos listados no Mapa do Site: **4/4**;
- rota pública de Privacidade: presente e incluída no workflow.

## 6. Conclusão

**AUDITORIA CORRETIVA APROVADA NO REPOSITÓRIO.**

Os achados do Relatório do Advogado do Diabo foram convertidos em seis Estratégias Autônomas, tratados materialmente e convertidos em regras preventivas. O corpus corrigido não apresenta, nos testes finais, as inconsistências objetivas que motivaram o ciclo.

A verificação de publicação GitHub Pages deve ser registrada separadamente pelo estado do workflow após o último commit público.
