# ROADMAP — PRJ-000003 — Ações Judiciais

## Estado atual e histórico de estratégias

**Estado atual em 22/09/2026:** nenhuma Estratégia Autônoma ativa. O bloco abaixo preserva o plano histórico da EA-000003-000001, já concluída.

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

## EA-000003-000007 — Impacto da indenização trabalhista por dano moral na Ação de Repactuação de Dívidas por Superendividamento — CONCLUÍDA

### FASE 01/09 [F-000003-000007-001] — Delimitação jurídica e cenários temporais
**Gate:** escopo, cenários antes/durante/depois do processo e perguntas centrais persistidos.  
**Estado:** CONCLUÍDA.

### FASE 02/09 [F-000003-000007-002] — Marco normativo integrado
**Gate:** núcleo normativo oficial registrado e classificado.  
**Estado:** CONCLUÍDA.

### FASE 03/09 [F-000003-000007-003] — Natureza jurídica e patrimonial da indenização recebida
**Gate:** matriz natureza jurídica → efeito patrimonial → consequência potencial na repactuação persistida.  
**Estado:** CONCLUÍDA.

### FASE 04/09 [F-000003-000007-004] — Cabimento, boa-fé e mínimo existencial
**Gate:** matriz de cabimento e efeitos sobre os requisitos da repactuação concluída sem automatismos.  
**Estado:** CONCLUÍDA.

### FASE 05/09 [F-000003-000007-005] — Fato superveniente, dever de informação e estágios processuais
**Gate:** consequências processuais por marco temporal e deveres de informação documentados.  
**Estado:** CONCLUÍDA.

### FASE 06/09 [F-000003-000007-006] — Efeito sobre o plano, credores e uso do capital
**Gate:** matriz jurídico-financeira de alternativas e limites produzida.  
**Estado:** CONCLUÍDA.

### FASE 07/09 [F-000003-000007-007] — Jurisprudência, doutrina e teses institucionais
**Gate:** matriz de precedentes, doutrina e posições institucionais criticamente confrontadas.  
**Estado:** CONCLUÍDA.

### FASE 08/09 [F-000003-000007-008] — Ferramentas práticas e protocolo de caso
**Gate:** instrumentos práticos revisados e protocolo de interoperabilidade com EA-000004-000022 produzido.  
**Estado:** CONCLUÍDA — checklist, roteiro de entrevista, árvore decisória, quadro antes/depois, manifestação e protocolo interprojetos.

### FASE 09/09 [F-000003-000007-009] — Publicação, auditoria e atualização
**Gate:** publicação verificável, fontes auditadas, ausência de vazamentos e estado atualizado.  
**Estado:** CONCLUÍDA — guia Markdown+HTML publicado, integrações concluídas, 15 HTMLs auditados e deploy 35593885449 success.

**Plano detalhado:** `research/EA-000003-000007/plano-de-fases.md`.  
**Auditoria:** `research/EA-000003-000007/auditoria-final-publicacao.md`.



### Resultado — EA-000003-000007

- 9/9 fases concluídas;
- cenário-base de R$ 100.000,00 líquidos integrado sem tratá-lo como renda recorrente;
- efeitos sobre cabimento, boa-fé, mínimo existencial, fato superveniente e plano estruturados;
- pesquisa superior sem tese específica localizada de captura integral ou exclusão integral da indenização;
- seis ferramentas práticas concluídas;
- guia público em `guias/indenizacao-trabalhista-superendividamento.html`;
- integração com o PRJ-000004 preservando fronteiras jurídica/financeira;
- auditoria global de 15 HTMLs aprovada;
- deploy GitHub Pages `35593885449`: **success**.

## Ciclo corretivo do Relatório do Advogado do Diabo — REQ-20260921-052

### EA-000003-000008 — Fale Conosco, Privacidade e conformidade informacional — CONCLUÍDA
Plano: `research/EA-000003-000008/plano-de-fases.md`.  
5 fases: estado/requisitos → privacidade/retenção → correção do Fale Conosco → recibo/navegação → auditoria/publicação.

### EA-000003-000009 — Revisão adversarial do Superendividamento e da interface com indenização trabalhista — CONCLUÍDA
Plano: `research/EA-000003-000009/plano-de-fases.md`.  
5 fases: exclusões/enquadramento → pesquisa negativa → cenários de capital → sincronização → auditoria/publicação.

