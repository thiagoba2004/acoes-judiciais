# Fase 06 — Contradições transversais e priorização

**Estratégia:** EA-000003-000019 — Nova Auditoria do Advogado do Diabo do Site Ações Judiciais  
**Data de corte:** 21/09/2026  
**Escopo:** cruzamento dos achados editoriais, jurídicos, jurisprudenciais, doutrinários e de fontes, sem correção pública.

## Critério de prioridade

- **ALTA:** risco concreto de omissão de instrumento jurídico relevante, erro de estratégia processual ou orientação material insuficiente em tema sensível.
- **MÉDIA:** pode reduzir segurança, rastreabilidade ou precisão e induzir aplicação excessiva, embora o núcleo jurídico principal permaneça utilizável.
- **BAIXA:** problema de atribuição, hierarquia, status ou força persuasiva que merece saneamento, mas dificilmente altera sozinho o resultado jurídico.

## Achados consolidados — sem duplicidade

### A-01 — Dossiê de família cita Leis 15.411/2026 e 15.412/2026, mas omite seus efeitos operacionais
**Prioridade:** ALTA  
**Página principal:** `acoes/divorcio-litigioso-partilha-guarda-convivencia-alimentos.*`

O texto lista as duas leis entre as fontes centrais, mas não incorpora no corpo:
- a ampliação do art. 12-C da Lei Maria da Penha para risco atual ou iminente à integridade sexual, psicológica, moral e patrimonial, além de vida/integridade física;
- a natureza de título executivo judicial das medidas protetivas cíveis, inclusive alimentos provisionais/provisórios, com dispensa de ação principal.

**Contradição transversal:** a página afirma revisão em 21/09/2026 e enumera as normas novas, mas a orientação prática continua estruturada como se seus efeitos processuais não existissem.

**Impacto:** urgências protetivas, moradia, afastamento do agressor, alimentos e desenho da estratégia processual.

### A-02 — Art. 699-A do CPC é mencionado apenas em nível genérico
**Prioridade:** MÉDIA/ALTA  
**Página principal:** dossiê de família.

O texto informa que deve haver atenção ao risco de violência antes de mediação/conciliação, mas omite o procedimento normativo concreto: indagação às partes e ao Ministério Público e prazo de cinco dias para apresentação de prova ou indícios.

**Impacto:** perda de providência processual objetiva num dossiê que pretende ser teórico-prático.

### A-03 — HTML trabalhista possui rastreabilidade normativa inferior ao Markdown canônico
**Prioridade:** MÉDIA  
**Páginas:** `acoes/reclamacao-trabalhista-danos-morais.md` × `.html`.

O HTML conserva a tese jurídica principal, mas sua malha de fontes não reproduz integralmente legislação especial expressamente identificada no Markdown, incluindo Lei 9.029/1995, Lei 14.457/2022, Lei 14.611/2023, Lei 8.213/1991 e LGPD.

**Contradição transversal:** a política do Projeto exige sincronização semântica e rastreabilidade, mas a versão pública é menos verificável que a fonte canônica.

### A-04 — Tema 215 do TST: texto público atualizado, registro de fonte ficou superado
**Prioridade:** MÉDIA  
**Página:** dossiê trabalhista / `SOURCE_REGISTRY.jsonl`.

O texto público já descreve o julgamento de agosto/2026. Um registro interno anterior ainda refletia o estado de tema afetado. A Fase 04 corrigiu a classificação do registro interno e adicionou fonte oficial superveniente, sem alterar a página pública.

**Impacto residual:** mostra risco de divergência temporal entre texto público e ficha-fonte; requer procedimento mais forte de atualização de status processual.

### A-05 — Guia sobre indenização e superendividamento pode ser lido como permissivo demais na quitação seletiva
**Prioridade:** MÉDIA  
**Página:** `guias/indenizacao-trabalhista-superendividamento.*`.

O guia qualifica quitação/amortização seletiva como cenários analíticos e contém ressalvas. Ainda assim, como o procedimento de superendividamento tem lógica global, o quadro pode ser lido pragmaticamente como autorização antecipada. A futura redação deve destacar ainda mais que qualquer seleção pode alterar plano, boa-fé, tratamento econômico e sustentabilidade perante os demais credores.

**Natureza:** fragilidade de segurança prática; não foi confirmada proibição abstrata nacional de todo pagamento seletivo.

### A-06 — BRASILCON e Idec não estão explicitamente rotulados como posições institucionais interessadas
**Prioridade:** MÉDIA  
**Páginas:** Superendividamento / Doutrina / registros de fontes.

O próprio protocolo metodológico cria categoria para posições de atores interessados, inclusive entidades de consumidores. BRASILCON e Idec são corretamente atribuídos e não vinculantes, mas a classificação pública/registral não explicita suficientemente sua posição de advocacy em defesa do consumidor.

