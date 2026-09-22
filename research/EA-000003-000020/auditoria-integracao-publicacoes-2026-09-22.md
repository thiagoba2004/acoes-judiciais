# Auditoria da integração editorial — 22/09/2026

## Escopo

Integração pública de **Publicações → Notícias / Artigos / Observatório** no Site Ações Judiciais.

## Resultado

- páginas HTML auditadas: **20**;
- páginas com item **Publicações** no menu global: **20/20**;
- links internos (`href`) verificados: **540**;
- links internos quebrados: **0**;
- marcadores internos de governança expostos na camada pública: **0**;
- pares Markdown/HTML criados para Hub, Notícias, Artigos e Observatório: **4/4**;
- JSON editorial espelho criado: **não** — política de JSON condicional preservada;
- Mapa do Site atualizado: **sim**;
- `SITE_ARCHITECTURE.md` atualizado: **sim**;
- workflow inclui `publicacoes/**` e copia as quatro rotas públicas: **sim**.

## Deploy

- commit público final: `6d161d0656f3053ea56d65b617d98c3a787f46e2`;
- GitHub Actions run: `35728854051`;
- job `deploy`: **success**;
- Checkout: success;
- Build public-only artifact: success;
- Setup Pages: success;
- Upload Pages artifact: success;
- Deploy to GitHub Pages: success.

## Observação de verificação

A tentativa de leitura HTTP independente das novas URLs pelo mecanismo externo disponível nesta sessão não conseguiu acessar o domínio GitHub Pages. Por isso, a comprovação de publicação adotada neste fechamento é o pipeline oficial do próprio repositório, cujo build, upload do artefato e etapa **Deploy to GitHub Pages** concluíram com sucesso.

## Gate de não redundância

Satisfeito:
- Notícias = mudança temporal/factual;
- Artigos = análise e argumentação;
- Observatório = conhecimento cumulativo, sinais, lacunas e revalidação;
- Ações/dossiês = fonte temática estável.
