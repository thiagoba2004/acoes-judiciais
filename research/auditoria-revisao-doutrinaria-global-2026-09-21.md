# Auditoria global — revisão doutrinária transversal

**Projeto:** PRJ-000003 — Ações Judiciais
**Data:** 21/09/2026
**Pedidos:** REQ-20260921-049 e REQ-20260921-050
**Estado:** APROVADA

## 1. Escopo

Aplicar o `RESEARCH_DOUTRINA_PROTOCOL.md` aos textos materiais já publicados e auditar o corpus editorial/canônico do Projeto, incluindo a coerência dos documentos de governança diretamente relacionados à publicação e à metodologia.

## 2. Universo auditado

- 15 arquivos HTML públicos;
- 14 arquivos Markdown editoriais correspondentes;
- 1 HTML público de confirmação (`fale-conosco/recebido.html`) sem Markdown editorial próprio, por natureza operacional;
- 8 documentos Markdown de governança/canônicos não pertencentes a `research/`;
- `SOURCE_REGISTRY.jsonl`, com 142 registros;
- total de 22 Markdown não pertencentes a `research/` verificados.

## 3. Aplicação material do novo protocolo

O protocolo não ficou apenas no AGENTS ou na página Doutrina. Foi aplicado diretamente a:

- `acoes/repactuacao-superendividamento.md/.html`;
- `acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.md/.html`;
- `acoes/reclamacao-trabalhista-danos-morais.md/.html`;
- `guias/indenizacao-trabalhista-superendividamento.md/.html`.

Também foram atualizadas as camadas transversais:

- `doutrina/index.md/.html`;
- `fontes/index.md/.html`;
- `mapa-do-site/index.md/.html`;
- `acoes/index.md/.html`;
- índices de Guias, Modelos, Jurisprudência e Legislação tiveram revisão editorial/datacional;
- `SITE_ARCHITECTURE.md` foi alinhado ao protocolo ampliado;
- `DECISIONS.md` passou a marcar a antiga publicação tripla como SUPERADA e a adotar Markdown + HTML, com JSON/JSONL somente quando houver finalidade estruturada real.

## 4. Novas camadas efetivamente incorporadas

### Produção acadêmica

- UFRGS — Observatório do Crédito, Superendividamento e Conciliação de Conflitos de Consumo;
- Faculdade de Direito da USP — produção autoral sobre fragmentação familiar, alimentos e dano moral trabalhista;
- CAPES — usada apenas como critério externo verificável de excelência acadêmica, sem ranking próprio do Site.

### OAB e Comissões

- Comissão de Defesa do Consumidor do Conselho Federal;
- Comissão Nacional de Defesa do Consumidor;
- Comissão de Direito de Família da OAB-SP;
- Comissão Especial de Direito de Família do Conselho Federal;
- Comissão da Mulher Advogada / produção preventiva sobre assédio;
- OAB-MT com distinção expressa entre artigo individual e posição institucional.

### Doutrina profissional especializada

- Machado Meyer — Superendividamento/mínimo existencial e Direito do Trabalho/assédio;
- Chieco Advogados / Chambers Family Law 2026 — Direito de Família;
- reconhecimento externo de especialidade usado somente como critério de seleção da fonte, nunca como autoridade jurídica ou recomendação comercial.

### Contraditório

Os dossiês passaram a registrar divergência, superveniência e controle por legislação/jurisprudência. Exemplos:

- mínimo existencial: parâmetro quantitativo versus avaliação material individualizada;
- separação judicial: tese histórica confrontada com o Tema 1053 do STF;
- dano moral trabalhista: críticas à tarifação, produção acadêmica e perspectiva empresarial confrontadas com as ADIs 6.050, 6.069 e 6.082.

## 5. SOURCE_REGISTRY.jsonl

Resultado:

