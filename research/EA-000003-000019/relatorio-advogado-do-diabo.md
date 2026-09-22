# Relatório do Advogado do Diabo — Site Ações Judiciais

**Estratégia:** EA-000003-000019 — Nova Auditoria do Advogado do Diabo do Site Ações Judiciais  
**Data de corte:** 21/09/2026  
**Escopo:** todo o corpus público atual do Site Ações Judiciais.  
**Regra de execução:** auditoria sem correção silenciosa das páginas públicas.

## 1. Conclusão executiva

A auditoria adversarial integral encontrou um Site estruturalmente consistente e juridicamente mais cuidadoso do que uma leitura hostil inicial sugeria, mas identificou lacunas reais que precisam ser corrigidas em etapa própria.

O inventário fechou em **16 páginas HTML públicas**, com **15 pares Markdown canônicos**; `fale-conosco/recebido.html` é página funcional sem par Markdown. A reauditoria técnica registrou **458 referências href**, **69 verificações de âncoras**, **4 botões reais COPIAR MODELO**, **zero links internos quebrados**, **zero âncoras quebradas** e **zero vazamentos de governança interna**.

Depois de atacar as teses jurídicas, conferir legislação e precedentes atuais e auditar doutrina/atribuição institucional, foram consolidados **10 achados finais**:
- 1 de prioridade **ALTA**;
- 1 de prioridade **MÉDIA/ALTA**;
- 6 de prioridade **MÉDIA**;
- 1 de prioridade **BAIXA/MÉDIA**;
- 1 de prioridade **BAIXA**.

O problema mais importante está no dossiê de Direito das Famílias: ele cita as Leis nº 15.411/2026 e nº 15.412/2026 como fontes, mas não incorpora no corpo suas consequências práticas para violência doméstica, afastamento do agressor, medidas protetivas cíveis e alimentos. O segundo problema mais relevante é a subexplicação do art. 699-A do CPC.

Em contrapartida, várias suspeitas fortes foram **refutadas** pela conferência oficial. Entre elas: a regra de competência federal quando a repactuação possui polo passivo exclusivamente federal, a possibilidade de separação de fato sob o mesmo teto, a atualização do mínimo existencial após o STF, a comunicabilidade do FGTS, a distinção entre horas extras e PLR nos alimentos e o núcleo dos precedentes trabalhistas testados.

## 2. Metodologia

A auditoria foi realizada em sete fases:
1. inventário integral e delimitação do corpus;
2. paridade Markdown/HTML e integridade editorial;
3. auditoria jurídica adversarial por ação e guia;
4. verificação normativa, jurisprudencial e de superveniência;
5. doutrina, posições institucionais e contraditório;
6. contradições transversais e priorização;
7. relatório final e fechamento.

Cada afirmação sensível foi submetida, conforme o caso, a pelo menos um dos seguintes testes:
- regra excessivamente categórica;
- exceção omitida;
- fonte hierarquicamente insuficiente;
- precedente superado ou estado processual desatualizado;
- confusão entre regra material e consequência processual;
- generalização a partir de precedente local;
- omissão de requisito probatório;
- incompatibilidade entre Markdown e HTML;
- atribuição indevida de posição institucional;
- ausência de contraditório doutrinário;
- divergência entre protocolo interno e execução pública.

## 3. Achados finais priorizados

### A-01 — Leis nº 15.411/2026 e nº 15.412/2026 citadas, mas não incorporadas
**Prioridade: ALTA**  
**Página:** Ação de Divórcio Litigioso c/c Partilha de Bens, Guarda, Convivência e Alimentos.

O dossiê lista ambas as leis entre as fontes centrais, mas não explica no corpo que:
- a Lei nº 15.411/2026 ampliou o art. 12-C da Lei Maria da Penha para risco atual ou iminente também à integridade sexual, psicológica, moral ou patrimonial;
- a Lei nº 15.412/2026 atribuiu natureza de título executivo judicial às medidas protetivas cíveis do art. 22, inclusive alimentos provisionais/provisórios, dispensando ação principal para sua eficácia.

**Risco:** uma consulta prática pode deixar de enxergar instrumentos processuais novos justamente em situações de urgência, violência, moradia e alimentos.

**Recomendação corretiva:** criar seção específica sobre violência doméstica, urgências protetivas e efeitos das Leis nº 15.411/2026 e nº 15.412/2026, integrando-a também ao modelo de petição e à triagem.

