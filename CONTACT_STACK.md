# Stack do Fale Conosco — Ações Judiciais

## Estado

**FORMINIT + EMAILJS CONFIGURADOS / TESTE E2E PENDENTE**

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
- Self-email notification: `Active`;
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


## Self-email notification ativada

A captura subsequente do painel Actions mostrou **Self-email notification — Active**, confirmando a ativação da notificação administrativa do Forminit.


## EmailJS Service criado

Em 20/09/2026, foi criado o serviço Gmail isolado do projeto:

- nome: **Gmail — Ações Judiciais**;
- Service ID: `service_3dyw7gl`;
- conta conectada: `acoesjudiciais2026@gmail.com`;
- estado no painel: serviço criado e marcado como **DEFAULT**.

O teste end-to-end ainda não está concluído. Permanecem pendentes:
- criação do template de confirmação de protocolo;
- obtenção do Template ID;
- obtenção da Public Key;
- inserção dos identificadores no frontend;
- teste real de recebimento + confirmação por e-mail.


## EmailJS Template e Public Key configurados

Em 20/09/2026, a configuração do EmailJS foi completada com:

- Service ID: `service_3dyw7gl`;
- Template: **Confirmação de Protocolo — Ações Judiciais**;
- Template ID: `template_jz6al72`;
- Public Key: `bRDjSNFb96VvEUPvx`;
- variáveis do template: `to_email`, `protocolo`, `registro`, `projeto`.

A Public Key é um identificador público de cliente usado pelo SDK no navegador. Não é tratada como segredo de backend.

O próximo gate é o teste end-to-end real:
1. submissão pelo Site;
2. confirmação de sucesso do Forminit;
3. exibição do mesmo protocolo na página de recibo;
4. chegada da notificação administrativa ao Gmail institucional;
5. chegada da confirmação de protocolo ao e-mail informado pelo visitante.


## Teste real de 20/09/2026

Foi executada uma submissão real pelo Site.

Evidências observadas:
- protocolo público: `AJ-20260920-164456-E2CFB5`;
- registro técnico devolvido pelo Forminit: `3C3ZU5iSwqLA4Wen`;
- página de confirmação exibiu “Mensagem recebida” somente após sucesso do Forminit;
- a página informou “Confirmação enviada por e-mail”;
- EmailJS History registrou resultado **OK**;
- History ID: `email_BOfGy7keSDe6S2llZi6wjS5r`;
- Service ID: `service_3dyw7gl`;
- Template ID: `template_jz6al72`;
- destinatário informado: `thiagoba2004@yahoo.com.br`;
- parâmetro `protocolo` no EmailJS: `AJ-20260920-164456-E2CFB5`;
- parâmetro `registro`: `3C3ZU5iSwqLA4Wen`;
- parâmetro `projeto`: `Ações Judiciais`.

### Estado do gate

O fluxo técnico **Site → Forminit → registro técnico → EmailJS** está comprovado.

Permanece uma verificação final para o estado `E2E_VERIFICADO`: confirmar a chegada da mensagem na caixa postal do destinatário, não apenas o aceite pelo provedor EmailJS.
