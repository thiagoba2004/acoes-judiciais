# Mapa processual, pedidos e alternativas — EA-000003-000001

**Projeto:** PRJ-000003 — Ações Judiciais  
**Estratégia:** EA-000003-000001 — Ação de Repactuação de Dívidas por Superendividamento  
**Fase:** 05/08 — Procedimento, pedidos e alternativas  
**Data:** 20/09/2026  
**Estado:** VERSÃO 1 — GATE DA FASE 05 SATISFEITO

## 1. Arquitetura legal

O procedimento deve ser lido como sistema de tratamento global, não como simples revisional contratual.

```text
DIAGNÓSTICO E TRIAGEM
↓
ESCOLHA DA PORTA DE ENTRADA
├─ Judicial — art. 104-A
├─ Administrativa/SNDC — art. 104-C
└─ Estrutura local de CEJUSC/Núcleo, conforme organização judiciária
↓
AUDIÊNCIA GLOBAL DE CONCILIAÇÃO
↓
ACORDO TOTAL OU PARCIAL
├─ SIM → homologação do plano consensual
└─ NÃO/PARCIAL → a pedido do consumidor, art. 104-B para credores remanescentes
↓
PLANO JUDICIAL COMPULSÓRIO, SE CABÍVEL
↓
EXECUÇÃO/ACOMPANHAMENTO DO PLANO
```

## 2. Fase consensual judicial — art. 104-A

### Entrada
O consumidor superendividado pessoa natural requer a instauração do processo de repactuação.

### Objetivo
Realizar audiência conciliatória global com os credores das dívidas abrangidas.

### Elemento central
O consumidor apresenta proposta de plano de pagamento:
- prazo máximo legal de cinco anos;
- preservação do mínimo existencial;
- observância das garantias e formas de pagamento originalmente pactuadas, nos termos legais;
- sem inclusão das dívidas excluídas pelo §1º.

### Credores ausentes
A consequência do art. 104-A, §2º depende dos pressupostos legais:
- ausência injustificada do credor ou procurador com poderes especiais e plenos para transigir;
- montante devido certo e conhecido pelo consumidor.

Não transformar a sanção legal em pedido automático quando esses pressupostos não estiverem presentes.

## 3. Acordo consensual

Havendo conciliação com um ou mais credores, a homologação judicial do acordo:
- descreve o plano;
- constitui título executivo;
- tem força de coisa julgada.

O plano consensual deve contemplar, conforme o caso:
- dilação de prazos;
- redução de encargos/remuneração ou outras medidas facilitadoras;
- referência a ações judiciais em curso;
- data para exclusão dos cadastros de inadimplentes;
- dever do consumidor de não agravar a situação de superendividamento.

## 4. Fase judicial compulsória — art. 104-B

### Gatilho
Falta de êxito na conciliação em relação a um ou mais credores.

### Condição processual importante
A instauração ocorre **a pedido do consumidor**.

### Objeto
- revisão e integração dos contratos;
- repactuação das dívidas remanescentes;
- plano judicial compulsório.

### Credores remanescentes
Devem ser citados. A lei prevê prazo de 15 dias para documentos e razões da recusa ao plano voluntário/renegociação.

### Administrador
O juiz pode nomear administrador, sem onerar as partes, para apresentar plano após diligências necessárias.

### Limites do plano compulsório
O plano:
- assegura no mínimo o principal devido, corrigido monetariamente por índice oficial;
- prevê liquidação total em até cinco anos, observada a sequência legal em relação a eventual plano consensual;
- primeira parcela em até 180 dias da homologação;
- saldo em parcelas mensais iguais e sucessivas.

## 5. Via administrativa — art. 104-C

Órgãos públicos do Sistema Nacional de Defesa do Consumidor podem, concorrente e facultativamente:
- promover a fase conciliatória/preventiva;
- realizar audiência global;
- facilitar elaboração de plano;
- atuar em reeducação financeira;
- formalizar acordos nos limites legais e regulamentares.

A existência da via administrativa não deve ser transformada em requisito universal de prévio exaurimento, salvo regra local/jurisprudência específica.

## 6. Arquitetura de pedidos — não é modelo pronto

