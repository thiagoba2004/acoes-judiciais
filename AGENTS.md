# AGENTS.md — AÇÕES JUDICIAIS

**project_code:** `PRJ-000003`  
**project_sequence:** `000003`  
**project_alias:** `AJ`  
**project_name:** `Ações Judiciais`  
**project_id legado:** `acoes-judiciais`  
**generated_from_kernel:** `1.4`  
**generator_release:** `1.11`  
**repository:** `thiagoba2004/acoes-judiciais`  
**modules:** `research`, `legal`, `publication`, `web-site`, `contact-protocol`, `software`, `legal`, `publication`, `software`

## 1. Missão

Manter uma fonte pública, verificável e atualizável de consulta teórica e prática sobre possíveis ações judiciais para pessoas físicas e jurídicas. Cada ação judicial relevante deve ser tratada como Estratégia Autônoma própria, com fontes, plano, estado e entregas recuperáveis.

## 2. Entrada de qualquer pedido

Todo novo pedido deve seguir esta ordem:

```text
REGISTRAR EM REQUEST_LOG.jsonl
↓
CONFIRMAR TECNICAMENTE O REGISTRO
↓
INFORMAR “PEDIDO REGISTRADO.”
↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS
↓
EXECUTAR
```

## 3. Fonte da verdade

1. `AGENTS.md`;
2. `REQUEST_LOG.jsonl`;
3. `STRATEGY_LOG.jsonl`;
4. `PROJECT_STATE.json`;
5. `ROADMAP.md` e planos de fases;
6. `SOURCE_REGISTRY.jsonl` e fontes recuperáveis;
7. `JURISPRUDENCE_MATRIX.md` para status e recorte dos precedentes centrais;
8. `RESEARCH_DOUTRINA_PROTOCOL.md` para a metodologia doutrinária;
9. arquivos Markdown canônicos de conteúdo;
10. histórico Git comprovado;
11. somente depois, memória/conversa.

## 4. Estratégias e fases

Toda Estratégia Autônoma deve possuir `strategy_code` e `strategy_name` antes da execução substantiva.

Padrão:
```text
EA-000003-EEEEEE
F-000003-EEEEEE-FFF
```

Toda estratégia deve possuir Plano de Fases integralmente numerado, com `phase_number`, `phase_total`, `phase_code`, `phase_name`, estado, objetivo e gate.

## 5. Resposta de continuidade

Quando o usuário perguntar “Onde paramos?” ou equivalente, responder nesta ordem:

```text
PROJETO: PRJ-000003 — Ações Judiciais
ALIAS: AJ
ESTRATÉGIA AUTÔNOMA: <código> — <nome>
FASE: <número>/<total> [<código>] — <nome>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado>
```

## 6. Persistência e verificação

```text
PRODUZIR → SALVAR → VERIFICAR → ATUALIZAR ESTADO → CONTINUAR
```

Nunca afirmar commit, publicação, implantação, jurisprudência verificada ou atualização normativa sem confirmação técnica.

## 7. Módulo research

- distinguir fato encontrado, interpretação e hipótese;
- priorizar fontes primárias e institucionais;
- registrar data de consulta quando a informação puder mudar;
- preservar URL, identificador, documento ou metadados suficientes para recuperação;
- registrar divergências entre fontes;
- não reconstruir citações, números ou datas de memória quando a fonte puder ser recuperada;
- para Notícias e Observatório, separar cadência de busca de gatilho de publicação;
- monitorar por padrão apenas temas já cobertos pelo Site, salvo decisão expressa de expansão;
- quando houver monitoramento recorrente, registrar janela temporal, descritores, fontes prioritárias, data de corte e critérios de relevância;
- no Observatório, aplicar ciclo de horizon scanning: detectar → filtrar → priorizar → avaliar → disseminar → acompanhar;
- usar lógica de evidência viva quando conclusões puderem mudar: data da última busca, versão/data da síntese e registro do que mudou.