### EA-000003-000010 — Revisão adversarial de Divórcio, Partilha, Guarda, Convivência e Alimentos — CONCLUÍDA
Plano: `research/EA-000003-000010/plano-de-fases.md`.  
4 fases: precedentes → dossiê/jurisprudência → proveniência doutrinária → auditoria/publicação.

### EA-000003-000011 — Revisão adversarial da Reclamação Trabalhista com Danos Morais — CONCLUÍDA
Plano: `research/EA-000003-000011/plano-de-fases.md`.  
5 fases: precedentes → responsabilidade/excludentes → gravação → dossiê/índice → auditoria/publicação.

### EA-000003-000012 — Matriz canônica de jurisprudência, paridade Markdown–HTML e auditoria adversarial — CONCLUÍDA
Plano: `research/EA-000003-000012/plano-de-fases.md`.  
5 fases: regra adversarial → matriz de precedentes → paridade → hierarquia normativa → auditoria global.

### EA-000003-000013 — Integridade editorial, proveniência pública e navegação — CONCLUÍDA
Plano: `research/EA-000003-000013/plano-de-fases.md`.  
4 fases: Home → proveniência → Modelos/Mapa → auditoria/publicação.


### Verificação final do ciclo adversarial

- GitHub Pages run `35623051769`: **success**;
- commit público implantado: `717e7c1d0a54b6f3d24a5d76459520f6152d9fab`;
- job `deploy`: **success**;
- etapa `Deploy to GitHub Pages`: **success**;
- reauditoria do corpus: aprovada;
- leitura HTTP direta do domínio `github.io`: não disponível neste ambiente; verificação registrada por pipeline/artefato.

## Frente — Separação de fato sem divórcio × Superendividamento — REQ-20260921-054

### EA-000003-000014 — Separação de fato sem divórcio e unidade econômica familiar no superendividamento — CONCLUÍDA
Plano: `research/EA-000003-000014/plano-de-fases.md`.  
7 fases: delimitação/cronologia → efeitos civis → unidade econômica familiar → jurisprudência/doutrina → prova → riscos/objeções → síntese/auditoria.

**Resultado EA-000003-000014:** 7/7 fases concluídas; casamento formal, separação de fato, unidade econômica e prova foram distinguidos; não localizada regra legal de soma automática da renda do cônjuge; dever de transparência e análise funcional de despesas preservados.

### EA-000003-000015 — Renda do cônjuge não devedor, mínimo existencial e capacidade de pagamento — CONCLUÍDA
Plano: `research/EA-000003-000015/plano-de-fases.md`.  
7 fases: cenários de renda → marco do mínimo existencial → renda informativa versus fonte de pagamento → despesas/dependentes → jurisprudência/doutrina → prova/redação processual → integração.

**Resultado EA-000003-000015:** 7/7 fases concluídas; renda do cônjuge separada em quatro camadas — informação, custeio de despesas, transferência econômica e responsabilidade jurídica — sem soma automática.

### EA-000003-000016 — Patrimônio conjugal, regime de bens e separação de fato na repactuação — CONCLUÍDA
Plano: `research/EA-000003-000016/plano-de-fases.md`.  
7 fases: regime/linha do tempo → comunicabilidade → patrimônio/direitos aquisitivos → capacidade de pagamento → jurisprudência/doutrina → prova/declaração patrimonial → síntese.

**Resultado EA-000003-000016:** 7/7 fases concluídas; patrimônio separado de renda e liquidez; bens financiados tratados por direito aquisitivo + passivo, com controle de meação e período de pagamentos.

### EA-000003-000017 — Apartamento financiado, veículo e limites patrimoniais da repactuação — CONCLUÍDA
Plano: `research/EA-000003-000017/plano-de-fases.md`.  
7 fases: tipologia de bens/garantias → apartamento financiado → veículo quitado/financiado → moradia/mobilidade → avaliação/transparência → jurisprudência/doutrina → ferramentas/integração.

**Resultado EA-000003-000017:** 7/7 fases concluídas; apartamento financiado, veículo quitado e financiamento com alienação fiduciária separados, com checklists e metodologia de valor líquido.

### EA-000003-000018 — Integração da separação de fato, renda do cônjuge e patrimônio ao dossiê de Superendividamento — CONCLUÍDA
Plano: `research/EA-000003-000018/plano-de-fases.md`.  
6 fases: consolidação → revisão do dossiê → ferramentas/modelos → sincronização pública → auditoria adversarial → publicação/fechamento.  
**Dependências:** EA-000003-000014 a EA-000003-000017.

