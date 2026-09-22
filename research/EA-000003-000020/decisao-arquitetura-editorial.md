# Decisão de arquitetura editorial — EA-000003-000020

## Decisão

Adotar **EDITORIAL_HUB** no Site Ações Judiciais.

### Rótulo do hub
**Publicações**

### Estrutura planejada
- Publicações
  - Notícias
  - Artigos
  - Observatório

### Rotas planejadas
- `/publicacoes/`
- `/publicacoes/noticias/`
- `/publicacoes/artigos/`
- `/publicacoes/observatorio/`

## Justificativa

1. O menu atual já possui nove itens estáveis.
2. As três novas funções são transversais, não novas matérias jurídicas.
3. Um hub acrescenta apenas um item de primeiro nível e preserva a legibilidade.
4. O rótulo **Publicações** é mais abrangente que “Atualidades”, “Análises” ou “Pesquisa” e não reduz nenhuma das três subáreas a apenas uma de suas funções.
5. O hub terá página própria e útil; não será dropdown vazio.
6. As três subáreas aparecerão também no Mapa do Site.
7. Notícias, Artigos e Observatório permanecem semanticamente autônomos e recebem rotas próprias.
8. A implementação pública fica bloqueada até existirem páginas centrais com conteúdo real e até o workflow do GitHub Pages incorporar as novas rotas.

## Menu futuro, após o gate de conteúdo

Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · **Publicações** · Fale Conosco

## Relações editoriais

- notícia → linka para dossiê/legislação/jurisprudência afetada;
- artigo → linka para bases jurídicas e doutrinárias relevantes;
- observatório → sintetiza e conecta evidências, tendências e lacunas;
- páginas estáveis → podem apontar para publicações relacionadas, mas continuam sendo a referência estrutural do tema.

## Gate da Fase 02

**SATISFEITO.** Modo de navegação, rótulo, rotas e regra de não redundância definidos. A alteração pública aguarda as estratégias filhas.