## 8. Módulo legal

- distinguir fato comprovado, alegação, interpretação jurídica e conclusão;
- verificar legislação, jurisprudência, súmulas e doutrina crítica antes de usar;
- registrar jurisdição, órgão, processo, data e estado do precedente quando relevantes;
- explicitar competência, legitimidade, prazos, pressupostos, riscos e controvérsias;
- nunca presumir fatos ausentes;
- modelos de peças são pontos de partida e devem indicar variáveis que dependem do caso concreto.

### 8.0. Auditoria adversarial obrigatória

Uma afirmação jurídica relevante **não é considerada auditada apenas porque a fonte citada está correta**. Antes de publicar ou manter tese, precedente, regra, exceção ou síntese jurídica, verificar e registrar, quando materialmente aplicável:

1. fonte primária ou institucional recuperável;
2. recorte exato da tese/regra;
3. condições de incidência;
4. exceções e limites;
5. alcance material e processual;
6. estado processual/recursal do precedente;
7. data da última verificação;
8. existência de superveniência normativa ou jurisprudencial;
9. fidelidade entre a formulação publicada e a fonte;
10. coerência com outras páginas do Site.

Se a conclusão for negativa (por exemplo, “não foi localizado precedente”), documentar bases pesquisadas, descritores e data de corte e qualificá-la como pesquisa negativa datada, nunca como inexistência absoluta.

Quando houver Markdown canônico e HTML público, é obrigatória **paridade semântica**: apresentação visual pode variar, mas nenhuma condicionante, exceção, estado processual, ressalva material ou conteúdo jurídico relevante pode existir em apenas uma das versões.

### 8.1. Teses institucionais de entidades jurídicas não governamentais

Cada Estratégia Autônoma deve identificar, quando materialmente relevante, instituições jurídicas não governamentais especializadas no ramo ou tema estudado — institutos, associações científicas, academias, centros de estudo e entidades equivalentes — e verificar se mantêm enunciados, notas técnicas, pareceres, manifestos, propostas legislativas, memoriais, intervenções como amicus curiae ou outras posições institucionais recuperáveis.

Regras obrigatórias:

- usar preferencialmente a fonte oficial da própria instituição;
- registrar instituição, documento/enunciado, data ou edição, URL e tema;
- deixar explícito que a posição é **institucional e não vinculante**, salvo se o documento tiver outra natureza jurídica comprovada;
- nunca apresentar tese institucional como lei, súmula, precedente vinculante ou jurisprudência consolidada;
- confrontar a posição com legislação e jurisprudência atual;
- classificar a relação, quando possível, como `CONVERGENTE`, `DIVERGENTE`, `CONTROVERTIDA`, `SUPERADA` ou `SEM_CONFRONTO_SUFICIENTE`;
- quando houver divergência relevante, mostrá-la ao leitor em vez de ocultá-la;
- não criar cota artificial de instituições: incluir apenas entidades pertinentes ao tema e com posição verificável;
- a área pública **Doutrina** organiza também teses institucionais; **Fontes** preserva a proveniência e o acesso ao documento institucional;
- cada dossiê de ação deve possuir, quando aplicável, seção **Teses institucionais relevantes**.

### 8.2. Dossiê mínimo por ação judicial

Cada Estratégia Autônoma de ação judicial deve buscar, quando aplicável:

1. problema jurídico e objetivo;
2. hipóteses de cabimento e não cabimento;
3. legitimidade e competência;
4. fatos e documentos necessários;
5. fundamentos normativos;
6. jurisprudência relevante e divergências;
7. procedimento e marcos processuais;
8. pedidos e alternativas;
9. riscos, defesas previsíveis e ônus probatórios;
10. cálculos/simulações quando pertinentes;
11. checklist prático;
12. modelos reutilizáveis, quando aprovados;
13. data e escopo da última revisão.

### 8.3. Protocolo canônico de pesquisa doutrinária

