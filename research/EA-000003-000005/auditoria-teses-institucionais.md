# Auditoria — Teses institucionais de entidades jurídicas não governamentais

**Data:** 20/09/2026  
**Pedido:** incorporar posições institucionais de entidades jurídicas não governamentais ao Site Ações Judiciais.

## 1. Estado anterior

Antes desta revisão:
- não havia menção ao IBDFAM no Site;
- a área Doutrina reunia apenas obras, capítulos e artigos;
- o SOURCE_REGISTRY não continha teses institucionais do IBDFAM;
- os dossiês não possuíam seção obrigatória de teses institucionais.

## 2. Regra criada

Toda Estratégia Autônoma deve identificar, quando materialmente relevante:
- institutos jurídicos;
- associações científicas;
- academias;
- centros de estudo;
- entidades equivalentes.

As posições devem ser:
- atribuídas à instituição;
- recuperáveis em fonte oficial;
- tratadas como não vinculantes, salvo natureza diversa comprovada;
- confrontadas com legislação e jurisprudência;
- classificadas quanto à relação com o Direito atual.

## 3. Arquitetura pública

A camada foi integrada sem criar novo item no menu global:
- **Doutrina:** apresenta e compara a tese institucional;
- **Fontes:** oferece acesso à fonte oficial;
- **Dossiê da ação:** seção "Teses institucionais relevantes".

## 4. Primeiro caso aplicado — IBDFAM

Foram incorporados ao dossiê de divórcio os Enunciados 01, 02, 14, 18, 46, 47, 58 e 60.

Destaque metodológico:
- Enunciado 14 do IBDFAM: posição institucional sobre PLR na base alimentar;
- STJ em 2026: PLR não entra automaticamente e exige necessidade específica;
- o Site expõe a divergência em vez de escolher silenciosamente uma das fontes.

## 5. Artefatos atualizados

- AGENTS.md;
- SITE_ARCHITECTURE.md;
- SOURCE_REGISTRY.jsonl;
- doutrina/index.html;
- fontes/index.html;
- acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.md;
- acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.html;
- acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.json;
- research/EA-000003-000005/teses-institucionais-ibdfam.md.

## 6. Auditoria pública

- páginas HTML: 13;
- hrefs: 263;
- links internos quebrados: 0;
- âncoras quebradas: 0;
- vazamentos de governança: 0;
- seção institucional no dossiê de divórcio: presente;
- seção Teses institucionais em Doutrina: presente;
- seção Instituições jurídicas não governamentais em Fontes: presente.

## 7. Regra de expansão futura

Não criar lista decorativa de entidades. Cada novo ramo/dossiê deve identificar apenas instituições:
- pertinentes à matéria;
- com posição verificável;
- cuja contribuição ajude a mapear convergências, divergências ou controvérsias relevantes.
