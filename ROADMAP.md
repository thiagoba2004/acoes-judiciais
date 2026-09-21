# ROADMAP — PRJ-000003 — Ações Judiciais

## Estratégia corrente

**EA-000003-000001 — Ação de Repactuação de Dívidas por Superendividamento**

### FASE 01/08 [F-000003-000001-001] — Delimitação e perguntas de pesquisa
Definir objeto, objetivo, público, questões jurídicas e fronteiras entre informação geral e análise de caso concreto.  
**Gate:** perguntas de pesquisa e escopo persistidos.

### FASE 02/08 [F-000003-000001-002] — Marco normativo e conceitos
Levantar e verificar fontes normativas, conceitos jurídicos e requisitos relevantes.  
**Gate:** fontes primárias centrais registradas e verificadas.

### FASE 03/08 [F-000003-000001-003] — Cabimento, legitimidade e competência
Mapear hipóteses de cabimento/não cabimento, sujeitos, competência e questões processuais de entrada.  
**Gate:** matriz de admissibilidade produzida.

### FASE 04/08 [F-000003-000001-004] — Fatos, documentos, prova e cálculos
Estruturar documentos, fatos relevantes, ônus probatórios e cálculos necessários.  
**Gate:** checklist probatório e variáveis documentadas.

### FASE 05/08 [F-000003-000001-005] — Procedimento, pedidos e alternativas
Reconstruir o fluxo processual e alternativas possíveis sem presumir estratégia adequada a todo caso.  
**Gate:** mapa processual e opções persistidos.

### FASE 06/08 [F-000003-000001-006] — Jurisprudência, doutrina e controvérsias
Pesquisar precedentes e doutrina, distinguindo entendimento consolidado, divergência e hipótese.  
**Gate:** fundamentos críticos verificáveis.

### FASE 07/08 [F-000003-000001-007] — Ferramentas práticas
Produzir checklists, roteiro de triagem e, se aprovado, modelos reutilizáveis com variáveis explícitas.  
**Gate:** instrumentos revisados e coerentes com as fontes.

### FASE 08/08 [F-000003-000001-008] — Publicação, auditoria e fechamento
Gerar/sincronizar Markdown + HTML; JSON apenas quando houver função estruturada real, revisar links e fontes e verificar publicação.  
**Gate:** dossiê publicável, coerente e verificável.


## EA-000003-000002 — Arquitetura pública e identidade visual do Site Ações Judiciais

1. **Fase 01/05 — Arquitetura de informação e identidade visual** — definir menu global, páginas centrais, hierarquia pública e design tokens exclusivos.
2. **Fase 02/05 — Implementação do sistema global** — criar CSS, cabeçalho, menu responsivo, componentes e rodapé compartilhados.
3. **Fase 03/05 — Construção das páginas centrais** — criar e popular as áreas do menu com conteúdo existente e rotas claras.
4. **Fase 04/05 — Migração e integração do conteúdo atual** — adaptar páginas já publicadas à nova navegação e identidade.
5. **Fase 05/05 — Auditoria, deploy e verificação pública** — testar navegação, responsividade, ausência de vazamento interno e publicação GitHub Pages.


## EA-000003-000003 — Mapa do Site, Início enxuto e Fale Conosco protocolado

1. **Fase 01/04 — Recuperação do padrão e desenho da correção** — recuperar a implementação do Fale Conosco do Classe e Massas e fixar arquitetura.
2. **Fase 02/04 — Implementação** — retirar catálogo de menus da Início, criar Mapa do Site, inserir Fale Conosco no menu e adaptar protocolo/e-mail.
3. **Fase 03/04 — Testes funcionais** — testar geração de protocolo, submissão, confirmação, navegação e responsividade.
4. **Fase 04/04 — Deploy, auditoria e fechamento** — publicar, verificar o GitHub Pages e encerrar a estratégia.


## EA-000003-000003 — CONCLUÍDA

Fale Conosco protocolado implantado e verificado end-to-end com Forminit + EmailJS.

- Forminit: `lprwcdbax4y`;
- EmailJS Service: `service_3dyw7gl`;
- EmailJS Template: `template_jz6al72`;
- teste real: `AJ-20260920-164456-E2CFB5`;
- estado final: `E2E_VERIFICADO`;
- dívida não bloqueante: primeira entrega ao Yahoo ocorreu em Spam.


## EA-000003-000004 — Menu Doutrina — correção arquitetural — CONCLUÍDA

1. **Fase 01/03 — Decisão arquitetural e escopo** — definir o papel público de Doutrina e sua relação com Fontes, Legislação e Jurisprudência.
2. **Fase 02/03 — Implementação e integração** — criar rota, conteúdo inicial, menu global e Mapa do Site.
3. **Fase 03/03 — Auditoria, deploy e fechamento** — verificar navegação, coerência conceitual, mobile e publicação.