O arquivo `RESEARCH_DOUTRINA_PROTOCOL.md` é obrigatório para toda nova Estratégia Autônoma e para revisões materiais de ações já publicadas.

A pesquisa doutrinária deve, quando materialmente aplicável, percorrer estas camadas:

1. doutrina autoral tradicional;
2. produção acadêmica de faculdades, programas, grupos, núcleos, centros e periódicos de reconhecida excelência;
3. comissões permanentes ou temáticas da OAB, no Conselho Federal e nas Seccionais;
4. institutos e entidades jurídicas especializadas;
5. doutrina profissional especializada produzida por advogados/equipes de escritórios reconhecidos no ramo;
6. posições institucionais interessadas, claramente identificadas como tais.

Regras obrigatórias:

- não criar ranking próprio de autores, faculdades ou escritórios;
- usar critérios externos verificáveis e pertinência temática para selecionar instituições acadêmicas ou profissionais;
- renome/prestígio não substitui leitura, fundamentação, legislação ou jurisprudência;
- identificar sempre autor, documento, data/edição, natureza da fonte e tese efetivamente consultada;
- não atribuir posição a universidade, curso, OAB, comissão, instituto ou escritório quando o texto for apenas de autoria individual;
- distinguir `POSICAO_INSTITUCIONAL_OAB`, `PRODUCAO_DE_COMISSAO` e `AUTORIA_INDIVIDUAL_EM_AMBIENTE_OAB`;
- tratar publicações de escritórios como doutrina profissional especializada e não como recomendação comercial;
- posições de partes interessadas devem ser rotuladas como potencialmente interessadas;
- em controvérsia material, buscar deliberadamente as principais formulações favoráveis e contrárias;
- confrontar toda tese com legislação vigente, precedentes qualificados e jurisprudência atual;
- registrar superveniência, divergência e eventual superação;
- a fase doutrinária não satisfaz o gate se houver atribuição sem leitura, ambiguidade de autoria institucional, ausência de contraditório relevante ou desconsideração de norma/precedente superveniente.

A área pública **Doutrina** pode expor essas categorias e teses relevantes, mas não deve publicar listas promocionais de “melhores escritórios” ou “melhores faculdades”.

## 9. Módulo publication

Para conteúdo textual/editorial publicável, o padrão é:

```text
Markdown (.md) = fonte textual canônica
HTML (.html) = artefato de publicação
JSON (.json) = somente quando houver função estruturada real
```

**JSON não é terceiro artefato obrigatório.** Não criar `.json` apenas para repetir título, resumo, seções, caminhos ou conteúdo já preservado em Markdown e HTML.

JSON/JSONL é apropriado quando houver finalidade objetiva de máquina, como:
- estado e governança do projeto;
- registros append-only;
- configuração;
- datasets, catálogos, taxonomias ou glossários;
- schemas;
- dados consumidos por script, automação, API, busca estruturada, filtro ou validação;
- interoperabilidade comprovada entre projetos.

Para cada novo JSON deve ser possível responder: **quem ou qual processo o consome e que informação estruturada não é adequadamente representada pelo Markdown?** Se não houver resposta concreta, não criar o arquivo.

Alterações editoriais devem ser sincronizadas entre a fonte Markdown e o HTML publicado. JSON existente só precisa ser atualizado quando sua função estruturada exigir. A auditoria final deve comparar semanticamente Markdown e HTML e bloquear a publicação quando houver divergência material.

Quando forem publicados conteúdos editoriais transversais:
- **Notícias** tratam fatos e mudanças verificáveis, com data do fato quando conhecida, data de publicação e fontes recuperáveis;
- **Artigos** tratam análise autoral/argumentativa, distinguindo fatos, direito positivo, jurisprudência, doutrina, inferências, objeções e posição editorial;
- **Observatório** trata pesquisa cumulativa, relações, tendências, lacunas e sínteses atualizáveis, com data de corte e registro de mudanças;
- cada conteúdo possui uma função editorial primária; evitar triplicação do mesmo texto entre as três camadas;
- buscas semanais, mensais, trimestrais, semestrais e anuais podem coexistir, mas publicação depende de materialidade e não do calendário isoladamente.

