# Fase 03 — Matriz de achados jurídicos adversariais por ação e guia

**Estratégia:** EA-000003-000019 — Nova Auditoria do Advogado do Diabo do Site Ações Judiciais  
**Data de corte:** 21/09/2026  
**Natureza:** auditoria adversarial. Este documento registra fragilidades e hipóteses de risco; não aplica correções ao corpus público.

## Critério

Cada formulação foi atacada por pelo menos um destes vetores: regra excessivamente categórica; exceção omitida; autoridade insuficiente; superveniência; confusão entre regra material e efeito processual; risco de interpretação prática indevida; lacuna probatória ou de competência.

Classificações:
- **ALTA:** pode causar erro de foro, pedido, tutela, prova ou conclusão material relevante;
- **MÉDIA:** não invalida o núcleo do texto, mas pode induzir leitura excessiva ou reduzir segurança profissional;
- **BAIXA:** melhoria de precisão, peso de precedente ou rastreabilidade.

A confirmação definitiva de cada achado material pertence à Fase 04.

## A. Ação de Repactuação de Dívidas por Superendividamento

### AJ19-JUR-001 — Competência quando o polo passivo é exclusivamente federal
**Prioridade preliminar:** ALTA  
**Trecho atacado:** a página afirma que, se o polo passivo for formado exclusivamente por instituição financeira federal, a competência é da Justiça Federal.

**Problema adversarial:** a formulação transforma em regra positiva geral uma fronteira que não está expressa na tese atual da Edição 282 de Jurisprudência em Teses do STJ. A tese oficial confirma a Justiça Estadual no processo de repactuação, inclusive com ente federal, por enquadramento na exceção do art. 109, I, da Constituição relativa a concurso de credores. O mesmo conjunto jurisprudencial preserva a Justiça Federal para ação autônoma de cobrança promovida por empresa pública federal. Não foi localizada, na verificação inicial, tese superior atual que autorize converter automaticamente a hipótese de "credor único federal" em regra federal para todo pedido estruturado sob o art. 104-A do CDC.

**Risco:** indicação incorreta de foro e replicação do erro no modelo de petição.

**Estado:** CONFIRMAR_NA_FASE_04. Até lá, a regra pública deve ser tratada como juridicamente mais categórica que a fonte superior identificada.

### AJ19-JUR-002 — Separação de fato sob o mesmo teto
**Prioridade preliminar:** MÉDIA  
**Trecho atacado:** "A permanência no mesmo imóvel não torna impossível a separação de fato".

**Problema adversarial:** a jurisprudência superior confirma que a separação de fato pode encerrar a eficácia patrimonial prospectiva do regime de bens, mas a frase sobre coabitação exige base fática e probatória própria. Na cadeia de fontes já auditada não foi localizado precedente superior específico que a eleve a regra geral.

**Risco:** o leitor confundir uma possibilidade probatória dependente dos fatos com orientação jurisprudencial consolidada.

**Estado:** FRAGILIDADE_DE_FUNDAMENTACAO; verificar fontes específicas na Fase 04.

### AJ19-JUR-003 — Patrimônio e ausência de venda prévia de bens
**Prioridade preliminar:** MÉDIA  
**Trecho atacado:** o CDC não estabelece, como requisito geral, a venda prévia de todos os bens.

**Diagnóstico adversarial:** a afirmação negativa é compatível, em leitura inicial, com a estrutura legal do superendividamento. O risco está no efeito pragmático: sem reforçar a diferença entre "não existir condição legal geral de liquidação" e "ativos líquidos poderem enfraquecer a impossibilidade manifesta de pagamento", o leitor pode inferir que patrimônio é secundário para o cabimento.

**Fator mitigador:** o próprio dossiê já declara que patrimônio, valor líquido e liquidez devem ser informados.

**Estado:** FRAGILIDADE_DE_ENFASE, não erro material confirmado.

### AJ19-JUR-004 — Veículo com alienação fiduciária
**Prioridade preliminar:** BAIXA/MÉDIA  
**Trecho atacado:** jurisprudência estadual consultada exclui da repactuação o crédito garantido por alienação fiduciária.

**Diagnóstico adversarial:** a página acerta ao não atribuir ao STJ uma tese repetitiva inexistente e ao qualificar a origem estadual da conclusão. O ponto fraco é a força persuasiva: sem identificar no texto público a origem e o alcance territorial da jurisprudência usada, o leitor pode projetá-la nacionalmente.

**Estado:** PROBLEMA_DE_FORCA_DA_FONTE; núcleo jurídico não refutado.

