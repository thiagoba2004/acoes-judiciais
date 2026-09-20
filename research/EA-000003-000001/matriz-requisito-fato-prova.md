# Matriz requisito jurídico → fato → prova — EA-000003-000001

**Projeto:** PRJ-000003 — Ações Judiciais  
**Estratégia:** EA-000003-000001 — Ação de Repactuação de Dívidas por Superendividamento  
**Fase:** 04/08 — Fatos, documentos, prova e cálculos  
**Data:** 20/09/2026  
**Estado:** VERSÃO 1 — OPERACIONAL PARA PESQUISA E TRIAGEM

## Regra metodológica

A matriz não converte automaticamente um documento em prova suficiente. Ela organiza a relação entre:

```text
REQUISITO / QUESTÃO JURÍDICA
↓
FATO QUE PRECISA SER DEMONSTRADO
↓
FONTE DE INFORMAÇÃO
↓
DOCUMENTO OU OUTRO MEIO DE PROVA
↓
ESTADO DE COMPROVAÇÃO
↓
LACUNA / PROVIDÊNCIA
```

Estados possíveis:

- `COMPROVADO`;
- `PARCIALMENTE_COMPROVADO`;
- `DECLARADO_NAO_COMPROVADO`;
- `CONTROVERTIDO`;
- `NAO_APLICAVEL`;
- `PENDENTE_DE_DOCUMENTO`;
- `PENDENTE_DE_VERIFICACAO_JURIDICA`.

## Matriz

| Questão jurídica | Fato a demonstrar | Evidência/documento típico | Risco de erro | Estado inicial |
|---|---|---|---|---|
| Pessoa natural consumidora | Identidade e posição de consumidor | documentos pessoais + contratos/relações de consumo | enquadrar pessoa jurídica ou relação não consumerista | PENDENTE |
| Quadro global de superendividamento | impossibilidade manifesta de pagar o conjunto das dívidas elegíveis sem comprometer o mínimo existencial | mapa global de dívidas + renda + despesas + fluxo de caixa | analisar apenas uma dívida isolada | PENDENTE |
| Boa-fé | cronologia, finalidade das contratações, comportamento e tentativas de solução | contratos, extratos, mensagens, protocolos, histórico de renegociação e narrativa coerente | presumir má-fé ou boa-fé sem exame factual | PENDENTE |
| Dívida de consumo elegível | origem consumerista e não incidência de exclusão | contrato, fatura, extrato, demonstrativo do credor | incluir dívida legalmente excluída | PENDENTE |
| Exclusões específicas do art. 104-A | natureza da dívida/garantia | contrato e documentação da garantia | ignorar garantia real, financiamento imobiliário ou crédito rural | PENDENTE |
| Universo de credores | identificação de todos os credores abrangíveis | mapa de credores, registratos/extratos quando pertinentes, contratos e cobranças | plano parcial apresentado como global | PENDENTE |
| Valor/saldo de cada obrigação | saldo-base e condições contratuais | demonstrativo atualizado, contrato, extrato, fatura | inventar saldo/taxa/prazo quando o documento falta | PENDENTE |
| Renda disponível | entradas líquidas recorrentes e variáveis | contracheques, benefícios, extratos, IR, comprovantes de renda | usar renda bruta ou período atípico sem aviso | PENDENTE |
| Despesas essenciais | despesas necessárias do consumidor e família | recibos, contas, contratos, comprovantes de saúde/educação etc. | tratar todas as despesas como essenciais ou descartá-las sem exame | PENDENTE |
| Mínimo existencial | preservação de recursos para subsistência digna conforme marco jurídico vigente e fatos do caso | composição familiar + despesas essenciais + parâmetro normativo aplicável | reduzir o conceito automaticamente a um número fixo sem examinar controvérsias | PENDENTE |
| Capacidade sustentável de pagamento | margem realista após necessidades essenciais e contingências justificadas | modelo financeiro + cenários + documentos de renda/despesa | confundir margem aritmética com capacidade sustentável | PENDENTE |
| Necessidade de tratamento global | interação entre múltiplas obrigações e insuficiência estrutural do fluxo | mapa das dívidas + fluxo mensal + vencimentos | transformar revisão de contrato isolado em ação concursal | PENDENTE |
| Tentativas anteriores | negociações, reclamações ou propostas já realizadas | protocolos, e-mails, WhatsApp, consumidor.gov.br, Procon, banco | afirmar recusa sem prova | DEPENDENTE_DO_CASO |
| Assédio/concessão irresponsável, se alegados | circunstâncias da oferta e avaliação de crédito | publicidade, gravações, mensagens, propostas, contratos, histórico da contratação | inserir alegação grave sem suporte | DEPENDENTE_DO_CASO |
| Competência territorial/unidade | domicílio e organização judiciária vigente | comprovante de residência + atos locais do tribunal | protocolar em unidade inadequada | PENDENTE |
| Credor federal | presença de empresa pública/ente federal | contrato/identificação do credor | deslocar automaticamente à Justiça Federal | DEPENDENTE_DO_CASO |

## Matriz de fontes de informação

### Fonte A — Consumidor
Narrativa, objetivos, histórico, composição familiar e dados ainda não documentalmente confirmados.

### Fonte B — Documentos do consumidor
Comprovantes de renda, despesas, contratos, faturas, extratos, protocolos e correspondências.

### Fonte C — Documentos do credor
Contrato integral, evolução do débito, taxas, saldo, forma de amortização, propostas e registros de atendimento.

### Fonte D — Bases/instituições
Registros oficiais ou institucionais legalmente acessíveis e pertinentes.

### Fonte E — Prova técnica
Cálculos, planilhas, perícia ou análise especializada quando necessária.

## Regra de conflito

Quando duas fontes divergirem:

1. registrar ambas;
2. não escolher silenciosamente uma;
3. identificar qual ponto está controvertido;
4. registrar qual documento adicional pode resolver a divergência;
5. manter cálculos em cenários separados, quando possível.

## Gate desta matriz

A matriz pode ser usada na triagem a partir desta versão, mas deve ser atualizada nas Fases 05 e 06 quando procedimento, jurisprudência e controvérsias alterarem o peso ou a suficiência das provas.