### A-02 — Art. 699-A do CPC subexplicado
**Prioridade: MÉDIA/ALTA**  
**Página:** dossiê de família.

O Site menciona que a Lei nº 14.713/2023 exige atenção ao risco de violência antes da mediação/conciliação, mas não registra o mecanismo concreto: nas ações de guarda, antes da audiência, o juiz deve indagar partes e Ministério Público sobre risco de violência doméstica/familiar e abrir prazo de cinco dias para apresentação de prova ou indícios.

**Risco:** perda de providência processual objetiva e de prazo importante.

**Recomendação corretiva:** incorporar o procedimento do art. 699-A ao corpo, ao roteiro de triagem e ao modelo.

### A-03 — Paridade normativa inferior no HTML trabalhista
**Prioridade: MÉDIA**  
**Página:** Reclamação Trabalhista com pedido de Indenização por Danos Morais.

O Markdown canônico identifica legislação especial relevante — entre outras, Lei nº 9.029/1995, Lei nº 14.457/2022, Lei nº 14.611/2023, Lei nº 8.213/1991 e LGPD — que não aparece com a mesma completude na malha pública de fontes do HTML.

**Risco:** redução da verificabilidade pública e quebra da política de sincronização semântica.

**Recomendação corretiva:** restaurar a malha normativa no HTML e incluir teste de paridade de fontes normativas no processo de publicação.

### A-04 — Tema 215 do TST: divergência temporal entre texto e registro de fonte
**Prioridade: MÉDIA**  
**Página:** dossiê trabalhista / governança de fontes.

O texto público já estava atualizado ao julgamento de agosto de 2026. Um registro interno anterior ainda refletia o estado de tema afetado. Durante a própria auditoria, esse registro interno foi reclassificado como fonte superada por superveniência e foi adicionada fonte oficial atualizada. Nenhuma página pública foi alterada.

**Risco:** uma futura revisão automatizada poderia usar ficha antiga e regredir o conteúdo.

**Recomendação corretiva:** instituir controle explícito de data de corte e de substituição de status para temas repetitivos, IRRs e repercussão geral.

### A-05 — Quitação/amortização seletiva no guia de indenização pode induzir leitura permissiva
**Prioridade: MÉDIA**  
**Página:** Indenização trabalhista e superendividamento.

O guia corretamente diz que quitação e amortização seletivas são apenas cenários analíticos. Mesmo assim, a apresentação pode ser lida como autorização prática antes de avaliar efeitos sobre a lógica global do plano, boa-fé, tratamento econômico dos credores e sustentabilidade posterior.

**Risco:** aplicação mecânica de um exemplo analítico.

**Recomendação corretiva:** acrescentar alerta de que pagamento seletivo não é estratégia presumidamente lícita ou ótima no processo de repactuação e exige análise do plano global, fase processual e efeitos perante os demais credores.

### A-06 — BRASILCON e Idec: natureza de posição interessada pouco explícita
**Prioridade: MÉDIA**  
**Páginas:** Superendividamento e Doutrina.

As posições estão atribuídas, datadas e tratadas como não vinculantes. Porém, o próprio Protocolo de Pesquisa Doutrinária prevê categoria específica para atores interessados, inclusive entidades de consumidores. BRASILCON e Idec defendem institucionalmente o polo consumidor e deveriam ser rotulados de forma transparente como posições institucionais interessadas.

**Risco:** aproximação indevida entre advocacy institucional e doutrina neutra.

**Recomendação corretiva:** manter as fontes, mas alterar a categoria e explicitar o lugar institucional de fala.

### A-07 — Enunciados da 2ª Jornada aproximados em excesso de posição oficial da ANAMATRA
**Prioridade: MÉDIA**  
**Páginas:** Doutrina e dossiê trabalhista.

A página trabalhista é relativamente cautelosa ao atribuir as teses à 2ª Jornada. Já a camada doutrinária e o registro de fontes permitem leitura de que seriam posições institucionais próprias da ANAMATRA. Fontes da própria entidade mostram que a Jornada foi promovida em parceria e reuniu múltiplas categorias; documento posterior distingue enunciados do evento de teses que, após reapreciação em CONAMAT/Assembleia, passaram a externar posições oficiais da associação.

**Risco:** sobreatribuição institucional.

**Recomendação corretiva:** classificar os enunciados como produção de jornada multi-institucional promovida pela ANAMATRA, salvo prova de ratificação específica.

