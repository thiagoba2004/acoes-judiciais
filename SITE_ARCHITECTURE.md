# Arquitetura Pública — Ações Judiciais

## Menu global

Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Publicações · Fontes · Fale Conosco

## Função de cada área

- **Início:** apresentação institucional enxuta; não funciona como catálogo dos Menus.
- **Ações:** catálogo dos dossiês de ações judiciais.
- **Guias:** roteiros operacionais e passo a passo.
- **Modelos:** peças reutilizáveis vigentes.
- **Jurisprudência:** precedentes e teses por controvérsia.
- **Doutrina:** obras, capítulos, artigos, produção acadêmica, produção de Comissões da OAB, teses de entidades jurídicas especializadas, doutrina profissional assinada e posições institucionais interessadas, organizadas por ação/tema com autoria, natureza documental, contraditório e confronto com legislação/jurisprudência.
- **Legislação:** legislação vigente organizada por tema, com **atos institucionais e soft law identificados separadamente** para não confundir lei com recomendação, resolução orientativa ou política judiciária.
- **Publicações:** hub editorial transversal em `/publicacoes/`, com três subáreas: **Notícias** (o que mudou), **Artigos** (como interpretar e problematizar) e **Observatório** (como o estado cumulativo do conhecimento se conecta e evolui). As páginas temáticas permanecem como fonte estável.
- **Fontes:** acesso às fontes primárias, acadêmicas, institucionais e profissionais efetivamente utilizadas, preservando proveniência, autoria e contexto. O Site não cria ranking de universidades ou escritórios.
- **Fale Conosco:** canal protocolado de contato.
- **Mapa do Site:** índice estrutural acessível pelo rodapé, fora do menu global.

## Identidade visual

Paleta exclusiva:
- azul-marinho profundo `#0a1d30`;
- azul jurídico `#122d4a`;
- marfim `#f7f4ed`;
- cobre `#a6532f`;
- dourado discreto `#c8a56a`.

Tipografia:
- títulos: Georgia;
- corpo e navegação: Arial/Helvetica.

A identidade deve comunicar rigor jurídico, consulta e confiabilidade, sem reproduzir a aparência do Classe e Massas.


### Camada doutrinária ampliada

A arquitetura não cria, por padrão, novos itens no Menu global. O conteúdo doutrinário pode vir de autores, academia, OAB, institutos especializados, produção profissional e posições interessadas. O protocolo canônico é `RESEARCH_DOUTRINA_PROTOCOL.md`. As fontes são tratadas em dois níveis:

1. **Doutrina:** apresenta e compara teses, com autoria, natureza documental, contraditório e indicação de caráter não vinculante quando aplicável;
2. **Fontes:** oferece acesso ao documento/página de origem e preserva a proveniência.

Nos dossiês de ações judiciais, quando materialmente relevante, devem existir as camadas necessárias do protocolo — incluindo teses institucionais, produção acadêmica, OAB e doutrina profissional — próximas à jurisprudência para permitir confronto crítico.


## Paridade editorial e auditoria adversarial

- Markdown é a fonte textual canônica e HTML é o artefato público; ambos devem conter o mesmo conteúdo jurídico substantivo.
- Condições, exceções, status recursal, datas de verificação e ressalvas materiais não podem aparecer em apenas um formato.
- Jurisprudência deve ser consolidada em matriz canônica de precedentes, com atualização de status antes de publicação.
- Nova rota pública exige atualização do workflow do GitHub Pages e conferência do artefato implantado.


## Arquitetura editorial transversal — implementada em 22/09/2026

- Modo de navegação: `EDITORIAL_HUB`.
- Rótulo global: **Publicações**.
- Rotas públicas: `/publicacoes/`, `/publicacoes/noticias/`, `/publicacoes/artigos/` e `/publicacoes/observatorio/`.
- O Mapa do Site expõe as três subáreas.
- Cada conteúdo tem função editorial primária; uma mesma evidência pode ser referenciada por mais de uma camada, sem duplicação textual.


## Padrão Coleção → Detalhe — 22/09/2026

- `/publicacoes/noticias/`, `/publicacoes/artigos/` e `/publicacoes/observatorio/` são páginas de **coleção/índice**.
- Cada item publicado possui página individual própria na mesma subpasta.
- O título do item é o hiperlink principal; data, tema e resumo curto orientam a escolha.
- O índice não reproduz integralmente múltiplos conteúdos individuais.
- Markdown e HTML seguem a mesma granularidade.