**Resultado EA-000003-000018:** 6/6 fases concluídas; dossiê e modelo integrados; Markdown/HTML sincronizados; fontes específicas expostas; reauditoria global aprovada com 16 HTMLs, 457 hrefs, 69 verificações de âncoras, 4 botões de cópia e zero falhas; GitHub Pages run `35668023210` success.

## EA-000003-000019 — Nova Auditoria do Advogado do Diabo do Site Ações Judiciais — CONCLUÍDA

1. **Fase 01/07 — Inventário integral e delimitação do corpus** — identificar todas as rotas públicas e pares Markdown/HTML.
2. **Fase 02/07 — Paridade Markdown/HTML e integridade editorial** — comparar semanticamente artefatos e arquitetura pública.
3. **Fase 03/07 — Auditoria jurídica adversarial por ação e guia** — atacar teses, pressupostos, exceções e riscos.
4. **Fase 04/07 — Verificação normativa, jurisprudencial e de superveniência** — conferir fontes oficiais e estado atual dos precedentes.
5. **Fase 05/07 — Doutrina, posições institucionais e contraditório** — verificar atribuição, atualidade e equilíbrio.
6. **Fase 06/07 — Contradições transversais e priorização** — cruzar o corpus e classificar achados.
7. **Fase 07/07 — Relatório do Advogado do Diabo e fechamento** — produzir relatório final sem correção silenciosa do corpus.
## Programa editorial — Atualidade, Análise e Observação — CONCLUÍDO

**Dependência transversal:** EA-000002-000008 no PRJ-000002 — Gerador de Agents.

- **EA-000003-000020 — Reorganização editorial e arquitetura de navegação do Site Ações Judiciais.** Estratégia integradora; 6 fases.
- **EA-000003-000021 — Notícias jurídicas dos temas cobertos pelo Site.** 6 fases; inclui cadências semanal, mensal, trimestral, semestral e anual.
- **EA-000003-000022 — Artigos jurídicos críticos e argumentativos.** 6 fases; foco em tese, contraditório e fundamentação legal, jurisprudencial e doutrinária.
- **EA-000003-000023 — Observatório jurídico dos temas cobertos pelo Site.** 7 fases; foco em pesquisa cumulativa, visão sistêmica, horizon scanning e evidência viva.

**Regra de execução:** nenhuma alteração pública de menu/rotas antes da conclusão das fases normativas pertinentes da EA-000002-000008.


## Sincronização canônica pós-Observatório — 22/09/2026

- **EA-000003-000019:** auditoria concluída em 7/7; 10 achados finais priorizados. A própria estratégia registrou que nenhuma correção pública foi executada durante a auditoria; portanto, o ciclo corretivo desses achados continua sendo uma frente material distinta.
- **EA-000003-000020 a EA-000003-000023:** programa editorial concluído e publicado; deploy integrado `35728854051` com success.
- **EA-000003-000024:** arquitetura Coleção → Detalhe concluída; deploy `35740233434` com success.
- **EA-000003-000025:** síntese institucional da Home concluída; deploy `35747259846` com success.
- **EA-000003-000026:** separação entre monitoramento interno e Site Público concluída; deploy `35753373991` com success. Rastreabilidade do fechamento reconciliada por evento append-only em 22/09/2026.
- **EA-000003-000027:** arquitetura pública do Observatório Jurídico concluída; deploy `35756498839` com success.
- **Estado corrente:** nenhuma estratégia ativa. Próxima frente material comprovada: ciclo corretivo específico dos 10 achados da EA-000003-000019, salvo novo pedido que altere a prioridade.


## Ciclo corretivo dos 10 achados da EA-000003-000019

- **EA-000003-000028 — Correção adversarial do dossiê de Direito das Famílias** — CONCLUÍDA; 6/6; A-01, A-02 e A-08 corrigidos; run `35759582362` success.
- **EA-000003-000029 — Correção adversarial do dossiê trabalhista e da proveniência institucional** — CONCLUÍDA; 6/6; A-03, A-04, A-07 e A-09 corrigidos; run `35760077593` success.
- **EA-000003-000030 — Correção adversarial de Superendividamento e Doutrina** — CONCLUÍDA; 5/5; A-05, A-06 e A-10 corrigidos; run `35760822807` success.
- **EA-000003-000031 — Reauditoria regressiva pós-correção do Site Ações Judiciais** — CONCLUÍDA; 5/5; 10/10 achados corrigidos e revalidados; regressão pública de monitoramento corrigida; 24 HTMLs, 633 hrefs, zero links/âncoras quebrados; run `35763781353` success.