Se forem publicados Modelos reutilizáveis:

- o botão **COPIAR MODELO** deve ficar imediatamente acima do texto exato a copiar;
- a função copia apenas o Modelo;
- somente a edição vigente fica acessível no Site Público;
- versões anteriores permanecem no Git ou em mecanismo não publicado;
- a verificação deve testar posição do botão, alvo da cópia e ausência de acesso público à edição superada.

### 9.1. Separação entre governança interna e Site Público

O Site Público é orientado ao leitor externo. A governança do projeto permanece no repositório e **não deve ser exibida na interface pública**.

É proibido publicar na UI, rodapé, cabeçalho, cards, tabelas, modelos ou metadados destinados ao navegador:

- códigos internos de projeto, estratégia, fase, pedido, evento ou fonte (`PRJ-*`, `EA-*`, `F-*`, `REQ-*`, `EVT-*`, `SRC-*`);
- número/total de fases, gates, estados de workflow ou estados editoriais/técnicos;
- versões de kernel/gerador, IDs de deployment, run, commit, branch ou arquivos de governança;
- nomes como `PROJECT_STATE`, `REQUEST_LOG`, `STRATEGY_LOG`, `AGENTS` ou equivalentes;
- rótulos de controle metodológico que só façam sentido internamente.

Pode permanecer público quando útil ao leitor:

- título e conteúdo material;
- data de atualização/revisão em linguagem comum;
- fontes jurídicas, bibliográficas e institucionais;
- avisos de uso e limitações;
- ferramentas, modelos e explicações em linguagem natural.

Antes de cada publicação, executar varredura de vazamento de governança. A presença de qualquer marcador interno na camada pública bloqueia o deploy.

## 10. Módulo web-site

O Site é uma arquitetura pública multipágina. Não pode ser reduzido a uma Home com cards e uma página longa.

**Menu global obrigatório vigente:** Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Fale Conosco.

**Arquitetura editorial planejada:** `EDITORIAL_HUB` com rótulo **Publicações**, contendo Notícias, Artigos e Observatório. O hub só entra no menu público após existir conteúdo real nas páginas centrais, rotas auditadas e workflow do GitHub Pages atualizado.

**Menu futuro após o gate de conteúdo:** Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Publicações · Fale Conosco.

