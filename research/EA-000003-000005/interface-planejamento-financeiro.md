# Interface com Planejamento Financeiro — Divórcio litigioso

## Regra
O PRJ-000003 fornece **premissas jurídicas confirmadas** ou marca explicitamente o que é controvertido. O PRJ-000004 não decide direitos.

## Pacote de dados a transferir

### Patrimônio
- ativo/passivo;
- valor bruto;
- saldo devedor;
- valor líquido;
- data-base;
- regime de bens;
- status jurídico: CONFIRMADO_COMUNICÁVEL / CONFIRMADO_PARTICULAR / CONTROVERTIDO / NÃO ANALISADO;
- percentual apenas quando juridicamente confirmado.

### Filhos
- despesas mensais equivalentes;
- despesas sazonais/extraordinárias;
- residência-base confirmada ou cenários;
- convivência confirmada ou cenários;
- custos logísticos;
- alimentos provisórios efetivamente fixados.

### Fluxo
- renda comprovada;
- renda variável;
- obrigações atuais;
- despesas de transição;
- custos jurídicos/tributários apenas quando conhecidos.

## Rótulos obrigatórios
- `JURIDICO_CONFIRMADO`
- `CENARIO_A`
- `CENARIO_B`
- `CONTROVERTIDO`
- `DADO_AUSENTE`

## Proibição
Nunca converter:
- pedido em direito adquirido;
- valor pretendido em valor judicial;
- bem litigioso em patrimônio líquido disponível;
- guarda pretendida em premissa definitiva de moradia;
- alimentos pedidos em fluxo garantido.