## B. Guia — Indenização trabalhista e superendividamento

### AJ19-JUR-005 — Capital superveniente após homologação
**Prioridade preliminar:** BAIXA/MÉDIA  
**Trecho atacado:** não existe regra geral de aceleração automática porque surgiu novo patrimônio.

**Diagnóstico adversarial:** a formulação é prudente e não afirma imunidade patrimonial. Contudo, não foi localizado precedente superior específico sobre indenização trabalhista superveniente em plano de superendividamento. A conclusão é inferencial: depende do título homologado, cláusulas de revisão, boa-fé, dever de informação e fase processual.

**Estado:** HIPOTESE_JURIDICA_PRUDENTE_SEM_PRECEDENTE_ESPECIFICO.

### AJ19-JUR-006 — Quitação/amortização seletiva como cenário analítico
**Prioridade preliminar:** MÉDIA  
**Trecho atacado:** o guia admite, como cenários analíticos, quitação ou amortização seletiva.

**Problema adversarial:** mesmo com a ressalva de que não são recomendações automáticas, a seleção de credores pode repercutir na coerência do plano global, na boa-fé processual e no tratamento econômico apresentado ao juízo e aos demais credores.

**Risco:** uso do quadro como autorização prática sem análise do efeito sobre o concurso global e a sustentabilidade.

**Estado:** FRAGILIDADE_DE_ALERTA; exigir, na futura correção, cautela ainda mais explícita, se confirmada na Fase 04.

### AJ19-JUR-007 — Pesquisa negativa de precedente específico
**Prioridade preliminar:** BAIXA  
**Diagnóstico:** a página corretamente qualifica a busca como "pesquisa negativa datada", não como prova de inexistência absoluta. O controle metodológico é adequado.

**Estado:** FALSO_POSITIVO_DESCARTADO nesta fase.

## C. Ação de Divórcio Litigioso c/c Partilha, Guarda, Convivência e Alimentos

### AJ19-JUR-008 — Leis nº 15.411/2026 e 15.412/2026 citadas, mas não integradas
**Prioridade preliminar:** ALTA  
**Trecho atacado:** as duas leis aparecem na lista de fontes, porém seus efeitos não são desenvolvidos no corpo do dossiê.

**Problema adversarial:** a Lei nº 15.411/2026 ampliou a disciplina do afastamento imediato do agressor no art. 12-C da Lei Maria da Penha para risco atual ou iminente também à integridade sexual, psicológica, moral ou patrimonial. A Lei nº 15.412/2026 atribuiu natureza executiva judicial às medidas protetivas de natureza civil do art. 22 e tratou expressamente, entre elas, de alimentos provisionais/provisórios, sem necessidade de ação principal para sua eficácia.

**Risco:** justamente a página que orienta triagem de violência, urgência familiar e alimentos deixa de explicar superveniências de 2026 diretamente úteis à estratégia processual.

**Estado:** OMISSAO_MATERIAL_CONFIRMAR_NA_FASE_04.

### AJ19-JUR-009 — Procedimento obrigatório do art. 699-A do CPC
**Prioridade preliminar:** MÉDIA/ALTA  
**Trecho atacado:** a página diz que a Lei nº 14.713/2023 exige atenção ao risco de violência antes da mediação ou conciliação, mas não explicita o mecanismo legal.

**Problema adversarial:** o art. 699-A do CPC impõe ao juiz, antes do início da audiência de mediação/conciliação nas ações de guarda, indagar as partes e o Ministério Público sobre risco de violência doméstica/familiar, abrindo prazo de cinco dias para apresentação de prova ou indícios.

**Risco:** perda de uma providência procedimental concreta em um dossiê destinado também ao uso prático.

**Estado:** OMISSAO_PROCESSUAL_PRELIMINAR; confirmação formal na Fase 04.

### AJ19-JUR-010 — Julgamento parcial do divórcio
**Prioridade preliminar:** BAIXA  
**Trecho atacado:** o STJ admitiu decretação do divórcio por julgamento parcial do mérito em ação cumulada.

**Diagnóstico adversarial:** a afirmação corresponde ao REsp 2.189.143/SP, mas é importante preservar o peso correto da fonte: precedente de Turma, não tese repetitiva ou súmula. O modelo já usa "avaliar", e não ordena aplicação automática.

**Estado:** FALSO_POSITIVO_MATERIAL_DESCARTADO; resta apenas cuidado de hierarquia jurisprudencial.