**Contradição transversal:** protocolo interno mais rigoroso do que sua implementação.

### A-07 — Enunciados da 2ª Jornada são aproximados em excesso de posição institucional da ANAMATRA
**Prioridade:** MÉDIA  
**Páginas:** Doutrina e dossiê trabalhista; registro de fonte.

A própria ANAMATRA informa que a Jornada foi promovida em parceria e reuniu múltiplas categorias profissionais. Documento posterior distingue enunciados da Jornada de teses que, após reapreciação em CONAMAT/Assembleia, passaram a externar posições oficiais da associação.

**Correção futura indicada:** classificar como produção/enunciados de jornada multi-institucional promovida pela ANAMATRA, salvo comprovação de ratificação específica.

### A-08 — IBDFAM Enunciado 18 é rotulado como convergente com STJ de modo excessivamente amplo
**Prioridade:** MÉDIA  
**Página:** dossiê de família.

O IBDFAM sustenta que o julgamento parcial do mérito para encerrar a conjugalidade deve ser a regra. O STJ confirmou a admissibilidade da técnica no REsp 2.189.143/SP, mas não fixou tese geral de que ela seja universalmente a regra.

**Correção futura indicada:** `CONVERGENTE_EM_PARTE` — convergência quanto à admissibilidade, não quanto à universalização.

### A-09 — Nota técnica atribuída à ABRAT possui coautoria institucional omitida
**Prioridade:** BAIXA/MÉDIA  
**Páginas:** Doutrina / dossiê trabalhista / registro de fonte.

O documento de 2017 está hospedado pela ABRAT, mas foi assinado conjuntamente por ANPT, ANAMATRA, ABRAT, SINAIT, ALAL, ALJT e JUTRA.

**Correção futura indicada:** “nota técnica conjunta, hospedada pela ABRAT, com a ABRAT entre as signatárias”.

### A-10 — Alienação fiduciária de veículo: força nacional da fonte deve continuar limitada
**Prioridade:** BAIXA  
**Página:** Superendividamento.

A página utiliza precedente do TJSP para tratar crédito de veículo alienado fiduciariamente como crédito garantido excluído do art. 104-A, §1º, e já informa que não identificou tese repetitiva específica do STJ. Não há erro confirmado; o achado consiste em preservar essa limitação territorial/persuasiva em qualquer futura edição.

## Falsos positivos relevantes descartados

1. **Competência federal exclusiva no superendividamento:** correta segundo a Tese 10 da Edição 282 do STJ.
2. **Separação de fato sob o mesmo teto:** juridicamente possível em precedente do STJ, desde que comprovada a cessação da vida conjugal.
3. **Mínimo existencial/consignado:** o dossiê está atualizado ao julgamento do STF de 23/04/2026.
4. **Julgamento parcial do divórcio:** admissibilidade confirmada pelo STJ; apenas a leitura do Enunciado 18 do IBDFAM precisa de qualificação.
5. **FGTS em comunhão parcial:** orientação de 2026 do STJ corretamente retratada.
6. **Horas extras e PLR na base alimentar:** distinção atual do STJ corretamente retratada.
7. **Assalto e atividade de risco:** o texto trabalhista não universaliza responsabilidade objetiva e preserva o teste do risco especial.
8. **IRR 84 e IRR 143:** núcleo das teses corretamente descrito.
9. **Art. 223-G/CLT:** leitura das faixas como orientativas, e não teto absoluto, está alinhada ao STF.
10. **ADFAS pós-EC 66:** o Site corretamente marca a antiga tese como superada pelo Tema 1053.

## Páginas sem achado material autônomo

Na auditoria transversal, índices, Início, Mapa do Site, Fontes, Legislação, Modelos, Fale Conosco, Privacidade e páginas meramente estruturais não geraram achado jurídico autônomo além dos problemas herdados das páginas materiais a que remetem. A página `recebido.html` é funcional e não possui par Markdown por desenho.

## Ordem recomendada de saneamento posterior

1. Família: integrar Leis 15.411/2026, 15.412/2026 e art. 699-A.
2. Trabalho: restaurar paridade normativa HTML/Markdown e formalizar rotina de atualização de temas qualificados.
3. Doutrina: corrigir categorias e autoria institucional (BRASILCON/Idec, Jornada/ANAMATRA, ABRAT conjunta, IBDFAM Enunciado 18).
4. Guia indenização × superendividamento: reforçar alerta sobre quitação/amortização seletiva.
5. Reauditoria final de paridade e fontes.

## Gate da Fase 06

Achados cruzados, deduplicados e classificados por criticidade. Foram consolidados 10 achados finais: 1 ALTA, 1 MÉDIA/ALTA, 6 MÉDIOS ou MÉDIA/BAIXA e 2 de baixa criticidade/controle de força da fonte. Os falsos positivos relevantes foram preservados separadamente. Gate satisfeito.
