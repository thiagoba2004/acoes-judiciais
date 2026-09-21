# Auditoria final — entidades jurídicas das ações publicadas

**Data:** 20/09/2026  
**Pedido:** REQ-20260920-032

## 1. Dossiês auditados

Foram identificadas duas ações judiciais efetivamente publicadas:

1. Ação de Repactuação de Dívidas por Superendividamento;
2. Ação de Divórcio Litigioso c/c Partilha de Bens, Guarda, Convivência e Alimentos.

A rota `acoes/index.html` é catálogo, não terceiro dossiê.

## 2. Superendividamento

### Incorporadas

**BRASILCON — Instituto Brasileiro de Política e Direito do Consumidor**
- posição institucional própria sobre Lei nº 14.181/2021, crédito responsável e mínimo existencial;
- requerimento de revogação do Decreto nº 11.150/2022;
- atuação como amicus curiae em discussão constitucional;
- relação atual: `DIVERGENTE_EM_PARTE_COM_SUPERVENIENCIA`, pois o STF em 23/04/2026 preservou a possibilidade de parâmetro quantitativo por decreto, mas exigiu revisão técnica anual e afastou a exclusão do consignado.

**Idec — Instituto de Defesa de Consumidores**
- posição institucional contrária a valor nominal rígido do mínimo existencial;
- defesa de metodologia sensível a moradia, saúde, alimentação, transporte, educação, condição individual e histórico de endividamento;
- relação atual: `DIVERGENTE_EM_PARTE_E_CONVERGENTE_QUANTO_A_NECESSIDADE_DE_BASE_TECNICA`.

### Monitorada

**MPCON — Associação Nacional do Ministério Público do Consumidor**
- entidade relevante;
- nesta auditoria, não foi localizada tese institucional própria suficientemente delimitada sobre a repactuação para atribuição autônoma;
- status: `MONITORAR`.

## 3. Divórcio e Direito das Famílias

### Incorporadas

**IBDFAM — Instituto Brasileiro de Direito de Família**
- já incorporado com Enunciados 01, 02, 14, 18, 46, 47, 58 e 60;
- cada enunciado possui confronto com o Direito atual.

**ADFAS — Associação de Direito de Família e das Sucessões**
- parecer institucional de 2019 sustentou a permanência da separação judicial como faculdade após a EC 66/2010;
- relação atual: `SUPERADA`;
- o Tema 1053 do STF fixou que a separação judicial não subsiste como figura autônoma após a EC 66/2010, preservados atos jurídicos perfeitos anteriores.

### Monitorada

**IBDCivil — Instituto Brasileiro de Direito Civil**
- associação civilista relevante, com produção acadêmica e atuação institucional;
- não foi localizada tese institucional específica e recuperável sobre o dossiê atual que justificasse atribuição;
- artigos publicados em sua revista permanecem atribuídos aos autores;
- status: `MONITORAR`.

## 4. Camadas públicas atualizadas

- dossiê de Superendividamento — Markdown + HTML + JSON;
- dossiê de Divórcio — Markdown + HTML + JSON;
- Doutrina — Markdown + HTML + JSON;
- Fontes — Markdown + HTML + JSON;
- Mapa do Site — Markdown + HTML + JSON;
- SOURCE_REGISTRY.jsonl.

## 5. Regra metodológica aplicada

A entidade somente é apresentada como fonte de tese institucional quando:
- existe posição própria;
- a autoria institucional é atribuível;
- há fonte oficial recuperável;
- o conteúdo é materialmente relevante;
- a tese pode ser confrontada com legislação e jurisprudência.

A mera hospedagem de artigo ou notícia não transforma o conteúdo em posição da entidade.

## 6. Auditoria técnica pública

- páginas HTML: **13**;
- hrefs: **277**;
- links externos: **70**;
- links internos quebrados: **0**;
- âncoras quebradas: **0**;
- vazamentos de governança: **0**;
- variantes do menu global: **1**;
- cards clicáveis: **32**;
- cards estáticos: **11**;
- usos ambíguos de `.resource-card`: **0**.

## 7. GitHub Pages

Workflow: **Deploy public site to GitHub Pages**  
Run: **35546489572**  
Commit público: **05ae89a576b0edd91998f7bc91cfe4fb417cdc9e**  
Estado: **completed / success**

Etapas:
- Checkout: success;
- Build public-only artifact: success;
- Setup Pages: success;
- Upload Pages artifact: success;
- Deploy to GitHub Pages: success.

## 8. Conclusão

A auditoria foi concluída com incorporação de quatro entidades com teses institucionais verificáveis:
- IBDFAM;
- ADFAS;
- BRASILCON;
- Idec.

Duas entidades permanecem monitoradas sem atribuição artificial de tese:
- IBDCivil;
- MPCON.

**Gate final:** SATISFEITO.
