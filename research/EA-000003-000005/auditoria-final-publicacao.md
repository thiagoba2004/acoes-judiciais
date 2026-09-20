# Auditoria final de publicação — Divórcio litigioso

**Projeto:** Ações Judiciais  
**Estratégia:** EA-000003-000005 — Ação de Divórcio Litigioso c/c Partilha de Bens, Guarda, Convivência e Alimentos  
**Data:** 20/09/2026  
**Fase:** 09/09 — Publicação, interoperabilidade financeira, auditoria e fechamento

## 1. Escopo auditado

Camada pública:
- `index.html`;
- `acoes/index.html`;
- dois dossiês em `acoes/`;
- `guias/index.html`;
- `modelos/index.html`;
- `jurisprudencia/index.html`;
- `doutrina/index.html`;
- `legislacao/index.html`;
- `fontes/index.html`;
- `fale-conosco/index.html`;
- `fale-conosco/recebido.html`;
- `mapa-do-site/index.html`.

Também foram verificados:
- `.github/workflows/pages.yml`;
- trio canônico do novo dossiê em Markdown + HTML + JSON;
- integração com a área Doutrina;
- interface documentada com o Projeto Planejamento Financeiro.

## 2. Resultado da varredura HTML

- páginas HTML auditadas: **13**;
- referências `href` examinadas: **256**;
- links internos apontando para arquivo inexistente: **0**;
- âncoras locais quebradas: **0**;
- páginas com divergência no Menu global: **0**;
- marcadores de governança interna encontrados na camada pública: **0**.

Marcadores pesquisados incluíram códigos e estados internos do tipo PRJ, EA, F, REQ, EVT, PROJECT_STATE, STRATEGY_LOG e estados editoriais/de execução.

## 3. Menu global

Menu verificado nas páginas públicas:

**Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Fale Conosco**

Resultado: consistente nas 13 páginas auditadas.

## 4. Modelos

### Superendividamento
- botão: **COPIAR MODELO**;
- alvo: `modelo-peticao`;
- alvo existente: **sim**.

### Divórcio litigioso
- botão: **COPIAR MODELO**;
- alvo: `modelo-divorcio`;
- alvo existente: **sim**.

O botão permanece imediatamente associado ao conteúdo copiável e não foi substituído por linguagem redundante de navegação.

## 5. Integração temática do novo dossiê

Confirmada presença em:
- Ações;
- Guias;
- Modelos;
- Jurisprudência;
- Doutrina;
- Legislação;
- Mapa do Site.

A Home permaneceu institucional e enxuta.

## 6. Workflow GitHub Pages

O workflow:
- observa alterações em `acoes/**`, `guias/**`, `modelos/**`, `jurisprudencia/**`, `doutrina/**`, `legislacao/**`, `fontes/**`, `fale-conosco/**` e `mapa-do-site/**`;
- cria diretório `_site/acoes`;
- copia `acoes/*.html` para o artefato público.

Logo, `acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.html` está coberto pelo processo de publicação.

## 7. Deploy

Última execução pública correspondente ao estado integrado:

- workflow run: **35540435610**;
- conclusão: **success**;
- commit público: **b794a3a30d23e0ca63ce7dcbbc1c80fa9fa4f0b6**.

A ferramenta externa de leitura de páginas usada na auditoria não conseguiu abrir diretamente o domínio GitHub Pages nesta sessão; por isso a comprovação de deploy foi feita pelo pipeline oficial do próprio repositório. Não há evidência de falha de publicação no workflow.

## 8. Interoperabilidade com Planejamento Financeiro

Documento de interface:
`research/EA-000003-000005/interface-planejamento-financeiro.md`.

Regras confirmadas:
- direito confirmado pode alimentar premissa financeira;
- questão jurídica pendente deve ser transmitida como cenário;
- pedido não vira direito adquirido;
- valor pretendido não vira valor judicial;
- bem litigioso não vira patrimônio líquido disponível;
- guarda pretendida não vira premissa definitiva de moradia;
- alimentos pedidos não viram fluxo garantido.

## 9. Gate final

**SATISFEITO.**

O dossiê:
- possui Markdown + HTML + JSON;
- está integrado às áreas públicas pertinentes;
- mantém Doutrina como camada própria;
- possui ferramentas práticas e modelo reutilizável;
- não expõe governança interna na UI pública;
- não possui quebra interna detectada;
- está abrangido pelo workflow Pages;
- possui deploy de sucesso;
- possui interface interprojetos documentada.

**Estado final da estratégia: CONCLUÍDA.**