**Origem:** auditoria comprovou que Doutrina já existia como camada de pesquisa, mas foi omitida na transposição para a arquitetura pública.

**Decisão da Fase 01:** Doutrina é área material própria; Fontes é camada transversal de proveniência. Menu aprovado pela lógica arquitetural: Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Fale Conosco.


### Resultado — EA-000003-000004

- Doutrina criada como Menu de primeiro nível;
- par canônico `doutrina/index.md + .html`; JSON somente se houver uso estruturado comprovado;
- menu global final: **Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Fale Conosco**;
- Mapa do Site atualizado;
- quatro referências doutrinárias iniciais sobre Superendividamento;
- auditoria: 12 páginas HTML, 159 links internos e 11 âncoras, sem quebra;
- deploy público `35537406550`: **success**.


## EA-000003-000005 — Ação de Divórcio Litigioso c/c Partilha de Bens, Guarda, Convivência e Alimentos — CONCLUÍDA

### FASE 01/09 [F-000003-000005-001] — Delimitação e perguntas de pesquisa
Definir objeto, público, pressupostos, hipóteses de cumulação e perguntas jurídicas centrais, distinguindo informação geral de análise de caso concreto.  
**Gate:** escopo, perguntas e limites persistidos.

### FASE 02/09 [F-000003-000005-002] — Marco normativo, casamento e regime de bens
Levantar e verificar Constituição, Código Civil, Código de Processo Civil, Estatuto da Criança e do Adolescente, Lei de Alimentos e demais fontes primárias pertinentes, incluindo regime de bens e efeitos patrimoniais do casamento.  
**Gate:** núcleo normativo primário registrado, datado e classificado.

### FASE 03/09 [F-000003-000005-003] — Competência, rito, cumulação, segredo de justiça e tutelas provisórias
Mapear competência, procedimento, possibilidade e limites da cumulação dos pedidos, intervenção do Ministério Público quando aplicável, segredo de justiça e tutelas provisórias, sem tratar medidas urgentes como automáticas.  
**Gate:** matriz processual de entrada e urgência verificada.

### FASE 04/09 [F-000003-000005-004] — Partilha: acervo, comunicabilidade, dívidas, avaliação e prova
Estruturar identificação do patrimônio, datas relevantes, titularidade formal, comunicabilidade, passivos, avaliação de ativos, frutos, empresas, financiamentos e documentos probatórios, preservando controvérsias conforme o regime de bens.  
**Gate:** matriz bem/dívida/regime/fato/prova e metodologia de avaliação persistidas.

### FASE 05/09 [F-000003-000005-005] — Guarda, convivência e proteção integral
Examinar guarda, convivência, rotina, tomada de decisões, melhor interesse da criança/adolescente, prova, escuta protegida quando juridicamente cabível e situações de risco ou violência, sem converter preferências parentais em presunções jurídicas.  
**Gate:** mapa de questões, provas e alternativas de organização parental verificado.

### FASE 06/09 [F-000003-000005-006] — Alimentos provisórios e definitivos
Mapear titulares, necessidades, capacidade contributiva, proporcionalidade, despesas ordinárias e extraordinárias, alimentos provisórios/definitivos, eventual obrigação entre ex-cônjuges e efeitos processuais relevantes.  
**Gate:** matriz necessidade/capacidade/proporcionalidade/prova e variáveis de cálculo documentadas.

### FASE 07/09 [F-000003-000005-007] — Jurisprudência, doutrina e controvérsias
Pesquisar precedentes e doutrina sobre partilha, bens particulares/comuns, dívidas, guarda, convivência, alimentos, empresas, previdência, imóveis e demais controvérsias encontradas, distinguindo entendimento consolidado, divergência e hipótese.  
**Gate:** fundamentos críticos e controvérsias verificáveis.

### FASE 08/09 [F-000003-000005-008] — Ferramentas práticas e modelos
Produzir roteiro de triagem, checklist documental, inventário patrimonial, matriz de despesas dos filhos, cronologia, quadro de pedidos/tutelas e, se adequado, modelos reutilizáveis com variáveis explícitas e alertas de adaptação ao caso concreto.  
**Gate:** instrumentos revisados e coerentes com fontes e limites profissionais.

### FASE 09/09 [F-000003-000005-009] — Publicação, interoperabilidade financeira, auditoria e fechamento
Sincronizar Markdown + HTML; JSON apenas quando houver função estruturada real, integrar Legislação/Jurisprudência/Doutrina/Fontes, relacionar consequências financeiras ao PRJ-000004 sem transferir conclusões jurídicas, auditar links, workflow Pages e publicação.  
**Gate:** dossiê publicável, verificável, sem vazamento de governança e com interface interprojetos documentada.


### Resultado — EA-000003-000005

