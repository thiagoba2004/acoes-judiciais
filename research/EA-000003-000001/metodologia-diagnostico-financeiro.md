# Metodologia de diagnóstico financeiro — EA-000003-000001

**Fase:** 04/08  
**Finalidade:** produzir diagnóstico reproduzível para subsidiar triagem e construção de cenários de repactuação.

## 1. Princípio

A ferramenta financeira **não decide cabimento jurídico**. Ela mede e organiza o quadro econômico informado/documentado.

O diagnóstico deve manter separados:

```text
DADO BRUTO
PREMISSA
CÁLCULO
RESULTADO
INTERPRETAÇÃO FINANCEIRA
CONCLUSÃO JURÍDICA
```

As duas últimas etapas não podem ser fundidas automaticamente.

## 2. Blocos do diagnóstico

### A. Pessoas e horizonte
- composição familiar;
- dependentes;
- horizonte mensal de análise;
- eventos previsíveis relevantes.

### B. Renda
Para cada entrada:
- fonte;
- valor;
- periodicidade;
- bruto/líquido;
- recorrente/variável;
- período usado na média;
- documento de suporte;
- grau de confiabilidade.

### C. Despesas
Para cada despesa:
- categoria;
- valor;
- periodicidade;
- essencial/discricionária/em análise;
- recorrente/sazonal/extraordinária;
- comprovada/declarada;
- documento de suporte.

### D. Dívidas
Para cada obrigação:
- credor;
- contrato;
- tipo;
- elegibilidade jurídica ainda sujeita à matriz;
- saldo informado;
- saldo documental;
- parcela;
- vencimento;
- taxa/CET quando disponível;
- garantia;
- atraso;
- fonte do dado;
- estado de confirmação.

## 3. Fórmulas mínimas

### 3.1. Renda líquida mensal normalizada

```text
RENDA_LIQ_NORMALIZADA =
soma das rendas líquidas recorrentes
+ média documentada das rendas variáveis pertinentes
```

A média deve registrar o período utilizado. Não usar automaticamente um único mês extraordinário.

### 3.2. Despesa essencial mensal normalizada

```text
DESPESA_ESSENCIAL_NORMALIZADA =
despesas essenciais recorrentes
+ média mensal das despesas essenciais sazonais
```

### 3.3. Margem financeira antes do serviço da dívida

```text
MARGEM_ANTES_DIVIDAS =
RENDA_LIQ_NORMALIZADA
- DESPESA_ESSENCIAL_NORMALIZADA
- RESERVAS/CONTINGENCIAS_JUSTIFICADAS
```

Se negativa, registrar o déficit. Não truncar silenciosamente para zero no dado bruto.

### 3.4. Serviço atual das dívidas

```text
SERVICO_ATUAL_DIVIDAS =
soma das parcelas/descontos mensais das dívidas no cenário analisado
```

Manter separado:
- total de todas as obrigações;
- total das dívidas potencialmente elegíveis;
- total das dívidas excluídas ou ainda controvertidas.

### 3.5. Saldo mensal após dívidas

```text
SALDO_APOS_DIVIDAS =
MARGEM_ANTES_DIVIDAS
- SERVICO_ATUAL_DIVIDAS
```

### 3.6. Índice de serviço da dívida

```text
INDICE_SERVICO_DIVIDA =
SERVICO_ATUAL_DIVIDAS / RENDA_LIQ_NORMALIZADA
```

Resultado meramente analítico. **Não adotar um percentual universal de corte sem fonte jurídica/técnica específica.**

### 3.7. Índice dívida/renda

```text
DIVIDA_RENDA_ANUAL =
SALDO_TOTAL_DIVIDAS / (RENDA_LIQ_NORMALIZADA × 12)
```

Usar como indicador comparativo, não como teste jurídico autônomo.

## 4. Capacidade sustentável para cenários de plano

A capacidade para uma proposta não é automaticamente igual a `MARGEM_ANTES_DIVIDAS`.

Criar pelo menos três cenários quando houver incerteza material:

- **CENÁRIO CONSERVADOR** — premissas de renda/despesa mais prudentes;
- **CENÁRIO BASE** — premissas mais bem documentadas;
- **CENÁRIO DE ESTRESSE** — redução de renda ou aumento de despesa plausível e explicitado.

Cada cenário deve mostrar:

```text
renda
despesas essenciais
contingências
margem
parcela global proposta
saldo remanescente
prazo testado
premissas
```

## 5. Mínimo existencial

Manter dois campos distintos:

1. `PARAMETRO_REGULAMENTAR_VIGENTE` — valor/norma vigente, com fonte e data;
2. `NECESSIDADES_ESSENCIAIS_DOCUMENTADAS` — despesas reais justificadas no caso.

É proibido fazer a planilha concluir que a preservação de um único valor regulamentar resolve, por si só, toda controvérsia jurídica sobre mínimo existencial.

## 6. Dados ausentes e divergentes

Nunca completar automaticamente.

Usar:

- `NAO_INFORMADO`;
- `NAO_COMPROVADO`;
- `SALDO_DIVERGENTE`;
- `TAXA_NAO_DISPONIVEL`;
- `DOCUMENTO_SOLICITADO`.

Se houver dois saldos, calcular cenários separados até a divergência ser resolvida.

## 7. Auditoria

Cada versão do diagnóstico deve informar:
- data-base;
- fontes/documentos usados;
- campos alterados;
- premissas;
- fórmula;
- responsável/revisor quando aplicável.

## 8. Arquivos associados

- `diagnostico-financeiro-template.csv` — estrutura tabular;
- `teste-diagnostico-financeiro.md` — teste lógico com caso fictício;
- matriz jurídico-probatória da mesma estratégia.