Regras obrigatórias:
- o mesmo menu global aparece em todas as páginas;
- a página corrente usa `aria-current="page"`;
- no mobile, o menu permanece acessível em linha horizontal rolável;
- a Home é institucional e enxuta; não contém catálogo dos Menus nem “Explore o Site”;
- toda página pública possui no rodapé o hiperlink **Mapa do Site**;
- toda página pública deve possuir `<title>` técnico no `<head>` e exatamente um `<h1>` editorial visível no corpo; páginas de dossiê/ação devem exibir o título antes do índice local;
- o `<h1>` editorial não pode usar escala de manchete gigante: deve ficar apenas moderadamente maior que o corpo, seguindo o `SITE_STYLE_GUIDE.md`; em mobile, títulos longos não podem ser artificialmente comprimidos por `max-width` estreito nem provocar overflow horizontal;
- a auditoria de publicação deve verificar separadamente presença de `<title>`, quantidade de `<h1>` e visibilidade editorial do título, para impedir páginas cujo título exista apenas na aba do navegador;
- `mapa-do-site/` reflete as rotas públicas reais;
- páginas centrais de Menu possuem conteúdo útil, não placeholders;
- Publicações não substitui áreas estáveis: Notícias = mudança factual; Artigos = análise autoral; Observatório = síntese sistêmica cumulativa;
- as rotas planejadas são `/publicacoes/`, `/publicacoes/noticias/`, `/publicacoes/artigos/` e `/publicacoes/observatorio/`;
- o Mapa do Site deve expor as três subáreas quando públicas, mesmo agrupadas sob o hub;
- cada notícia deve apontar para a página jurídica estável afetada quando houver; artigos e observatórios devem usar referências cruzadas, não duplicação;
- Doutrina é área material própria e não deve ser absorvida por Fontes; Fontes registra proveniência e acesso, enquanto Doutrina organiza conteúdo interpretativo por tema/ação;
- toda publicação doutrinária deve separar metadados verificados, escopo seguro de uso e teses efetivamente lidas;
- a interface pública não exibe códigos, estados e metadados de governança interna;
- `SITE_ARCHITECTURE.md` é a fonte da arquitetura;
- `SITE_STYLE_GUIDE.md` é a fonte da identidade visual;
- mudanças estruturais exigem auditoria desktop/mobile, links, overflow e navegação;
- cards clicáveis e cards meramente informativos devem ser visualmente distintos: navegação usa cor própria + estado de hover; conteúdo estático permanece neutro e não recebe efeito de clique; nunca compensar falta de diferenciação visual com rótulos redundantes como “ACESSAR →”;
- toda nova rota pública deve ser incluída explicitamente no workflow de GitHub Pages (`paths`, diretório `_site` e cópia para o artefato) antes de considerar o deploy concluído;
- auditoria de publicação deve verificar a presença da rota no artefato público, não apenas no repositório.

**Identidade visual:** deve ser exclusiva deste projeto. Reutilizar a estrutura do Classe e Massas não autoriza reutilizar sua paleta, tipografia ou composição.

## 11. Módulo contact-protocol

O Fale Conosco adota o padrão técnico de referência do Classe e Massas:

```text
Forminit = recebimento/aceite da submissão e anexos
EmailJS  = confirmação do protocolo ao e-mail informado
```

Regras:
- e-mail institucional: `acoesjudiciais2026@gmail.com`;
- prefixo: `AJ-`;
- `CONTACT_STACK.md` documenta a configuração e o estado;
- FormSubmit não é stack canônica e a implementação atual deve ser migrada;
- é proibido substituir Forminit/EmailJS por outro provedor sem decisão expressa e persistida;
- o protocolo pode ser preparado antes do envio, mas só é **confirmado** após sucesso do Forminit;
- EmailJS só é acionado após recebimento confirmado;
- falha no EmailJS não invalida um protocolo já aceito pelo Forminit;
- a página de confirmação usa `noindex,nofollow` e oferece **Copiar protocolo**;
- cada projeto deve ter Forminit próprio ou isolamento de roteamento comprovado;
- o canal só é declarado operacional após teste end-to-end real de recebimento + protocolo + e-mail.

**Estado atual:** `E2E_VERIFICADO` com Forminit + EmailJS.

## 12. Módulo software

- distinguir IMPLEMENTADO, TESTADO, VERSIONADO, IMPLANTADO e VERIFICADO EM EXECUÇÃO;
- testar alterações de comportamento quando tecnicamente possível;
- preservar compatibilidade, configuração e segurança;
- não confundir arquivo no repositório com site efetivamente publicado.

## 13. Interoperabilidade com outros projetos

Temas com consequências financeiras, inclusive **superendividamento** e **divórcio litigioso com partilha, guarda, convivência e alimentos**, podem ser estudados também no PRJ-000004 — Planejamento Financeiro. O PRJ-000003 permanece fonte da verdade para questões jurídicas; o PRJ-000004 pode usar resultados jurídicos confirmados como premissas/cenários financeiros. Cada projeto mantém estratégia, fontes, análise e conclusão próprias. Não copiar silenciosamente conteúdo entre projetos.

## 14. Fechamento

Antes de declarar uma etapa concluída, confirmar persistência, versão remota, estado, fontes críticas, coerência dos artefatos publicados e próximo passo lógico.

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