- 9/9 fases concluídas;
- novo dossiê público em Markdown + HTML; JSON apenas quando houver função estruturada real;
- integração com Ações, Guias, Modelos, Jurisprudência, Doutrina, Legislação e Mapa do Site;
- roteiro de triagem, checklist, inventário patrimonial, despesas dos filhos, cronologia, quadro de pedidos/tutelas e estrutura-base de petição;
- interface formal com o Projeto Planejamento Financeiro;
- auditoria final: 13 HTMLs, 256 hrefs, zero links internos quebrados, zero âncoras locais quebradas e zero vazamentos de governança;
- deploy público 35540435610: **success**.


## Manutenção — Auditoria de entidades jurídicas das ações publicadas — 20/09/2026

**Escopo:** dossiês públicos de Superendividamento e Divórcio Litigioso.

**Resultado institucional:**
- Superendividamento: BRASILCON e Idec incorporados; MPCON mantido em monitoramento sem atribuição artificial de tese;
- Divórcio: IBDFAM mantido e ampliado; ADFAS incorporada com tese histórica classificada como superada pelo Tema 1053 do STF; IBDCivil mantido em monitoramento sem atribuição artificial de tese;
- Doutrina e Fontes ampliadas com camada institucional por ramo;
- Mapa do Site atualizado com acesso às seções de teses institucionais;
- regra metodológica preservada: só há atribuição de tese quando existe posição institucional própria, oficial e recuperável.

**Auditoria pública:**
- 13 páginas HTML;
- 277 hrefs;
- 0 links internos quebrados;
- 0 âncoras quebradas;
- 0 vazamentos de governança;
- menu global uniforme;
- 32 cards clicáveis, 11 cards estáticos e 0 usos ambíguos.

## EA-000003-000006 — Reclamação Trabalhista com pedido de Indenização por Danos Morais — CONCLUÍDA

### FASE 01/09 [F-000003-000006-001] — Delimitação, hipóteses de dano e perguntas de pesquisa
Mapear hipóteses de dano moral no contexto laboral e formular as perguntas jurídicas centrais, sem presumir que toda ilicitude trabalhista gere dano moral indenizável.  
**Gate:** escopo, taxonomia inicial, perguntas e limites persistidos.  
**Estado:** CONCLUÍDA — 12 grupos de hipóteses e 40 perguntas de pesquisa persistidos.

### FASE 02/09 [F-000003-000006-002] — Marco normativo e responsabilidade civil trabalhista
Levantar e verificar Constituição, CLT, Código Civil, CPC, legislação especial e fontes primárias pertinentes.  
**Gate:** núcleo normativo registrado, datado e classificado.  
**Estado:** CONCLUÍDA — Constituição, CLT, Código Civil, CPC, legislação especial e precedentes constitucionais centrais sistematizados.

### FASE 03/09 [F-000003-000006-003] — Competência, legitimidade, prescrição e estrutura processual
Mapear competência, legitimidade, prescrição, cumulação, rito, valor da causa, tutela provisória e requisitos processuais.  
**Gate:** matriz processual de entrada verificada.  
**Estado:** CONCLUÍDA — controvérsias dos IRR 215, 200 e 35 tratadas como pendentes, sem simplificação.

### FASE 04/09 [F-000003-000006-004] — Fatos, documentos, prova e ônus probatório
Estruturar cronologia, documentos, prova testemunhal, prova digital, registros internos, documentos médicos/ocupacionais quando pertinentes e ônus probatório.  
**Gate:** matriz fato–elemento jurídico–prova e checklist documental persistidos.  
**Estado:** CONCLUÍDA — matriz probatória, preservação digital, gravações, testemunhas, saúde, assédio, discriminação, acidente e ônus dinâmico estruturados.

### FASE 05/09 [F-000003-000006-005] — Elementos da responsabilidade, defesas e controvérsias
Examinar ilicitude, dano, nexo, imputação, culpa ou risco conforme o caso, excludentes e principais linhas defensivas.  
**Gate:** matriz de responsabilidade e defesas previsíveis documentada.  
**Estado:** CONCLUÍDA — responsabilidade subjetiva/objetiva, prepostos, excludentes, fato de terceiro, compliance, mitigação e bis in idem estruturados.

### FASE 06/09 [F-000003-000006-006] — Quantificação da indenização e repercussões
Pesquisar critérios jurídicos de arbitramento, gravidade, duração, repercussão, proporcionalidade e controvérsias sobre parâmetros de fixação.  
**Gate:** metodologia de análise do quantum e mapa de controvérsias verificados.  
**Estado:** CONCLUÍDA — art. 223-G tratado como referência orientativa pós-STF; metodologia do quantum, agravantes, mitigantes e danos autônomos persistidos.