### A-08 — IBDFAM Enunciado 18: convergência com STJ é parcial, não integral
**Prioridade: MÉDIA**  
**Página:** dossiê de família.

O IBDFAM sustenta que o julgamento parcial do mérito para decretar o fim da conjugalidade deve ser a regra. O REsp 2.189.143/SP confirmou a admissibilidade da técnica, inclusive para decretação liminar do divórcio, mas não estabeleceu tese geral de que ela seja universalmente a regra.

**Risco:** atribuir ao STJ a força normativa de uma formulação institucional mais ampla.

**Recomendação corretiva:** substituir a classificação por CONVERGENTE_EM_PARTE, esclarecendo convergência quanto à admissibilidade, não quanto à universalização.

### A-09 — “Nota Técnica da ABRAT” tem coautoria institucional
**Prioridade: BAIXA/MÉDIA**  
**Páginas:** Doutrina e dossiê trabalhista.

O documento de 2017 está hospedado pela ABRAT e a entidade o assinou, mas a nota é conjunta: ANPT, ANAMATRA, ABRAT, SINAIT, ALAL, ALJT e JUTRA.

**Risco:** perda de precisão de autoria institucional.

**Recomendação corretiva:** identificar o documento como nota técnica conjunta hospedada pela ABRAT.

### A-10 — Alienação fiduciária de veículo: preservar limite da fonte estadual
**Prioridade: BAIXA**  
**Página:** Superendividamento.

O Site utiliza precedente do TJSP para a exclusão do crédito garantido por alienação fiduciária de bem móvel e já informa que não foi identificada tese repetitiva específica do STJ.

**Risco:** baixo, desde que a origem estadual e o caráter não vinculante continuem explícitos.

**Recomendação corretiva:** não elevar esse precedente a regra nacional vinculante em futuras revisões.

## 4. Falsos positivos descartados

A auditoria registrou e depois descartou suspeitas que não resistiram ao confronto com fontes oficiais. Essa seção é parte essencial do método: um relatório adversarial não deve transformar hipótese de erro em erro confirmado.

### 4.1. Competência no superendividamento
A formulação do Site segundo a qual a Justiça Federal é competente quando o polo passivo é composto exclusivamente por instituição financeira federal foi confirmada pela Tese 10 da Edição 282 de Jurisprudência em Teses do STJ.

### 4.2. Separação de fato sob o mesmo teto
O STJ já reconheceu que a permanência na mesma residência não impede, por si só, a separação de fato. A prova deve demonstrar cessação efetiva da vida conjugal. O Site já exige explicação e prova mais robustas.

### 4.3. Mínimo existencial e consignado
O tratamento do julgamento do STF de 23/04/2026 está atualizado: parâmetro quantitativo por decreto foi preservado com exigência de reavaliação técnica periódica, e a exclusão do consignado da aferição do mínimo existencial foi afastada.

### 4.4. Divórcio por julgamento parcial do mérito
A possibilidade está confirmada pelo REsp 2.189.143/SP. O problema não é a admissibilidade da técnica, mas apenas a classificação excessivamente ampla da convergência com o Enunciado 18 do IBDFAM.

### 4.5. FGTS, horas extras e PLR
As formulações atuais do dossiê de família coincidem com a jurisprudência de 2026 consultada: FGTS formado no período conjugal em comunhão parcial é comunicável; horas extras integram a base de alimentos percentuais sobre rendimentos líquidos; PLR não entra automaticamente e exige análise concreta de necessidade.

### 4.6. Danos morais trabalhistas
Não se confirmou generalização indevida da responsabilidade objetiva por assalto. O texto preserva o teste de risco especial. Também passaram no confronto o núcleo do IRR 84, IRR 143 e a leitura do art. 223-G após as ADIs 6.050, 6.069 e 6.082.

### 4.7. ADFAS e separação judicial
O Site corretamente conserva a antiga tese institucional da ADFAS como posição histórica e a marca como superada pelo Tema 1053 do STF.

## 5. Pontos fortes confirmados