- registros: 142;
- JSON inválido: 0;
- IDs duplicados: 0;
- IDs malformados: 0;
- lacunas numéricas entre `AJ-SRC-000001` e `AJ-SRC-000142`: 0;
- registros sem `source_id`, `type`, `issuer`, `title` ou `status`: 0;
- novas fontes adicionadas nesta revisão: 17 (`AJ-SRC-000126` a `AJ-SRC-000142`);
- novos tipos metodológicos: `producao_academica`, `posicao_institucional_oab`, `producao_comissao_oab`, `autoria_individual_ambiente_oab`, `doutrina_profissional_especializada`, `criterio_excelencia_academica` e `reconhecimento_externo_escritorio`.

Foram identificadas 10 URLs reutilizadas em mais de um registro. A inspeção demonstrou que correspondem à mesma fonte oficial utilizada para objetos jurídicos, trechos ou estratégias distintos. Não há duplicidade de `source_id`; por isso, o reuso não foi tratado como erro de integridade.

## 6. Auditoria dos 15 HTMLs públicos

Resultado consolidado:

- `<title>` ausente ou duplicado: 0;
- `<h1>` ausente ou duplicado: 0;
- menu global diferente de 9 itens: 0;
- IDs HTML duplicados: 0;
- links internos apontando para arquivo inexistente: 0;
- vazamentos de governança (`PRJ-`, `EA-`, `REQ-`, `EVT-`, logs, AGENTS etc.): 0;
- rótulos redundantes `ACESSAR →` / `ACESSAR ->`: 0;
- linguagem promocional “melhores escritórios” / “melhores faculdades”: 0.

## 7. Âncoras e modelos

As âncoras essenciais das quatro unidades materiais revisadas foram verificadas.

Botões `COPIAR MODELO`:

- Superendividamento → `modelo-peticao`: íntegro;
- Divórcio → `modelo-divorcio`: íntegro;
- Reclamação trabalhista → `modelo-trabalhista-dano-moral`: íntegro;
- Guia indenização × superendividamento → `modelo-fato-superveniente`: íntegro.

Botões sem bloco `<pre>` correspondente: 0.

## 8. Auditoria dos Markdown

### 14 Markdown editoriais públicos

- H1 ausente/duplicado: 0;
- links internos para HTML inexistente: 0;
- dossiês materiais com protocolo doutrinário aplicado: 3/3;
- guia material interáreas com protocolo aplicado: 1/1;
- índices revisados em 21/09/2026 quando houve alteração material.

### 8 documentos canônicos/de governança

- H1 ausente/duplicado: 0;
- `AGENTS.md` referencia o protocolo e mantém JSON condicional;
- `SITE_ARCHITECTURE.md` agora reconhece produção acadêmica, OAB, doutrina profissional e posições interessadas;
- `DECISIONS.md` registra expressamente a superação da antiga regra de publicação tripla;
- datas de 20/09 mantidas em logs/decisões históricas não são tratadas como desatualização editorial.

## 9. Deploy

- workflow: `Deploy public site to GitHub Pages`;
- último run público: `35607094313`;
- conclusão: `success`;
- commit público: `7cc5b8b9c9071c1f85d3a8c2d66ddb414eb127b6`.

Runs intermediários cancelados ocorreram por concorrência serial do Pages durante a sequência de commits e não representam falha do artefato final.

## 10. Conclusão

**AUDITORIA APROVADA.**

O corpus público e canônico do Projeto Ações Judiciais está coerente com o novo Protocolo Doutrinário no escopo auditado. As três ações publicadas e o guia interáreas receberam aplicação material do método; as áreas Doutrina, Fontes e Mapa do Site foram ampliadas; o catálogo de fontes está íntegro; e o último artefato público foi implantado com sucesso.

## 11. Regra para próximas estratégias

Toda nova Estratégia Autônoma deve aplicar `RESEARCH_DOUTRINA_PROTOCOL.md` desde a fase de pesquisa, e não somente na auditoria final. A ausência de fonte materialmente aplicável em uma categoria deve ser registrada como resultado de busca/monitoramento, sem inventar posição institucional.