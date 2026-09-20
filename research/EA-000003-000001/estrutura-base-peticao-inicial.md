# Estrutura-base de petição inicial — Repactuação de dívidas por superendividamento

**Estratégia:** EA-000003-000001  
**Fase:** 07/08 — Ferramentas práticas  
**Estado:** ESQUELETO REUTILIZÁVEL COM VARIÁVEIS — NÃO É PETIÇÃO PRONTA  
**Data:** 20/09/2026

> Este arquivo define estrutura e campos obrigatórios. Antes de uso em caso real, todos os fatos, competência, documentos, valores, pedidos e precedentes devem ser conferidos.

## 1. Endereçamento

`[VAR_JUIZO_COMPETENTE]`

Antes de preencher:
- conferir competência estadual/federal;
- conferir unidade interna/local;
- não presumir Juizado Especial;
- conferir domicílio/foro aplicável.

## 2. Partes

**Autor(a):** `[VAR_CONSUMIDOR]`  
**Qualificação:** `[VAR_QUALIFICACAO]`

**Credores abrangidos:**  
1. `[VAR_CREDOR_1]`  
2. `[VAR_CREDOR_2]`  
3. `[VAR_CREDOR_N]`

Anexar quadro consolidado de credores.

## 3. Objeto

Indicar que se busca, conforme o caso concreto:

- instauração autônoma do procedimento de repactuação;
- realização de audiência global de conciliação;
- apresentação e discussão de plano de pagamento;
- preservação do mínimo existencial;
- tratamento das dívidas de consumo elegíveis.

**Não inserir dívida excluída apenas para aumentar artificialmente o passivo submetido ao rito.**

## 4. Síntese factual cronológica

Preencher:

- renda antes do evento crítico: `[VAR]`;
- renda atual: `[VAR]`;
- evento(s) relevante(s): `[VAR]`;
- despesas essenciais: `[VAR]`;
- evolução do endividamento: `[VAR]`;
- tentativas de negociação: `[VAR]`;
- número e natureza dos credores: `[VAR]`;
- processos/cobranças existentes: `[VAR]`.

Separar fatos comprovados de alegações ainda sem documento.

## 5. Demonstração econômica

Anexar e explicar:

```text
RENDA_LIQUIDA = [VAR]
DESPESAS_ESSENCIAIS = [VAR]
SERVICO_MENSAL_DAS_DIVIDAS = [VAR]
ATIVOS_LIQUIDOS = [VAR]
FLUXO_LIVRE = [VAR]
```

Usar a metodologia da Fase 04.

**Proibição:** converter qualquer fórmula em prova automática do conceito jurídico.

## 6. Enquadramento jurídico

Estruturar em subtópicos:

### 6.1. Pessoa natural e relação de consumo
`[FATOS + DOCUMENTOS]`

### 6.2. Impossibilidade manifesta de pagamento global e mínimo existencial
`[FATOS + DOCUMENTOS + CÁLCULOS]`

### 6.3. Boa-fé
Apresentar elementos concretos, sem tratá-la como slogan nem presumir má-fé por endividamento.

### 6.4. Dívidas abrangidas e excluídas
Inserir tabela contrato a contrato.

### 6.5. Natureza autônoma e global do procedimento
Controlar com AJ-SRC-000015.

## 7. Competência

Selecionar **uma** hipótese demonstrada:

- `[ESTADUAL_SEM_FEDERAL]`;
- `[ESTADUAL_CONCURSO_COM_FEDERAL_E_NAO_FEDERAL]`;
- `[FEDERAL_POLO_EXCLUSIVAMENTE_FEDERAL]`.

Explicar organização local e unidade escolhida.

## 8. Proposta de plano consensual

Tabela:

| Credor | Saldo-base | Proposta | Prazo | Parcela | Encargos negociados | Observações |
|---|---:|---|---:|---:|---|---|
| [VAR] | [VAR] | [VAR] | [VAR] | [VAR] | [VAR] | [VAR] |

O plano deve ser financeiramente coerente com o diagnóstico e respeitar os limites legais.

## 9. Tutela provisória — somente se houver base factual

Criar seção apenas se existirem:
- risco concreto;
- prova documental;
- adequação cautelar;
- pedido individualizado e compatível com o tratamento global.

`[VAR_FATO_URGENTE]`  
`[VAR_PROVA]`  
`[VAR_MEDIDA_CAUTELAR]`

**Não usar percentual-padrão nacional inexistente.**

## 10. Pedidos — matriz condicional

Selecionar apenas o que tiver suporte:

- [ ] recebimento/processamento do procedimento autônomo;
- [ ] convocação/citação dos credores abrangidos para audiência global;
- [ ] designação de audiência de conciliação;
- [ ] consideração da proposta de plano apresentada;
- [ ] eventual tutela cautelar especificamente fundamentada;
- [ ] aplicação, quando comprovados os pressupostos, das consequências legais relativas ao credor injustificadamente ausente/sem poderes adequados;
- [ ] homologação de acordo total ou parcial;
- [ ] providências relativas a ações e cadastros apenas nos termos do plano/acordo;
- [ ] após insucesso e **a pedido do consumidor**, instauração da fase do art. 104-B quanto aos créditos remanescentes;
- [ ] demais providências estritamente decorrentes dos fatos comprovados.

## 11. Provas e anexos

Numerar:
1. identificação/residência;
2. renda;
3. despesas essenciais;
4. inventário e contratos;
5. extratos/faturas;
6. negativações/cobranças;
7. tentativas de negociação;
8. planilha financeira;
9. documentos dos eventos críticos;
10. processos em curso;
11. outros.

## 12. Controle final antes do protocolo

- [ ] todos os fatos têm fonte ou estão marcados como alegação;
- [ ] todos os credores foram inventariados;
- [ ] dívidas excluídas não foram tratadas como elegíveis;
- [ ] competência foi atualizada;
- [ ] consignado não foi excluído do mínimo existencial com base na regra invalidada pelo STF;
- [ ] precedentes estão atuais e identificados;
- [ ] plano cabe no fluxo financeiro demonstrado;
- [ ] tutela, se houver, é cautelar e individualmente fundamentada;
- [ ] pedidos não excedem os fatos;
- [ ] valores e documentos foram conferidos.

## 13. Fontes de controle

CDC consolidado; AJ-SRC-000014; AJ-SRC-000015; matriz de cabimento; matriz requisito-fato-prova; mapa processual; matriz jurisprudencial.
