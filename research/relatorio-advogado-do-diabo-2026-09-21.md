# Relatório do Advogado do Diabo — Auditoria adversarial do Site Ações Judiciais

**Projeto:** PRJ-000003 — Ações Judiciais
**Data:** 21/09/2026
**Escopo:** corpus público do Site (15 HTMLs públicos, 14 Markdown editoriais correspondentes e página operacional de recibo), confrontado com documentos internos apenas para testar coerência e estado atual.
**Estado:** ACHADOS_REQUEREM_CORRECAO

## 1. Método

A revisão foi deliberadamente adversarial. Cada afirmação foi tratada como se fosse contestada por parte contrária, magistrado, advogado adverso, pesquisador crítico ou usuário que tentasse aplicar o texto literalmente.

Foram procurados erro jurídico objetivo, generalização excessiva de precedente, omissão de condição ou exceção relevante, confusão entre tese vinculante e fonte persuasiva, divergência Markdown/HTML, contradição interna, afirmação negativa não reproduzível, problema de proveniência, risco de atualização e risco de indução ao uso profissional sem salvaguarda suficiente.

## 2. Síntese executiva

O Site está estruturalmente organizado e vários enunciados jurídicos centrais resistiram à revisão adversarial. Contudo, há problemas materiais que justificam revisão antes de considerar o corpus fechado.

Achados prioritários: a seção de exclusões do superendividamento comprime regimes distintos dos arts. 54-A, § 3º, e 104-A, § 1º, do CDC; o Tema 1.236/STF pode ser lido como faculdade unilateral; o IRR 84/TST é apresentado sem o estado oficial RE Pendente; culpa concorrente aparece sob rubrica de excludentes; o Fale Conosco diverge entre Markdown, HTML e estado E2E; falta política/aviso público de privacidade para o formulário; há divergências materiais Markdown/HTML; Jurisprudência não espelha todos os temas pendentes do dossiê; Mapa do Site lista apenas dois dos quatro modelos; e dois links bibliográficos de Direito das Famílias apontam para uma disciplina da USP em vez de fonte adequada da obra.

## 3. Achados de prioridade alta

### AJ-ADV-001 — Superendividamento: duas categorias de exclusão foram comprimidas em uma só

O dossiê acerta parte das exclusões do art. 104-A, § 1º, mas não explicita adequadamente que o art. 54-A, § 3º, também retira do capítulo situações de fraude ou má-fé e aquisição/contratação de produtos e serviços de luxo de alto valor.

**Risco:** a árvore de cabimento pode ser montada sem testar categorias normativas distintas.

**Correção:** criar quadro separado entre exclusões/limitações do art. 54-A, § 3º, e dívidas excluídas da repactuação pelo art. 104-A, § 1º.

### AJ-ADV-002 — Tema 1.236/STF: risco de leitura como faculdade unilateral

A redação deve dizer expressamente que o afastamento do regime depende de manifestação de vontade das partes por escritura pública. A forma atual pode sugerir poder unilateral da pessoa maior de 70 anos.

### AJ-ADV-003 — Fale Conosco: texto canônico objetivamente desatualizado

O Markdown afirma backend indisponível. O PROJECT_STATE registra E2E_VERIFICADO e o teste de 20/09/2026 documenta submissão, confirmação e entrega. O HTML ainda contém texto estático de configuração que é ocultado em runtime.

**Risco:** três versões da verdade coexistem.

### AJ-ADV-004 — Fale Conosco: transparência LGPD insuficiente

O formulário coleta nome/pseudônimo, e-mail, assunto, mensagem, link e anexos, mas não foi localizada política pública com finalidade, duração, controlador, compartilhamentos, direitos e demais informações de transparência.

### AJ-ADV-005 — IRR 84/TST: tese sem estado recursal

A tese foi firmada/publicada, mas a ficha oficial registra RE Pendente. O status deve acompanhar a tese para evitar impressão de estabilidade superior à indicada pela própria fonte.

## 4. Achados de prioridade média

### AJ-ADV-006 — Culpa concorrente não deve aparecer indistintamente como excludente

Separar causas de exclusão de responsabilidade/nexo de fatores que podem reduzir a indenização ou repartir causalidade.

### AJ-ADV-007 — Tema 932/STF precisa conservar o recorte de acidente de trabalho

O Tema 932 trata de danos decorrentes de acidentes de trabalho em atividade de risco. Em dossiê amplo de danos morais, deixar explícito que assédio, discriminação e outros ilícitos exigem fundamentos próprios.

### AJ-ADV-008 — Página Jurisprudência incompleta em relação ao dossiê trabalhista

O Markdown destaca Temas 103, 107 e 117; o dossiê registra também 200, 215 e 35 como pendentes. O índice deve ser derivado de fonte única de status.

### AJ-ADV-009 — Alimentos: “horas extras podem integrar” é impreciso

O STJ em 2026 formulou que, quando os alimentos são fixados em percentual sobre rendimentos líquidos, horas extras, mesmo não habituais, integram a base; a PLR não entra automaticamente e depende de necessidade específica.

### AJ-ADV-010 — Guia da indenização: pesquisa negativa não reproduzível

A frase “não foi localizado precedente superior específico” deve informar data de corte, tribunais, bases e termos de busca ou remeter a nota metodológica recuperável.