1. O Site costuma separar norma, jurisprudência vinculante/qualificada, precedente persuasivo e doutrina.
2. A linguagem dos modelos é predominantemente condicional e evita vendê-los como petições prontas.
3. O dossiê de superendividamento distingue renda, patrimônio, liquidez, dívida elegível e dívida excluída.
4. A seção sobre renda do cônjuge evita tanto a soma automática quanto a irrelevância automática.
5. A pesquisa negativa sobre indenização trabalhista superveniente é corretamente apresentada como datada, e não como prova de inexistência absoluta de precedentes.
6. Produção acadêmica autoral não é atribuída artificialmente à universidade.
7. O artigo da OAB-MT é corretamente marcado como autoria individual em ambiente OAB.
8. Doutrina profissional de escritórios é apresentada como não vinculante e, no trabalhista, com indicação de perspectiva empresarial.
9. A tese histórica da ADFAS é confrontada com superveniência vinculante.
10. A infraestrutura pública passou nos testes de links, âncoras, navegação, botões de cópia e ausência de vazamento de governança.

## 6. Risco global do corpus

O relatório não atribui nota ou selo geral de “correto/incorreto”. O resultado é granular.

As páginas centrais são utilizáveis como material de estudo e triagem, mas **não devem permanecer sem a rodada corretiva**, especialmente no dossiê de família. A maior parte dos problemas encontrados não é de tese central falsa; é de omissão de superveniência operacional, rastreabilidade, força da fonte ou precisão de atribuição.

O risco mais sensível é o seguinte: uma página pode estar formalmente “atualizada” e até citar a lei nova, mas ainda assim não ter incorporado seus efeitos concretos. A-01 é exatamente esse caso.

## 7. Plano corretivo recomendado

Sem executar correções nesta estratégia, o relatório recomenda quatro frentes autônomas posteriores:

### Frente corretiva 1 — Direito das Famílias
- integrar Leis 15.411/2026 e 15.412/2026;
- incorporar art. 699-A do CPC, inclusive prazo de cinco dias;
- reclassificar IBDFAM Enunciado 18 como convergência parcial;
- revisar modelo, checklist e HTML/Markdown em conjunto.

### Frente corretiva 2 — Direito do Trabalho
- restaurar paridade normativa HTML/Markdown;
- revisar rotina de atualização de estado de temas qualificados;
- corrigir classificação da 2ª Jornada/ANAMATRA;
- corrigir autoria conjunta da nota técnica hospedada pela ABRAT.

### Frente corretiva 3 — Superendividamento e Doutrina
- rotular BRASILCON e Idec como posições institucionais interessadas;
- reforçar limites de força de precedentes estaduais;
- endurecer o alerta do guia sobre pagamentos seletivos.

### Frente corretiva 4 — Reauditoria pós-correção
- conferir paridade Markdown/HTML;
- repetir links/âncoras;
- verificar status jurisprudencial;
- testar que cada correção pública possui fonte recuperável;
- confirmar que nenhum novo automatismo foi introduzido.

## 8. Documentos produzidos na auditoria

- `research/EA-000003-000019/plano-de-fases.md`
- `research/EA-000003-000019/inventario-corpus-publico.md`
- `research/EA-000003-000019/paridade-integridade-editorial.md`
- `research/EA-000003-000019/matriz-achados-juridicos.md`
- `research/EA-000003-000019/verificacao-normativa-jurisprudencial-superveniencia.md`
- `research/EA-000003-000019/doutrina-posicoes-institucionais-contraditorio.md`
- `research/EA-000003-000019/contradicoes-transversais-priorizacao.md`
- `research/EA-000003-000019/relatorio-advogado-do-diabo.md`

## 9. Fontes oficiais de controle mais relevantes

- STJ — Jurisprudência em Teses, Edição 282: Superendividamento.
- STF — ADPFs 1005, 1006 e 1097.
- STF — Tema 1053.
- STF — Tema 1236.
- Lei nº 14.713/2023.
- Lei nº 15.411/2026.
- Lei nº 15.412/2026.
- STJ — REsp 2.189.143/SP.
- STJ — precedentes/informativos de 2026 sobre FGTS e base alimentar.
- TST — precedentes qualificados relativos a danos extrapatrimoniais e competência territorial.

## 10. Fechamento

A Estratégia EA-000003-000019 cumpre seu objetivo: o corpus público foi inventariado, atacado adversarialmente, confrontado com fontes atuais, auditado quanto a doutrina e autoria institucional, cruzado transversalmente e priorizado.

**Nenhuma correção do corpus público foi aplicada durante esta estratégia.** As únicas alterações realizadas durante a auditoria foram de governança e rastreabilidade internas necessárias para registrar o trabalho e atualizar a própria evidência de auditoria.

O próximo passo lógico é abrir estratégia(s) corretiva(s) específica(s) a partir deste relatório e, após as alterações, executar reauditoria independente.
