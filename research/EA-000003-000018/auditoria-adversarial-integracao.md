# EA-000003-000018 — Fase 05/06
## Auditoria adversarial da integração — separação de fato, renda do cônjuge e patrimônio

**Data de corte:** 21/09/2026.

## Escopo
Auditar o conteúdo integrado em:
- `acoes/repactuacao-superendividamento.md`;
- `acoes/repactuacao-superendividamento.html`;
- modelo reutilizável;
- área pública `modelos/`;
- matriz canônica de jurisprudência.

## Testes jurídicos

### 1. “Casado = soma automática da renda do cônjuge”
**REJEITADO.** Não foi localizada regra legal nacional que imponha soma automática. O texto público preserva a distinção entre dado informativo, custeio, transferência econômica e responsabilidade jurídica.

### 2. “Separado de fato = renda do cônjuge jamais pode ser conhecida”
**REJEITADO.** Há jurisprudência estadual exigindo documentação do cônjuge para compreender o orçamento familiar. O texto alerta para esse risco e não promete irrelevância absoluta.

### 3. “Separação de fato = divórcio”
**REJEITADO.** O texto mantém estado civil formal de casado e trata a separação como fato juridicamente relevante sujeito a prova.

### 4. “Separação de fato apaga patrimônio comum anterior”
**REJEITADO.** O texto distingue cessação prospectiva da eficácia do regime de bens de direitos patrimoniais já constituídos.

### 5. “Apartamento financiado entra no plano”
**REJEITADO.** Art. 104-A, § 1º, do CDC exclui financiamento imobiliário.

### 6. “Apartamento vale integralmente como patrimônio líquido”
**REJEITADO.** O texto exige valor de mercado, saldo devedor, direitos aquisitivos e meação potencial.

### 7. “Veículo financiado fiduciariamente é certamente excluído por tese vinculante do STJ”
**REJEITADO.** A redação pública usa jurisprudência estadual e explicita ausência de tese repetitiva específica do STJ encontrada até a data de corte.

### 8. “Ter patrimônio impede automaticamente a repactuação”
**REJEITADO.** O art. 104-A, § 5º, afasta a equivalência com declaração de insolvência civil. O patrimônio permanece relevante para boa-fé, liquidez e coerência econômica.

## Pesquisa negativa datada

Até 21/09/2026 não foi localizada:
- regra legal nacional de soma automática da renda do cônjuge;
- tese repetitiva do STJ específica sobre renda de cônjuge separado de fato no superendividamento;
- tese repetitiva do STJ específica sobre inclusão/exclusão de financiamento de veículo com alienação fiduciária no plano da Lei 14.181/2021.

Esses registros não significam inexistência absoluta e devem ser rechecados antes de uso profissional futuro.

## Auditoria técnica

Resultado da verificação automatizada sobre o dossiê alterado:
- exatamente 1 `<title>`;
- exatamente 1 `<h1>`;
- 14 links de âncora local no índice e 0 âncoras ausentes;
- 1 botão `COPIAR MODELO`;
- alvo `modelo-peticao` existente;
- botão imediatamente acima do bloco copiável;
- modelo Markdown e HTML com conteúdo textual idêntico;
- 0 duplicações de “VI — DO PLANO CONSENSUAL”;
- 0 marcadores internos `PRJ-*`, `EA-*`, `F-*`, `REQUEST_LOG`, `STRATEGY_LOG`, `PROJECT_STATE` ou `AGENTS.md` na camada pública;
- área `modelos/` mantém link para `#modelo`.

## Proveniência pública

A lista pública de fontes foi ampliada para incluir:
- Código Civil;
- STJ — REsp 2.180.444/MT;
- STJ — AgInt no AREsp 3.032.409/SP;
- TJSP — AI 2017822-94.2025.8.26.0000;
- TJSP — Ap. 1182227-29.2023.8.26.0100.

## Gate da Fase 05

**SATISFEITO.** Nenhuma fragilidade material aberta impede a publicação. Permanecem apenas as ressalvas expressamente documentadas quanto ao caráter não vinculante dos precedentes estaduais e às pesquisas negativas datadas.
