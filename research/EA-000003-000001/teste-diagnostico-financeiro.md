# Teste lógico do diagnóstico financeiro — caso fictício

**Objetivo:** verificar fórmulas, estados e tratamento de lacunas.  
**Não representa orientação para pessoa real.**

## Caso fictício

Considere um consumidor fictício com:
- uma renda recorrente documentada;
- renda variável histórica em alguns meses;
- despesas essenciais recorrentes;
- despesa médica sazonal;
- dívidas com três credores;
- um dos credores com saldo divergente entre extrato do consumidor e demonstrativo recente;
- uma obrigação cuja elegibilidade jurídica ainda não foi definida.

## Testes obrigatórios

### T1 — renda variável
A planilha não pode somar o último recebimento variável como se fosse renda mensal permanente. Deve exigir período da média.

**Resultado esperado:** PASSA se o período permanece explícito.

### T2 — despesa sazonal
Despesa essencial anual não pode ser ignorada por não ocorrer no mês-base.

**Resultado esperado:** PASSA se for convertida em média mensal com premissa registrada.

### T3 — margem negativa
Se despesas essenciais + contingências superarem a renda, a planilha deve mostrar resultado negativo.

**Resultado esperado:** PASSA se não substituir automaticamente por zero.

### T4 — saldo divergente
Dois valores diferentes para o mesmo débito não podem ser fundidos silenciosamente.

**Resultado esperado:** PASSA se gerar `SALDO_DIVERGENTE` e cenários separados.

### T5 — elegibilidade jurídica pendente
Dívida de elegibilidade controvertida pode aparecer no inventário total, mas não deve ser somada definitivamente ao conjunto elegível.

**Resultado esperado:** PASSA se total global e total elegível permanecerem separados.

### T6 — mínimo existencial
A existência de parâmetro regulamentar não pode apagar as necessidades essenciais documentadas.

**Resultado esperado:** PASSA se os campos jurídicos e factuais permanecerem separados.

### T7 — capacidade de pagamento
A parcela proposta não pode ser preenchida automaticamente com 100% da margem antes das dívidas.

**Resultado esperado:** PASSA se a proposta exigir decisão/premissa própria e teste de cenário.

### T8 — rastreabilidade
Todo valor relevante deve possuir fonte, estado ou observação de ausência.

**Resultado esperado:** PASSA se nenhum dado ausente for convertido em zero sem marcação.

## Resultado da validação estrutural

O modelo satisfaz os oito testes por construção de esquema. A validação matemática com valores concretos deverá ocorrer quando forem criados casos didáticos da Fase 07 ou quando houver um caso real devidamente anonimizado/autorizado.
