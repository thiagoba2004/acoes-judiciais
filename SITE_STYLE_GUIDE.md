# Guia de Identidade Visual — Ações Judiciais

## Princípio

A identidade deve transmitir rigor jurídico, consulta, clareza e confiabilidade. A arquitetura pode reutilizar padrões funcionais de outros Sites, mas a aparência não pode ser copiada.

## Design tokens

- fundo principal: marfim `#f7f4ed`;
- superfície: branco quente `#fffdfa`;
- texto: azul-carvão `#17212b`;
- primária: azul-marinho `#122d4a`;
- primária profunda: `#0a1d30`;
- acento: cobre `#a6532f`;
- acento secundário: dourado discreto `#c8a56a`;
- linha/borda: `#d6d0c5`.

## Tipografia

- títulos: Georgia / Times New Roman;
- corpo, navegação e interface: Arial / Helvetica.

## Componentes

- toda página pública deve possuir `<title>` técnico no `<head>` e exatamente um `<h1>` editorial visível no corpo da página;
- páginas de dossiê/ação devem abrir com bloco `hero`, contendo ao menos `eyebrow`, `<h1>` e texto introdutório (`lede`) antes do índice local;

- cabeçalho escuro e sóbrio;
- cards com bordas retas e ênfase superior;
- **cards clicáveis** (`a.resource-card`) usam fundo azul-claro `#e5edf4`, borda azul acinzentada e faixa superior azul-marinho; no hover, ganham fundo `#d8e4ee`, faixa cobre e leve elevação;
- **cards estáticos** (`article.resource-card`) usam superfície branco-quente/marfim, borda neutra, sem faixa superior colorida, sem deslocamento e sem sombra de hover;
- a diferença entre navegação e informação deve ser perceptível **pela cor e pelo comportamento**, sem rótulos redundantes como “ACESSAR →”;
- tabelas editoriais;
- botões sólidos, sem aparência de aplicativo financeiro;
- leitura longa com largura controlada.

## Home

Institucional e enxuta. Não contém catálogo dos Menus nem bloco “Explore o Site”.

## Mobile

Menu global horizontal rolável, item atual identificável, conteúdo sem overflow geral.

## Diferenciação

Não reutilizar a paleta, tipografia ou linguagem de cards do Classe e Massas ou do Planejamento Financeiro.