### AJ19-JUR-011 — FGTS e remuneração variável em alimentos
**Prioridade preliminar:** BAIXA  
**Diagnóstico:** a verificação inicial confirma a orientação de 2026 descrita no dossiê: FGTS formado no período conjugal, sob comunhão parcial, é comunicável; horas extras integram a base de alimentos percentuais sobre rendimentos líquidos pela natureza remuneratória, enquanto PLR não entra automaticamente e exige demonstração concreta de necessidade.

**Estado:** FALSO_POSITIVO_DESCARTADO; manter controle de aderência ao caso concreto.

## D. Reclamação Trabalhista com pedido de Indenização por Danos Morais

### AJ19-JUR-012 — Tema 215 do TST: mérito atual versus fonte canônica desatualizada
**Prioridade preliminar:** MÉDIA  
**Trecho atacado:** o dossiê afirma que o Tema 215 foi julgado em 19/08/2026 e deixou de estar apenas afetado.

**Diagnóstico adversarial:** publicações oficiais de Tribunais Regionais do Trabalho divulgam o julgamento do TST e a tese de flexibilização excepcional da competência territorial para o domicílio do trabalhador em situações concretamente justificadas. Ao mesmo tempo, documento temático do TST recuperado na auditoria ainda aparece com status anterior de "afetado". Portanto, o conteúdo material do dossiê é plausivelmente atual, mas sua cadeia de rastreabilidade precisa impedir que uma ficha antiga do TST seja usada como prova do status novo.

**Estado:** PROBLEMA_DE_SUPERVENIENCIA_E_RASTREABILIDADE, não erro material confirmado.

### AJ19-JUR-013 — Tema 183 do TST
**Prioridade preliminar:** BAIXA  
**Diagnóstico:** a tese descrita está compatível com o precedente qualificado: o termo inicial da prescrição em acidente/doença ocupacional é a ciência inequívoca da consolidação da lesão em toda sua extensão. O tema já transitou em julgado, dado útil que a página não explicita.

**Estado:** PRECISAO_DE_STATUS, sem erro de tese.

### AJ19-JUR-014 — Responsabilidade objetiva em assaltos na atividade bancária
**Prioridade preliminar:** BAIXA  
**Diagnóstico:** o ataque não confirmou generalização indevida. O texto condiciona a responsabilidade ao risco especial, distingue comércio em geral e ancora a análise no Tema 932 do STF. A jurisprudência trabalhista reconhece risco diferenciado em atividade bancária em casos de assalto.

**Estado:** FALSO_POSITIVO_DESCARTADO.

### AJ19-JUR-015 — IRR 84 e atraso de verbas rescisórias
**Prioridade preliminar:** BAIXA  
**Diagnóstico:** o estado "RE Pendente" do IRR 84 e a orientação do IRR 143 de que atraso/inadimplemento de verbas rescisórias, isoladamente, não gera dano moral automático foram confirmados na verificação inicial.

**Estado:** FALSO_POSITIVO_DESCARTADO.

### AJ19-JUR-016 — Tarifação do art. 223-G
**Prioridade preliminar:** BAIXA  
**Diagnóstico:** a leitura de que as faixas do § 1º funcionam como parâmetros orientativos e não como teto absoluto está alinhada às ADIs 6.050, 6.069 e 6.082 do STF.

**Estado:** FALSO_POSITIVO_DESCARTADO.

## E. Achado herdado da Fase 02

### P-01 — Rastreabilidade normativa do HTML trabalhista
**Prioridade:** MÉDIA  
A versão HTML condensa a lista normativa e omite legislação especial que o Markdown canônico considera relevante (entre outras, Lei nº 9.029/1995, Lei nº 14.457/2022, Lei nº 14.611/2023, Lei nº 8.213/1991 e LGPD). Não altera a tese central, mas reduz verificabilidade pública.

**Estado:** CONFIRMADO na Fase 02; deve ser cruzado novamente nas Fases 04 e 06.

## Gate da Fase 03

A matriz jurídica por página foi produzida. Os achados de maior criticidade preliminar são:

1. competência no superendividamento — risco de regra federal excessivamente categórica;
2. superveniências de 2026 em violência doméstica/alimentos no dossiê de família — fontes citadas sem incorporação material;
3. art. 699-A do CPC — procedimento concreto subexplicado;
4. Tema 215 do TST — necessidade de controlar divergência entre julgamento superveniente e ficha temática desatualizada;
5. quitação/amortização seletiva de credores no guia de indenização — alerta prático pode ser insuficiente.

Nenhuma página pública foi alterada nesta fase.
