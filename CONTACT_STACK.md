# Stack do Fale Conosco — Ações Judiciais

## Estado

**FORMINIT CONFIGURADO / EMAILJS PENDENTE**

O FormSubmit foi removido da camada pública. O frontend já usa a stack canônica Forminit + EmailJS.

## Padrão canônico aprovado

- e-mail institucional: `acoesjudiciais2026@gmail.com`;
- prefixo de protocolo: `AJ-`;
- recebimento e anexos: **Forminit**;
- confirmação do protocolo ao remetente: **EmailJS**;
- referência funcional: Fale Conosco do Site Classe e Massas.

## Regra de recebimento

1. gerar protocolo no cliente;
2. enviar protocolo e conteúdo ao Forminit;
3. somente após resposta de sucesso do Forminit considerar a submissão recebida;
4. se houver e-mail de retorno, acionar EmailJS;
5. redirecionar para página de confirmação com o protocolo;
6. distinguir sucesso do protocolo de eventual falha no e-mail.

## Configuração exigida antes do teste

- Forminit próprio do projeto criado;
- `FORM_ID`: `lprwcdbax4y`;
- Authentication mode: `Public`;
- notificação de recebimento destinada a `acoesjudiciais2026@gmail.com`;
- configurar EmailJS para envio ao e-mail informado pelo visitante;
- registrar `SERVICE_ID`, `TEMPLATE_ID` e chave pública quando aplicável;
- não reutilizar FORM_ID do Classe e Massas sem comprovar isolamento.

## Gate end-to-end

O canal só pode ser declarado operacional depois de teste real que comprove:
- recebimento no backend;
- protocolo idêntico na submissão e na confirmação;
- chegada do protocolo ao e-mail de retorno;
- comportamento sem e-mail;
- falha do e-mail sem invalidação do protocolo;
- anexos, se publicados.


## Bloqueio externo comprovado

O frontend já segue a lógica Forminit + EmailJS. A ativação pública depende de configuração autenticada nos painéis dos provedores:

- Forminit próprio já criado em modo Public, com `FORM_ID lprwcdbax4y`;
- notificação de recebimento apontada para `acoesjudiciais2026@gmail.com`;
- criar ou validar serviço/template EmailJS e obter Service ID, Template ID e Public Key;
- inserir os quatro identificadores no frontend;
- executar teste end-to-end real.

Enquanto os identificadores do EmailJS não existirem, o formulário permanece oculto e o e-mail institucional direto continua disponível.


## Limite de formulários da conta

Em 20/09/2026, ao tentar criar o formulário isolado **Fale Conosco — Ações Judiciais**, o painel Forminit exibiu: “You have reached your form limit. Please increase your package to add more.”

A tabela pública do Forminit informa:
- Free: 1 formulário;
- Pro: 5 formulários;
- Business: 15 formulários;
- Volume: sem limite de formulários.

O formulário do Classe e Massas não deve ser apagado nem reutilizado para este projeto apenas para contornar o limite. A solução precisa preservar isolamento entre projetos.


## Correção do bloqueio por limite de conta

O alerta de limite registrado anteriormente ocorreu porque a tentativa foi feita na conta Forminit já utilizada pelo Classe e Massas.

Em seguida, o usuário entrou com o e-mail próprio do projeto Ações Judiciais e criou com sucesso o formulário isolado:

- nome: **Fale Conosco — Ações Judiciais**;
- Form ID: `lprwcdbax4y`;
- endpoint exibido: `/f/lprwcdbax4y`;
- Authentication mode: **Public**;
- destinatário da notificação: `acoesjudiciais2026@gmail.com`.

Portanto, o estado `BLOQUEADA_POR_LIMITE_DE_CONTA_FORMINIT` está superado.