### FASE 07/09 [F-000003-000006-007] — Jurisprudência, doutrina e teses institucionais
Pesquisar STF, TST, TRTs, doutrina e posições institucionais recuperáveis de entidades jurídicas especializadas.  
**Gate:** matriz jurisprudencial, camada doutrinária e teses institucionais criticamente confrontadas.  
**Estado:** CONCLUÍDA — STF, TST qualificado, TRTs, doutrina, ANAMATRA e ABRAT separados por força e natureza; ANPT monitorada.

### FASE 08/09 [F-000003-000006-008] — Ferramentas práticas e modelos
Produzir roteiro de triagem, cronologia, checklist de provas, matriz de danos e nexo, quadro de pedidos, mapa de riscos e, se adequado, estrutura-base de petição inicial.  
**Gate:** instrumentos revisados e coerentes com as fontes.  
**Estado:** CONCLUÍDA — triagem, cronologia, matriz dano–nexo, quadro de pedidos/riscos e estrutura-base da inicial produzidos.

### FASE 09/09 [F-000003-000006-009] — Publicação, auditoria e fechamento
Sincronizar Markdown + HTML; criar JSON apenas se houver função estruturada real; integrar Menus pertinentes, auditar fontes, links, governança, responsividade e GitHub Pages.  
**Gate:** dossiê publicável, verificável, sem vazamento de governança e com deploy comprovado.  
**Estado:** CONCLUÍDA — dossiê publicado, hipótese específica de assalto/roubo incorporada, 14 HTMLs/338 hrefs auditados sem links ou âncoras quebrados, zero vazamentos, modelo com botão de cópia correto e deploy 35550557280 success.

### Resultado — EA-000003-000006

- 9/9 fases concluídas;
- dano moral trabalhista tratado sem automatismo;
- assédio, discriminação, acidente/doença, privacidade, retaliação e violência estruturados;
- hipótese de assalto/roubo incorporada com distinção entre risco especial e comércio comum;
- responsabilidade subjetiva/objetiva, prepostos e excludentes sistematizados;
- competência, prescrição e temas qualificados pendentes separados;
- prova digital, gravações, testemunhas e documentos médicos estruturados;
- quantum sem tabela automática e art. 223-G tratado conforme STF;
- STF, TST, TRTs, doutrina, ANAMATRA e ABRAT organizados por força/natureza;
- ferramentas práticas e modelo reutilizável produzidos;
- publicação em Markdown + HTML, sem JSON narrativo;
- integração pública em Ações, Guias, Modelos, Jurisprudência, Doutrina, Legislação, Fontes e Mapa do Site;
- auditoria técnica final aprovada;
- deploy GitHub Pages `35550557280`: **success**.

**Plano detalhado:** `research/EA-000003-000006/plano-de-fases.md`.

## Frente interprojetos — Indenização trabalhista líquida × Superendividamento

**Origem:** REQ-20260921-042.  
**Integração:** PRJ-000003 ↔ PRJ-000004.  
**Estratégia financeira correlata:** EA-000004-000022.

## EA-000003-000007 — Impacto da indenização trabalhista por dano moral na Ação de Repactuação de Dívidas por Superendividamento — PLANEJADA

### FASE 01/09 [F-000003-000007-001] — Delimitação jurídica e cenários temporais
**Gate:** escopo, cenários antes/durante/depois do processo e perguntas centrais persistidos.

### FASE 02/09 [F-000003-000007-002] — Marco normativo integrado
**Gate:** núcleo normativo oficial registrado e classificado.

### FASE 03/09 [F-000003-000007-003] — Natureza jurídica e patrimonial da indenização recebida
**Gate:** matriz natureza jurídica → efeito patrimonial → consequência potencial na repactuação persistida.

### FASE 04/09 [F-000003-000007-004] — Cabimento, boa-fé e mínimo existencial
**Gate:** matriz de cabimento e efeitos sobre os requisitos da repactuação concluída sem automatismos.

### FASE 05/09 [F-000003-000007-005] — Fato superveniente, dever de informação e estágios processuais
**Gate:** consequências processuais por marco temporal e deveres de informação documentados.

### FASE 06/09 [F-000003-000007-006] — Efeito sobre o plano, credores e uso do capital
**Gate:** matriz jurídico-financeira de alternativas e limites produzida.

### FASE 07/09 [F-000003-000007-007] — Jurisprudência, doutrina e teses institucionais
**Gate:** matriz de precedentes, doutrina e posições institucionais criticamente confrontadas.

### FASE 08/09 [F-000003-000007-008] — Ferramentas práticas e protocolo de caso
**Gate:** instrumentos práticos revisados e protocolo de interoperabilidade com EA-000004-000022 produzido.

### FASE 09/09 [F-000003-000007-009] — Publicação, auditoria e atualização
**Gate:** publicação verificável, fontes auditadas, ausência de vazamentos e estado atualizado.

**Plano detalhado:** `research/EA-000003-000007/plano-de-fases.md`.

