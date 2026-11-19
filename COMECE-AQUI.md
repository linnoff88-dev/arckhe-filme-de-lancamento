# Comece aqui

Você vai fazer um filme de cerca de 30 segundos para o seu negócio. Você conversa, a IA monta, e você decide o que fica.

## Antes de instalar

- **Custo:** o kit é grátis. O plano mais barato com Claude Code, o Pro, custava [US$ 20 por mês](https://claude.com/pricing) em 18/11/2026, no pagamento mensal. No anual, custava US$ 17 por mês, com US$ 200 pagos de uma vez. Confira o valor atual antes de assinar.
- **Cancelar:** a página oficial informa que você pode cancelar quando quiser, em **Settings > Billing > Cancel**. O plano segue ativo até o fim do período pago. Para evitar a próxima cobrança, cancele pelo menos 24 horas antes da renovação.
- **Limite de uso:** todo plano tem limite, e não medimos quanto um filme consome. A página oficial informa uma janela que renova a cada cinco horas na maioria das contas, mais limites semanais nos planos pagos. Se acabar, veja em **Settings > Usage** quando renova, espere e continue na mesma pasta.
- **Programas gratuitos:** a IA pode precisar instalar programas que geram o vídeo, e você aprova antes:
  - **Node.js** roda o programa que monta o filme.
  - **FFmpeg** junta imagem e som no arquivo de vídeo.
  - **Chrome** desenha cada quadro do filme.
  - **Python** mede a música, se você usar uma.
- **Sistemas:** o kit foi testado em Linux. Windows e Mac têm instalação oficial do Claude, mas o kit ainda não foi testado neles.
- **Confira antes de pagar:** o [mínimo oficial do Claude Code](https://code.claude.com/docs/pt/setup) é Windows 10 versão 1809 ou mais nova, ou macOS 13 ou mais novo, com 4 GB de memória, processador x64 ou ARM64 e internet. No Windows, veja em **Configurações > Sistema > Sobre**. No Mac, em **menu Apple > Sobre este Mac**. Esse mínimo vale para o Claude Code e não garante que o filme será gerado.
- **Filme no seu computador:** o mínimo para gerar o filme não foi medido. Numa máquina Linux ARM64 com 118 GB de memória, gerar o exemplo levou cerca de 20 s. Num computador comum leva mais.
- **Faça um teste primeiro:** no Windows e no Mac, antes de personalizar, peça à IA `gere o filme de exemplo sem mudar nada`. Se falhar, copie a mensagem de erro para a IA e tente uma vez. Se não resolver, pare. Não há garantia de que funcione no seu computador.

## Antes de começar, separe

- O nome do negócio e uma frase sobre o que ele faz.
- O problema que ele resolve, contado como você contaria a um amigo.
- Fotos do negócio feitas no celular, ou prints, se você tiver um site ou app.
- Números, só se você tiver e puder provar.
- O logo oficial, em boa qualidade.
- Música é opcional: o filme pode sair sem música, só com efeitos. Veja [AVISOS.md](AVISOS.md).

## O caminho, em 9 passos

1. **Instale e abra a pasta do kit.**
   - **Windows ou Mac (ainda sem teste com o kit):** baixe o app Claude na [página oficial](https://code.claude.com/docs/pt/desktop-quickstart), instale e entre na sua conta. No Windows ele fica no menu Iniciar; no Mac, em Aplicativos.
   - **Assine o plano antes de abrir a aba Code.** Sem plano pago, a aba pede a assinatura.
   - **Baixe o kit:** em https://github.com/inematds/filme-de-lancamento, use o botão **Code** e depois **Download ZIP**. Descompacte o arquivo.
   - **Abra a pasta sem terminal:** no app, clique na aba **Code**. Abaixo da caixa de texto, escolha **Local** e, no controle ao lado, **Open folder…**. O ZIP pode criar uma pasta dentro de outra: escolha a pasta onde aparece o arquivo `COMECE-AQUI.md`.
   - **Linux (testado):** [instale o Claude Code](https://code.claude.com/docs/pt/setup), abra o terminal dentro da pasta do kit e digite `claude`.
2. **Cole o pedido abaixo.** A IA confere o que falta no computador. Quando ela pedir para instalar algo, responda sim se ela disse o que é e para que serve. Se não entender, escreva "explique de forma simples".
3. **Teste antes de personalizar.** Escreva: `gere o filme de exemplo sem mudar nada e me diga onde ele ficou`. Assista ao vídeo. Se falhar, copie o erro para a IA e tente uma vez. Se não resolver, pare aqui, antes de gastar tempo com a sua história.
4. **Conte a história.** Escreva para a IA: `siga o arquivo prompts/P1`. Você não precisa abrir nenhum arquivo `.md`: ela lê o arquivo e pergunta o que falta.
5. **Entregue o que é real.** Escreva: `siga o arquivo prompts/P2`.
6. **Olhe as imagens paradas.** Escreva: `siga o arquivo prompts/P3`. Corrigir aqui é rápido. Se quiser o filme em pé, para WhatsApp e Instagram, peça 1080x1920. Essa opção ainda não foi testada no kit.
7. **Peça ritmo, sons e sua marca.** Escreva, um de cada vez: `siga o arquivo prompts/P4`, `siga o arquivo prompts/P5` e `siga o arquivo prompts/P7`. No P7, a IA troca a marca e mostra as imagens paradas. Confira com o [checklist antes de gerar](checklists/antes-de-renderizar.md) e aprove. Só então ela gera o vídeo.
8. **Assista e corrija por segundo.** O filme fica em `filme/renders/filme.mp4`. Assista com o [checklist depois de gerar](checklists/depois-de-gerar.md). Para achar o arquivo, peça `abra a pasta onde está o vídeo pronto`. Para corrigir, escreva `siga o arquivo prompts/P6` e diga o que mudar, até gostar.
9. **Passe para o celular.** Abra o [WhatsApp Web](https://web.whatsapp.com/) e envie o arquivo para você mesmo, ou mande por e-mail como anexo. Depois baixe no celular. O filme sai deitado; o formato em pé, 1080x1920, ainda não foi testado no kit.

## O pedido para colar

```text
Leia o COMECE-AQUI.md e a pasta prompts/ deste projeto. Depois me explique em linguagem
simples como vamos fazer um filme de lançamento de cerca de 30 segundos para o meu negócio.
Confira o que falta instalar usando a seção de instalação técnica do README e peça minha
aprovação antes de instalar. Faça uma pergunta por vez sobre o negócio, o problema que ele
resolve e as fotos, telas e números reais que eu tenho. Não mude nenhum arquivo antes do meu
sim. Não publique nem envie nada. Converse comigo em português.
```

## Se travar

Copie a frase, troque o que está entre colchetes e envie para a IA.

- **Erro de instalação:** `Deu este erro ao instalar: [cole o erro]. Explique em palavras simples e tente resolver uma vez.`
- **Permissão do sistema:** `O sistema pediu esta permissão: [o que apareceu]. Para que serve? Preciso aceitar?`
- **Programa não encontrado:** `O programa [nome] foi instalado, mas você não o encontra. Confira onde ele está e tente de novo uma vez.`
- **Limite de uso:** espere a renovação indicada em **Settings > Usage**, abra a mesma pasta e escreva `continue de onde paramos`.

Se a mesma falha voltar depois de uma tentativa, pare. Não continue pagando só para insistir.

## Exemplo fictício: um salão só com fotos

O Salão da Rua é um nome inventado para este exemplo. Ele não tem app nem números. A dona tira fotos do espaço e de um corte pronto com o celular e conta o problema: a cliente quer horário no fim do dia e não sabe que agora o salão abre até mais tarde. O filme mostra essa cena, as fotos reais, o novo horário e o contato.

## Como lidar com arquivos e campos

- **Fotos, prints e logo:** você não precisa criar pastas. No app, arraste os arquivos para a conversa ou use o botão **+** ao lado da caixa de texto. Se não conseguir anexar, diga à IA onde eles estão no computador. Depois peça: `organize estes arquivos no projeto`.
- **Pessoas nas fotos:** peça autorização de quem aparece, como clientes e funcionários.
- **Campos entre colchetes:** a IA pergunta o que precisa. Não sabe o caminho de um arquivo, o código de uma cor ou o que é BPM? Escreva "não sei" ou "o laranja da fachada".
- **Música, se usar:** o método mede arquivos WAV, um tipo de arquivo de áudio. Se a sua vier em outro formato, peça para a IA converter.

## Três regras que evitam retrabalho

- **Só mostre o que existe.** Foto, tela ou número inventado fica fora.
- **Confira parado antes de animar.** Um quadro errado aparece melhor quando nada se mexe.
- **Peça por segundo.** "No segundo 12, o título está cortado; suba o título" funciona melhor que "melhora isso".

## Antes de mostrar a alguém

Passe pelo [checklist de envio](checklists/antes-de-enviar.md). A música do exemplo é só para uso não comercial: no seu negócio, tire a música ou troque por outra. Os detalhes estão em [AVISOS.md](AVISOS.md).

Quer fazer um filme para o negócio de outra pessoa? Leia o [método da amostra](amostra/METODO-DA-AMOSTRA.md).
