# Roteiro de triagem inicial — Repactuação por superendividamento

**Projeto:** PRJ-000003 — Ações Judiciais  
**Estratégia:** EA-000003-000001 — Ação de Repactuação de Dívidas por Superendividamento  
**Fase:** 07/08 — Ferramentas práticas  
**Data de revisão:** 20/09/2026  
**Estado:** INSTRUMENTO OPERACIONAL — NÃO SUBSTITUI ANÁLISE DO CASO

## 1. Identificação e escopo

Registrar antes de concluir qualquer enquadramento:

- nome e qualificação do interessado;
- pessoa natural? `SIM/NÃO`;
- domicílio e comarca;
- renda líquida média e estabilidade;
- composição familiar e dependentes;
- despesas essenciais documentadas;
- ativos líquidos disponíveis;
- lista completa de credores e contratos;
- processos judiciais/cobranças já existentes;
- urgências concretas alegadas e respectiva prova.

**Parada:** se o requerente não for pessoa natural consumidora, esta Estratégia Autônoma não é a ferramenta adequada.

## 2. Relação de consumo e natureza das dívidas

Para cada dívida, classificar:

| Campo | Registro |
|---|---|
| Credor | [VAR_CREDOR] |
| Origem | crédito / compra a prazo / serviço continuado / outra |
| Relação de consumo demonstrada? | sim / não / duvidosa |
| Saldo atual | [VAR_SALDO] |
| Parcela/serviço mensal | [VAR_PARCELA] |
| CET/taxa conhecida? | [VAR_CET] |
| Vencida/vincenda | [VAR_STATUS] |
| Garantia real? | sim / não |
| Financiamento imobiliário? | sim / não |
| Crédito rural? | sim / não |
| Indício de fraude/má-fé ou contratação dolosa sem propósito de pagar? | sim / não / controvertido |
| Produto/serviço de luxo de alto valor em hipótese do art. 54-A §3º? | sim / não / controvertido |
| Elegibilidade preliminar | incluir / excluir / análise jurídica necessária |

**Regra:** exclusões devem ser feitas contrato a contrato. Não excluir toda a situação financeira por existir uma dívida não abrangida.

## 3. Núcleo do superendividamento

Perguntas obrigatórias:

1. há impossibilidade **global** de pagar as dívidas de consumo exigíveis e vincendas?
2. o pagamento integral comprometeria o mínimo existencial?
3. os dados demonstram insuficiência persistente ou apenas dificuldade transitória?
4. a boa-fé pode ser sustentada pelos fatos e documentos disponíveis?
5. há contradições relevantes entre renda, patrimônio, consumo, contratos e alegações?
6. o problema exige tratamento global ou é litígio isolado de um único contrato?

**Nunca concluir automaticamente** pelo número de credores, pelo percentual de comprometimento ou pelo valor de R$ 600,00 isoladamente.

## 4. Documentos mínimos

Solicitar, conforme o caso:

- documento de identificação e comprovante de residência;
- comprovantes de renda e extratos bancários;
- comprovantes das despesas essenciais;
- contratos, faturas, demonstrativos e extratos dos débitos;
- SCR/Registrato e outras fontes de inventário quando pertinentes;
- comprovantes de renegociações anteriores;
- comunicações de cobrança e negativações;
- documentos de ações judiciais em curso;
- planilha de diagnóstico financeiro do Projeto;
- documentos de eventos que afetaram renda/despesa, se alegados.

Marcar cada item como `COMPROVADO`, `DECLARADO_NAO_COMPROVADO`, `DIVERGENTE` ou `NAO_INFORMADO`.

## 5. Competência e porta de entrada

### 5.1. Credores

- sem ente federal: Justiça Estadual/Distrital, com verificação da organização interna/local;
- concurso global com credores federais e não federais: Justiça Estadual/Distrital, conforme linha consolidada do STJ;
- polo passivo exclusivamente formado por instituição(ões) financeira(s) federal(is): Justiça Federal;
- cobrança autônoma promovida por empresa pública federal: permanece na Justiça Federal.

### 5.2. Unidade interna

Verificar:
- Vara Cível, unidade especializada, CEJUSC/Núcleo ou fluxo local;
- compatibilidade com Juizado Especial — **não presumir regra nacional uniforme**;
- competência territorial e atos atuais do tribunal.

## 6. Escolha do caminho procedimental

### Caminho A — fase conciliatória judicial
Adequado quando se pretende instaurar autonomamente o procedimento do art. 104-A, com proposta de plano.

### Caminho B — fase conciliatória administrativa/pré-processual
Avaliar Procon, CEJUSC/Núcleo ou estrutura equivalente, conforme art. 104-C e regulamentação local.

### Caminho C — fase judicial compulsória
Após insucesso total ou parcial da conciliação, avaliar pedido do consumidor para instauração do processo do art. 104-B quanto às dívidas remanescentes.

**Regra STJ:** o procedimento do art. 104-A é autônomo; não tratar como mero incidente dentro de execução em curso.

## 7. Plano consensual — dados para preparar

O plano precisa ser construído a partir de capacidade de pagamento demonstrável.

Registrar:
- prazo pretendido, observado o limite legal;
- renda líquida recorrente;
- despesas essenciais;
- margem mensal efetivamente sustentável;
- ordem e forma de pagamento propostas;
- encargos cuja redução será negociada;
- ações judiciais que podem ser suspensas/extintas por acordo;
- data pretendida para retirada de registros de inadimplência;
- medidas para evitar agravamento do endividamento.

## 8. Tutela provisória

Perguntar antes de formular pedido:
- qual risco concreto existe?
- qual prova demonstra urgência?
- a medida é cautelar e compatível com o tratamento global?
- o pedido preserva contraditório, contratos e peculiaridades do caso?

A jurisprudência superior consolidada no Projeto admite tutela **cautelar**, não um efeito satisfativo automático ou um teto nacional uniforme de descontos.

## 9. Saída da triagem

Classificar o caso em uma das seguintes situações:

- `APTO_PARA_APROFUNDAMENTO_104A`;
- `APTO_PARA_VIA_PRE_PROCESSUAL`;
- `POSSIVEL_104B_APOS_CONCILIACAO`;
- `DIVIDAS_PARCIALMENTE_EXCLUIDAS`;
- `COMPETENCIA_A_CONFIRMAR`;
- `PROVA_INSUFICIENTE`;
- `FORA_DO_ESCOPO_DESTA_ESTRATEGIA`.

A classificação é de **triagem**, não decisão judicial nem promessa de resultado.

## 10. Fontes de controle

- AJ-SRC-000001 — CDC consolidado;
- AJ-SRC-000014 — ADPFs 1005, 1006 e 1097/STF;
- AJ-SRC-000015 — Jurisprudência em Teses 282/STJ;
- AJ-SRC-000006 — CC 192.140/DF;
- AJ-SRC-000007 e AJ-SRC-000008 — CNJ/TJBA;
- matriz de cabimento, matriz probatória e matriz jurisprudencial desta Estratégia.