### AJ-ADV-011 — Guia da indenização: quitação/amortização seletiva exige ressalva mais forte

Não deve soar como estratégia neutra. Seu impacto depende da fase processual, boa-fé, fotografia global do passivo, plano e efeitos sobre os demais credores.

### AJ-ADV-012 — Doutrina: links bibliográficos inadequados

As obras de Cristiano Chaves de Farias/Nelson Rosenvald e Rodrigo da Cunha Pereira usam como destino a mesma página de disciplina da USP. Substituir por editora, ISBN, catálogo bibliográfico, biblioteca ou página oficial pertinente.

### AJ-ADV-013 — Legislação mistura lei e soft law

Recomendação do CNJ é relevante, mas não é legislação em sentido próprio. Melhor separar “legislação” de “atos normativos/institucionais” ou ampliar o nome da área.

### AJ-ADV-014 — Markdown canônico versus HTML público

O projeto declara Markdown como texto canônico, mas Legislação e Jurisprudência têm HTML materialmente mais rico e o Fale Conosco está desatualizado no Markdown. Isso ameaça regeneração e auditoria.

### AJ-ADV-015 — Fontes promete proveniência maior que a rastreabilidade pública

O SOURCE_REGISTRY interno é robusto, mas o público vê principalmente categorias. Teses relevantes deveriam exibir fonte direta, órgão/autoria, data, status e data de consulta.

### AJ-ADV-016 — Home: “uso profissional” sem ressalva global equivalente

Melhor “apoio ao estudo e à pesquisa profissional” ou ressalva institucional curta sobre validação temporal, territorial e factual antes do uso em caso real.

### AJ-ADV-017 — Mapa do Site não espelha todos os modelos

Modelos oferece quatro itens; o Mapa lista apenas repactuação e manifestação de indenização superveniente. Faltam divórcio e reclamação trabalhista.

## 5. Achados de baixa prioridade

### AJ-ADV-018 — Atualidade deve acompanhar o precedente

Data geral no rodapé não substitui status/data de consulta perto de tese com RE pendente, afetação ou mudança recente.

### AJ-ADV-019 — Gravação ambiental: reforçar autenticidade e integridade

A licitude pelo Tema 237 não resolve, sozinha, autenticidade, integridade, contexto, pertinência ou alegação de edição/manipulação.

### AJ-ADV-020 — Modelos: manter aviso junto ao texto copiável

As advertências atuais são adequadas. Ainda assim, convém conservar no início de cada modelo “estrutura-base, não petição pronta”, data de revisão e jurisdição a confirmar.

## 6. Pontos que resistiram ao ataque

Não foi identificado erro material na síntese das ADPFs 1005/1006/1097 sobre mínimo existencial e consignado; nas teses centrais da Jurisprudência em Teses 282/STJ; no Tema 1053/STF; na comunicabilidade do FGTS do período conjugal em comunhão parcial; na distinção de 2026 entre horas extras e PLR, ressalvada a precisão redacional; nas ADIs 6050/6069/6082; nem na regra central do Tema 237/STF.

## 7. Cobertura página a página

| Página | Resultado adversarial |
|---|---|
| Início | ressalva sobre “uso profissional” |
| Ações | sem erro material autônomo |
| Repactuação | revisar exclusões e taxonomia de cabimento |
| Divórcio litigioso | corrigir Tema 1.236 e refinar alimentos |
| Reclamação trabalhista | informar RE pendente do IRR 84; separar culpa concorrente; delimitar Tema 932 |
| Guias | sem erro autônomo relevante |
| Guia indenização × superendividamento | documentar pesquisa negativa e qualificar cenários seletivos |
| Doutrina | corrigir proveniência de links e operacionalizar critérios |
| Jurisprudência | completar temas/status e sincronizar |
| Legislação | separar legislação de soft law e sincronizar Markdown/HTML |
| Fontes | ampliar rastreabilidade pública |
| Modelos | advertências adequadas; reforçar atualização junto do modelo |
| Mapa do Site | incluir quatro modelos |
| Fale Conosco | corrigir estado textual e implantar transparência LGPD |
| Mensagem recebida | funcional; abranger em política de privacidade e retenção |

## 8. Ordem de correção recomendada

1. Fale Conosco + LGPD.
2. Exclusões do superendividamento.
3. Tema 1.236.
4. IRR 84 e culpa concorrente.
5. Sincronização Markdown/HTML e índice jurisprudencial.
6. Links bibliográficos.
7. Mapa do Site.
8. Rastreabilidade e pesquisa negativa.

## 9. Conclusão

A auditoria anterior foi suficiente para estrutura, navegação e aplicação do protocolo doutrinário, mas permissiva quanto à semântica jurídica fina e à coerência entre fontes da verdade.

O principal risco atual não é uma tese frontalmente absurda. É a compressão de condições importantes, omissão de status recursal, páginas transversais menos completas que os dossiês e divergência entre Markdown, HTML e estado operacional.

O Site deve ser considerado **juridicamente promissor, porém ainda não adversarialmente fechado**.

Regra recomendada para a próxima revisão: nenhuma tese relevante deve ser publicada sem responder qual é a fonte, o recorte da tese, suas condições, exceções, estado processual e data da verificação.