### 6.1. Pedidos estruturais normalmente compatíveis com a fase 104-A
Conforme fatos, competência e documentos:
1. recebimento do pedido de repactuação;
2. reconhecimento do processamento sob o regime legal, se presentes os requisitos;
3. designação de audiência global;
4. convocação/citação/intimação dos credores conforme rito e prática local;
5. apreciação da proposta global apresentada;
6. aplicação das consequências legais ao credor ausente apenas se preenchidos os pressupostos;
7. homologação dos acordos eventualmente alcançados;
8. registro das medidas que integrarão o plano consensual.

### 6.2. Pedido condicional ligado ao art. 104-B
Se a conciliação não resolver integralmente:
- requerer, **condicionalmente e a pedido do consumidor**, a instauração da fase judicial para os credores remanescentes.

Evitar redigir o art. 104-B como se seu plano compulsório existisse automaticamente desde a petição inicial da fase conciliatória.

### 6.3. Pedidos de tutela provisória
Não integrar como cláusula-padrão automática.

Qualquer tutela para:
- limitar descontos;
- suspender cobrança;
- impedir negativação;
- suspender exigibilidade;
- alterar pagamentos antes da audiência;

deve possuir fundamento fático, jurídico e jurisprudencial próprio, com análise dos requisitos de tutela provisória e dos efeitos sistêmicos sobre todos os credores.

## 7. O que NÃO deve ser pedido mecanicamente

- “suspensão de todas as dívidas” como efeito automático da Lei 14.181/2021;
- exclusão imediata e incondicionada de todos os cadastros sem fundamento específico;
- redução arbitrária de principal na fase compulsória em contradição com o limite legal;
- inclusão de dívidas legalmente excluídas;
- tratamento privilegiado silencioso a um credor que comprometa a lógica global;
- declaração abstrata de boa-fé sem suporte factual;
- competência de Juizado/vara especializada sem verificação local.

## 8. Alternativas e portas de entrada

| Alternativa | Função | Limite |
|---|---|---|
| Negociação direta | solução bilateral rápida | pode não resolver o quadro global |
| Consumidor.gov.br | reclamação/negociação institucional | não substitui automaticamente audiência global do regime |
| Procon/SNDC — art. 104-C | prevenção e conciliação administrativa | verificar estrutura local |
| CEJUSC/Núcleo especializado | conciliação e, conforme organização local, integração ao fluxo processual | competência/fluxo variam por tribunal |
| Processo judicial 104-A | audiência global judicial | exige triagem de cabimento e mapa completo |
| Fase 104-B | tratamento compulsório dos remanescentes | depende de insucesso consensual e pedido do consumidor |

## 9. Fluxo específico já comprovado na Bahia

O NUPEMEC/TJBA mantém Núcleo de Superendividamento e material operacional que admite:
- reclamação pré-processual;
- anamnese socioeconômica;
- apoio técnico/reeducação;
- proposta global;
- audiência;
- encaminhamento à fase judicial em caso de insucesso;
- ação judicial diretamente proposta com possibilidade de encaminhamento ao Núcleo.

Esse fluxo é referência operacional da Bahia, não regra nacional automática.

## 10. Matriz “pedido → pressuposto”

| Pedido/efeito | Pressuposto mínimo a verificar |
|---|---|
| instaurar 104-A | consumidor pessoa natural + superendividamento + dívidas elegíveis |
| audiência global | universo de credores minimamente identificado |
| sanção ao ausente | ausência injustificada + poderes de transigir + dívida certa/conhecida |
| homologar acordo | consenso + plano juridicamente válido |
| iniciar 104-B | conciliação não exitosa total/parcial + pedido do consumidor |
| plano compulsório | credores remanescentes citados + fase judicial processada |
| tutela provisória | requisitos próprios do CPC + fatos do caso + coerência com regime global |

## 11. Gate da Fase 05

**SATISFEITO.**

O procedimento, as portas de entrada, os pedidos estruturais, os pedidos condicionais, os limites e as alternativas estão persistidos. Questões controvertidas sobre tutela, mínimo existencial, efeitos em contratos específicos e entendimentos dos tribunais passam à Fase 06 — Jurisprudência, doutrina e controvérsias.
