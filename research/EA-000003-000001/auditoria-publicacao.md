# Auditoria de publicação — acoes-judiciais

**Data:** 20/09/2026  
**Fase:** 08/08 — Publicação, auditoria e fechamento  
**Estado:** CONTEÚDO APROVADO TECNICAMENTE; IMPLANTAÇÃO BLOQUEADA POR GITHUB PAGES DESABILITADO

## Artefatos públicos

- Markdown canônico: `acoes/repactuacao-superendividamento.md`
- HTML público: `acoes/repactuacao-superendividamento.html`
- JSON estruturado: `acoes/repactuacao-superendividamento.json`
- Workflow: `.github/workflows/pages.yml`
- Run auditado: `35521317252`

## Verificações

- [x] Markdown, HTML e JSON sincronizados.
- [x] Botão COPIAR MODELO localizado imediatamente acima do bloco exato do modelo.
- [x] JavaScript copia apenas o conteúdo do modelo.
- [x] Nenhum link para edição anterior foi localizado na página pública.
- [x] Nenhum link para research/ ou REQUEST_LOG foi localizado na página pública.
- [x] Workflow constrói artefato apenas com index.html, assets/ e acoes/*.html.
- [x] Etapa Build public-only artifact: SUCCESS.
- [x] Etapa Setup Pages: FAILURE exclusivamente porque Pages não está habilitado/configurado para GitHub Actions.

## Bloqueio comprovado

O repositório reporta `has_pages: false`.

O workflow chegou com sucesso até a construção do artefato público. A ação `actions/configure-pages@v5` falhou na etapa **Setup Pages** porque o GitHub Pages ainda não está habilitado/configurado para usar GitHub Actions.

Esse estado impede declarar:
- `IMPLANTADO`;
- `PUBLICADO`;
- `VERIFICADO_EM_EXECUCAO`.

## Ação externa necessária uma única vez

No GitHub:

1. abrir o repositório;
2. **Settings**;
3. **Pages**;
4. em **Build and deployment**, selecionar **GitHub Actions** como Source.

Depois dessa habilitação, o workflow já existente pode ser reexecutado. O próximo gate é confirmar:
- run concluído com sucesso;
- `has_pages: true`;
- URL pública respondendo;
- homepage e página da Estratégia/Unidade acessíveis;
- recursos CSS/JS carregando;
- comportamento funcional relevante verificado.

## Conclusão da auditoria

O conteúdo e o pipeline estão preparados. A Fase 08 permanece aberta exclusivamente porque a habilitação inicial do GitHub Pages exige uma configuração de repositório que não está disponível nas ações de escrita do conector atual.
