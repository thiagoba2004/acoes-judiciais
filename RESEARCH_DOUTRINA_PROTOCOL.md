# PROTOCOLO DE PESQUISA DOUTRINÁRIA — AÇÕES JUDICIAIS

**Projeto:** PRJ-000003 — Ações Judiciais
**Aplicação:** todas as novas Estratégias Autônomas e revisões materiais de ações já publicadas
**Data de adoção:** 21/09/2026

## 1. Finalidade

Ampliar a pesquisa doutrinária para além de livros e artigos tradicionais, mantendo rigor de autoria, proveniência, contraditório e hierarquia jurídica.

O protocolo não cria ranking de autores, faculdades ou escritórios e não transforma prestígio institucional em autoridade normativa.

## 2. Camadas de pesquisa

### 2.1. Doutrina autoral tradicional

Livros, tratados, manuais, capítulos, artigos científicos e pareceres de autores identificados.

Registrar, quando disponível:
- autor;
- título;
- edição/ano;
- editora/periódico;
- página ou trecho efetivamente consultado;
- tese atribuída;
- contexto e eventuais limites.

### 2.2. Produção acadêmica de excelência

Pesquisar produção vinculada a faculdades, programas de pós-graduação, grupos de pesquisa, núcleos, centros de estudo e periódicos jurídicos de reconhecida qualidade acadêmica.

A seleção não deve depender de um ranking próprio do Site. Usar critérios externos verificáveis e pertinência temática, como avaliação institucional oficial, reconhecimento acadêmico, produção do programa/grupo e especialização dos autores.

Não atribuir ao curso ou universidade uma 'posição institucional' quando o texto for de autoria individual. Identificar o autor, vínculo acadêmico e natureza do documento.

### 2.3. Comissões da OAB

Pesquisar, quando pertinente, o Conselho Federal e as Seccionais da OAB, especialmente comissões permanentes ou temáticas relacionadas ao ramo estudado.

Podem ser considerados:
- pareceres;
- notas técnicas;
- estudos;
- enunciados;
- cartilhas técnicas;
- artigos;
- relatórios;
- audiências/debates com documentação recuperável.

Classificar corretamente a autoria:
- `POSICAO_INSTITUCIONAL_OAB` quando houver aprovação/adoção institucional verificável;
- `PRODUCAO_DE_COMISSAO` quando atribuível à comissão;
- `AUTORIA_INDIVIDUAL_EM_AMBIENTE_OAB` quando for opinião de membro ou palestrante sem adoção institucional.

Nenhuma dessas categorias é vinculante por si só.

### 2.4. Institutos e entidades jurídicas especializadas

Pesquisar institutos, associações científicas, academias e centros de estudo pertinentes ao tema.

Separar posição institucional de produção individual hospedada pela entidade.

### 2.5. Doutrina profissional especializada

Pesquisar artigos, legal updates, pareceres e análises assinadas por advogados ou equipes de escritórios reconhecidos no ramo jurídico específico.

Critérios mínimos:
- autoria identificada;
- área de atuação pertinente;
- texto jurídico recuperável;
- conteúdo substantivo, não meramente promocional;
- reconhecimento externo verificável da especialidade ou produção técnica consistente;
- data e contexto identificáveis.

Não criar lista de 'melhores escritórios'. O escritório entra somente como contexto de autoria/proveniência da tese.

### 2.6. Posições institucionais interessadas

Quando materialmente relevante, podem ser pesquisadas posições de bancos, seguradoras, empresas, sindicatos, associações empresariais, entidades de consumidores ou outros atores com interesse no resultado da controvérsia.

Essas posições devem ser explicitamente identificadas como potencialmente interessadas e nunca confundidas com doutrina neutra.

## 3. Hierarquia metodológica

A força jurídica da conclusão não decorre do prestígio da fonte doutrinária.

Ordem de controle:
1. Constituição e legislação vigente;
2. precedentes vinculantes e jurisprudência qualificada;
3. atos normativos e regulatórios competentes;
4. jurisprudência persuasiva relevante;
5. doutrina e produção técnico-institucional;
6. posições interessadas.

A doutrina interpreta e critica as fontes superiores; não as substitui.

## 4. Contraditório doutrinário obrigatório

Quando houver controvérsia material:
- localizar as principais formulações favoráveis e contrárias;
- identificar autores e instituições de cada corrente;
- expor os fundamentos de cada tese;
- verificar se alguma posição foi superada por lei ou precedente posterior;
- registrar convergências parciais;
- não selecionar apenas fontes que confirmem a hipótese inicial.

Classificações úteis:
- `CONVERGENTE`;
- `DIVERGENTE`;
- `CONTROVERTIDA`;
- `SUPERADA`;
- `SEM_CONFRONTO_SUFICIENTE`.

## 5. Regra de atribuição

Toda tese deve responder:
- quem sustenta?
- em qual documento?
- em qual data/edição?
- qual trecho ou fundamento foi efetivamente consultado?
- a posição é individual, acadêmica, institucional ou interessada?
- existe atualização posterior relevante?

É proibido escrever 'a universidade entende', 'a OAB entende' ou 'o escritório entende' sem prova de que a posição é institucional.

## 6. Registro no projeto

Fontes efetivamente utilizadas devem ser registradas no `SOURCE_REGISTRY.jsonl` quando houver função de rastreabilidade.

Tipos recomendados:
- `doutrina_autoral`;
- `producao_academica`;
- `posicao_institucional_oab`;
- `producao_comissao_oab`;
- `autoria_individual_ambiente_oab`;
- `tese_institucional_nao_governamental`;
- `doutrina_profissional_especializada`;
- `posicao_institucional_interessada`.

Não criar JSON narrativo paralelo ao conteúdo.

## 7. Entrega mínima por Estratégia Autônoma

Quando materialmente aplicável, a fase de doutrina deve produzir uma matriz com:
- questão jurídica;
- tese;
- autor/instituição;
- categoria da fonte;
- documento e data;
- fundamento resumido;
- posição oposta ou ressalva;
- relação com legislação;
- relação com jurisprudência;
- estado atual da tese;
- link/identificador recuperável.

## 8. Publicação

A área pública `Doutrina` pode apresentar as categorias de fontes e teses materialmente relevantes, mas:
- não publica rankings promocionais;
- não anuncia 'melhores escritórios' ou 'melhores faculdades' como conclusão própria;
- identifica autoria e natureza da fonte;
- explicita quando uma posição não é vinculante;
- preserva divergências relevantes;
- separa doutrina de legislação e jurisprudência.

## 9. Gate

Uma pesquisa doutrinária não está metodologicamente concluída quando:
- a tese foi atribuída sem leitura do documento;
- autoria/natureza institucional está ambígua;
- há controvérsia material sem busca da posição oposta;
- a tese ignora precedente ou lei superveniente relevante;
- o prestígio da instituição foi usado como substituto da fundamentação jurídica.