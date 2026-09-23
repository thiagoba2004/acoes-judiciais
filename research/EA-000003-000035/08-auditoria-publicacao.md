# Auditoria final de publicação — EA-000003-000035

**Estratégia:** EA-000003-000035 — Erros advocatícios na repactuação por superendividamento e protocolo preventivo  
**Fase:** 08/08 — Publicação, integração, auditoria e deploy  
**Data:** 23/09/2026

## 1. Objeto auditado

- `publicacoes/artigos/erros-advocacia-repactuacao-superendividamento.md`
- `publicacoes/artigos/erros-advocacia-repactuacao-superendividamento.html`
- `publicacoes/artigos/index.md` e `index.html`
- `mapa-do-site/index.md` e `index.html`
- `fontes/index.md` e `index.html`
- workflow `.github/workflows/pages.yml`
- artefato `github-pages` do deploy final

## 2. Paridade Markdown–HTML

A auditoria identificou uma divergência semântica inicial: o subtítulo do artigo estava como `H2` no Markdown e como texto de abertura (`lede`) no HTML. O Markdown foi corrigido no commit `c1be07dc1d53ce6bc2cdee1a75165e1d6ebe67d5`.

Resultado pós-correção:

- 51 headings estruturais no Markdown;
- 51 headings estruturais no HTML;
- zero headings ausentes ou extras entre as versões;
- 1 `H1` em cada versão;
- 21 referências externas únicas em cada versão.

**Gate de paridade:** APROVADO.

## 3. Integração editorial

Confirmado no repositório e no artefato público:

- artigo presente em `publicacoes/artigos/`;
- card presente no índice de Artigos;
- entrada presente no Mapa do Site;
- catálogo público de Fontes atualizado;
- rota abrangida por `publicacoes/**` no gatilho do GitHub Pages;
- workflow copia `publicacoes/artigos/*.html` para o artefato público.

**Gate de integração:** APROVADO.

## 4. Auditoria regressiva do artefato público

Artefato final inspecionado: `github-pages`, artifact id `10746267417`, digest `sha256:25e846501e6118ec2c38826c9304e9e7baa9ba654160229c8a94903e21364445`.

Resultados:

- 26 arquivos HTML auditados;
- 716 ocorrências de `href`;
- 514 links internos resolvidos;
- 69 âncoras internas verificadas;
- zero destinos internos ausentes;
- zero âncoras ausentes;
- todas as páginas com `<title>`;
- exatamente um `<h1>` por página;
- todas as páginas com `meta viewport`;
- zero marcadores internos de governança (`PRJ-*`, `EA-*`, `F-*`, `REQ-*`, `EVT-*`);
- zero atributos `style=` inline no corpus público auditado;
- CSS com chaves balanceadas e 3 media queries responsivas.

**Gate técnico/regressivo:** APROVADO.

## 5. Referências externas do novo artigo

Foram verificadas 21 URLs externas únicas do artigo. As fontes diretamente acessíveis e as que exigiram busca de confirmação foram reconciliadas, incluindo Planalto, STJ, STF, TJDFT, TJSP, CNJ, EPM/TJSP, BDJur/STJ, UFRGS, OAB, Ministério da Justiça e Idec.

A verificação confirmou inclusive o endereço BDJur/STJ `2011/184082/superendividamento_consumidores_aspectos_buzzi.pdf` por indexação do próprio acervo.

**Gate de recuperabilidade das referências:** APROVADO.

## 6. Deploy

GitHub Pages run `35853415203`:

- head commit: `c1be07dc1d53ce6bc2cdee1a75165e1d6ebe67d5`;
- workflow: `Deploy public site to GitHub Pages`;
- job `deploy`: success;
- etapa `Build public-only artifact`: success;
- etapa `Upload Pages artifact`: success;
- etapa `Deploy to GitHub Pages`: success;
- conclusão do run: **success**.

A leitura HTTP direta do domínio `github.io` não ficou disponível no ambiente desta auditoria. Por isso, o fechamento não usa essa leitura como prova. A comprovação foi feita pelo pipeline oficial do GitHub Pages e pela inspeção do artefato efetivamente produzido pelo run.

## 7. Conclusão

Todos os gates previstos para a Fase 08/08 foram satisfeitos. A rota está presente no artefato público, a integração editorial está comprovada, a paridade Markdown–HTML foi corrigida e revalidada, a auditoria regressiva não encontrou falhas e o deploy foi concluído com sucesso.

**Resultado:** FASE 08/08 APROVADA. EA-000003-000035 APTA PARA FECHAMENTO FORMAL.
