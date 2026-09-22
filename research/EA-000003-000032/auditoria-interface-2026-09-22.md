# Auditoria de Interface — Ações Judiciais

**Projeto:** PRJ-000003 — Ações Judiciais  
**Estratégia:** EA-000003-000032 — Auditoria e harmonização semântica da interface do Site Ações Judiciais  
**Data:** 22/09/2026

## Síntese

O padrão geral foi aplicado sem copiar a identidade do Classe e Massas. O Ações Judiciais preserva sua linguagem jurídica de **azul-marinho, marfim e cobre**, títulos serifados e componentes retos.

A divergência encontrada era semântica: a classe genérica `.button` era usada tanto para ações reais quanto para navegação. Isso fazia “Voltar”, “Abrir dossiê”, “Ver jurisprudência”, envio e cópia compartilharem a mesma gramática visual.

## Correções aplicadas

- **ação real:** `action-button` ou `copy-button`;
- **ação primária:** azul-marinho `#122d4a`, texto branco;
- **hover/foco da ação:** azul profundo `#0a1d30`;
- **navegação destacada:** `nav-button`, contorno azul-marinho e detalhe cobre;
- **retorno/navegação simples:** `secondary-link` textual;
- classe genérica `.button`: removida do CSS público e das páginas auditadas;
- cards clicáveis permanecem azul-claro `#e5edf4`, com hover `#d8e4ee`;
- cards informativos permanecem branco-quente/marfim e sem comportamento de clique.

## Páginas corrigidas

- três dossiês de Ações: links de retorno → `secondary-link`;
- Guias: “Abrir dossiê completo” → `nav-button`;
- Jurisprudência: CTAs de consulta → `nav-button`;
- Fale Conosco: “Enviar mensagem” → `action-button`;
- Recibo: “Copiar protocolo” → `action-button`; “Enviar outra mensagem” → `nav-button`.

## Auditoria integral

Foram verificados **24 arquivos HTML públicos**.

Resultado:
- exatamente um `<h1>` em 24/24;
- zero `<style>` ou atributos `style=`;
- zero âncoras com classe genérica `button`;
- zero botões com classe genérica `button`;
- zero âncoras com classe de ação;
- todos os `<button>` usam `action-button` ou `copy-button`;
- menu global presente em 24/24;
- **94 cards clicáveis** e **41 cards informativos** mantêm semântica de tag e diferenciação cromática;
- **7 navegações destacadas** usam `nav-button`;
- **24 links secundários** usam `secondary-link`.

CSS:
- ação primária azul-marinho e hover azul profundo: confirmado;
- card clicável e informativo: diferenciação confirmada;
- menu horizontal rolável no mobile: confirmado;
- chaves CSS balanceadas: confirmado.

## Gate

**APROVADO NO CÓDIGO.**

A próxima etapa é confirmar o pipeline do GitHub Pages e fechar a estratégia.
