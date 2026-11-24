# Filme por conversa

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Filme por conversa: seu filme de lanÃ§amento feito sÃ³ conversando com a IA](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

VocÃª tem um negÃ³cio bom e nenhum vÃ­deo que mostre isso. O **filme por conversa** Ã© um kit grÃ¡tis e aberto para fazer um filme de lanÃ§amento de cerca de 30 segundos, sem programa de ediÃ§Ã£o, conversando em portuguÃªs com o Claude Code, uma IA que cria arquivos no seu computador. Serve para quem tem um pequeno negÃ³cio, procura trabalho ou quer uma renda extra e nunca editou vÃ­deo. VocÃª precisa de um computador, de um plano pago do Claude e de fotos do negÃ³cio feitas no celular; nÃºmeros, sÃ³ se tiver. A IA confere o que falta instalar.

**O que precisa:** computador e plano pago do Claude. O kit Ã© grÃ¡tis; o plano mais barato com Claude Code, o Pro, custava [US$ 20 por mÃªs](https://claude.com/pricing) em 18/11/2026, no pagamento mensal. Todo plano tem limite de uso, e nÃ£o medimos quanto um filme consome. **Testado em Linux; Windows e Mac ainda sem teste.** Nesses sistemas, confira o [mÃ­nimo oficial do Claude Code](https://code.claude.com/docs/pt/setup), que nÃ£o garante o filme, e teste primeiro com o filme de exemplo.

**Programas gratuitos:** a IA pode precisar instalar Node.js, que roda o programa que monta o filme; FFmpeg, que junta imagem e som; Chrome, que desenha cada quadro; e Python, que mede a mÃºsica, se vocÃª usar uma. VocÃª aprova antes.

## ðŸ“– Guia de uso

Guia completo, sem termos tÃ©cnicos: **https://linnoff88-dev.github.io/

Primeira vez? Abra o [COMECE-AQUI.md](COMECE-AQUI.md).

## PeÃ§a para a IA comeÃ§ar

Abra o Claude Code nesta pasta e cole:

```text
Leia o COMECE-AQUI.md e a pasta prompts/ deste projeto. Depois me explique em linguagem
simples como vamos fazer um filme de lanÃ§amento de cerca de 30 segundos para o meu negÃ³cio.
Confira o que falta instalar usando a seÃ§Ã£o de instalaÃ§Ã£o tÃ©cnica do README e peÃ§a minha
aprovaÃ§Ã£o antes de instalar. FaÃ§a uma pergunta por vez sobre o negÃ³cio, o problema que ele
resolve e as fotos, telas e nÃºmeros reais que eu tenho. NÃ£o mude nenhum arquivo antes do meu
sim. NÃ£o publique nem envie nada. Converse comigo em portuguÃªs.
```

Depois, basta pedir `siga o arquivo prompts/P1`, e assim por diante. VocÃª nÃ£o precisa abrir os arquivos.

## O que tem aqui

| Pasta ou arquivo | Para que serve |
|---|---|
| [COMECE-AQUI.md](COMECE-AQUI.md) | O caminho curto para quem nunca editou vÃ­deo |
| [prompts/](prompts/) | P1 a P7, os pedidos para colar na IA, com os campos explicados |
| [amostra/METODO-DA-AMOSTRA.md](amostra/METODO-DA-AMOSTRA.md) | Como fazer um filme curto para um negÃ³cio e mostrar sÃ³ ao dono |
| [checklists/](checklists/) | O que conferir antes de gerar, depois de gerar e antes de enviar |
| [filme/](filme/) | O filme de exemplo, editÃ¡vel |
| [ferramentas/mapa_batidas.py](ferramentas/mapa_batidas.py) | Mede a mÃºsica e aponta onde cortar |
| [guia/](guia/) | A pÃ¡gina do projeto em portuguÃªs, inglÃªs e espanhol |
| [AVISOS.md](AVISOS.md) | LicenÃ§as de terceiros e limites de uso da trilha e da marca |

## O filme de exemplo

O exemplo fala do prÃ³prio ARCKHÉ AI: [`guia/assets/filme-ARCKHÉ.mp4`](guia/assets/filme-ARCKHÉ.mp4). SÃ£o 28,9 s em 1920x1080, a 30 quadros por segundo, com 7 cenas, mÃºsica e efeitos.

---

## O processo, do inÃ­cio ao fim

ðŸ§  = sessÃ£o com a pessoa Â· âš™ï¸ = script Â· ðŸ¤– = IA

Rode os comandos âš™ï¸ dentro da pasta indicada. Os pedidos ðŸ¤– sÃ£o colados no Claude Code, aberto na raiz do projeto.

| # | Passo | Comando ou pedido | Quem |
|---|---|---|---|
| 1 | Contar o negÃ³cio, o pÃºblico e o problema | conversa inicial do [COMECE-AQUI.md](COMECE-AQUI.md) | ðŸ§  |
| 2 | Escrever a histÃ³ria do problema | [P1](prompts/P1-historia-do-problema.md) | ðŸ¤– + ðŸ§  aprova |
| 3 | Juntar fotos, telas e nÃºmeros reais | [P2](prompts/P2-telas-e-numeros-reais.md) | ðŸ§  entrega, ðŸ¤– organiza |
| 4 | Montar as cenas como imagens paradas | [P3](prompts/P3-imagens-paradas.md) | ðŸ¤– |
| 5 | Gerar os quadros para conferir | na pasta `filme/`: `npx hyperframes@0.8.77 snapshot . --at 2,9,17` | âš™ï¸ |
| 6 | Aprovar os quadros | abrir `filme/snapshots/` e dizer o que muda | ðŸ§  |
| 7 | Medir a mÃºsica, se houver | na raiz: `python3 ferramentas/mapa_batidas.py filme/assets/audio/trilha.wav` (troque pelo arquivo da sua mÃºsica) | âš™ï¸ |
| 8 | Animar e cortar na batida | [P4](prompts/P4-musica-e-batida.md) | ðŸ¤– |
| 9 | PÃ´r sons sÃ³ nas aÃ§Ãµes visÃ­veis | [P5](prompts/P5-sons-nas-acoes.md) | ðŸ¤– |
| 10 | Trocar o que ainda Ã© do exemplo pela sua marca e mostrar as imagens paradas | [P7](prompts/P7-sua-marca.md) | ðŸ¤– + ðŸ§  entrega o logo |
| 11 | Conferir e aprovar as imagens | [checklist antes de gerar](checklists/antes-de-renderizar.md) e, em `filme/`: `npx hyperframes@0.8.77 check` | âš™ï¸ + ðŸ§  |
| 12 | Gerar o vÃ­deo depois da aprovaÃ§Ã£o | em `filme/`: `npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30` | âš™ï¸ |
| 13 | Assistir e pedir correÃ§Ãµes por segundo | [checklist depois de gerar](checklists/depois-de-gerar.md) e [P6](prompts/P6-revisao-por-segundo.md); depois volte ao passo 11 | ðŸ§  + ðŸ¤– |
| 14 | Conferir antes de mostrar a alguÃ©m | [checklist](checklists/antes-de-enviar.md) | ðŸ§  |
| 15 | Fazer para outro negÃ³cio, se quiser | [mÃ©todo da amostra](amostra/METODO-DA-AMOSTRA.md) | ðŸ§  |

P6 vem depois de P7 porque a revisÃ£o olha o filme jÃ¡ gerado com a sua marca.

## InstalaÃ§Ã£o tÃ©cnica

### O que precisa

- **Claude Code**, incluÃ­do nos [planos pagos do Claude](https://claude.com/pricing). No Windows e no Mac, use o [app Claude](https://code.claude.com/docs/pt/desktop-quickstart), aba **Code**, **Local** e **Open folderâ€¦**. No Linux, use a [instalaÃ§Ã£o oficial](https://code.claude.com/docs/pt/setup). O render Ã© local; o custo Ã© o plano da IA.
- **Node.js** com `npx`. Testado com a versÃ£o 24.22.3.
- **FFmpeg e FFprobe**. Testado com a versÃ£o 6.1.1.
- **Chrome para render**. Rode `npx hyperframes@0.8.77 doctor` em `filme/` para ver o que falta. Ele tambÃ©m avisa que existe versÃ£o mais nova do HyperFrames; este kit fica fixo na 0.8.77 para o filme sair igual.
- **Python 3 com `numpy` e `scipy`**, sÃ³ para medir a mÃºsica.

Testado em Linux ARM64. Windows e Mac nÃ£o foram testados com o kit. O mÃ­nimo oficial do Claude Code Ã© Windows 10 versÃ£o 1809 ou macOS 13, com 4 GB de memÃ³ria, processador x64 ou ARM64 e internet. Isso nÃ£o garante o filme: o mÃ­nimo para gerÃ¡-lo nÃ£o foi medido.

### Rodar o filme de exemplo

```bash
cd filme
npx hyperframes@0.8.77 check
npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30
```

O resultado fica em `filme/renders/filme.mp4`. O render levou cerca de 20 s nesta mÃ¡quina, com Linux ARM64 e 118 GB de memÃ³ria. Num computador comum leva mais.

O kit usa 1920x1080 por padrÃ£o. Para WhatsApp e Instagram, peÃ§a 1080x1920 no [P3](prompts/P3-imagens-paradas.md). Esse formato ainda nÃ£o foi testado no kit.

### Como funciona por dentro

Cada cena Ã© uma pÃ¡gina HTML em `filme/compositions/`, animada com GSAP. O `filme/index.html` diz quando cada cena, mÃºsica e efeito entra. O HyperFrames 0.8.77 abre tudo num navegador sem janela, grava quadro a quadro e entrega o MP4.

| Cena | Arquivo | ComeÃ§a em | O que faz |
|---|---|---|---|
| 1 | `pilha.html` | 0 s | VÃ­deos salvos se empilham |
| 2 | `queda.html` | 4,288 s | A pilha cai: "O depois nÃ£o chegou." |
| 3 | `barras.html` | 8,896 s | A virada: "Aprenda. Pratique. Evolua." |
| 4 | `busca.html` | 11,968 s | Busca real no catÃ¡logo |
| 5 | `parede.html` | 17,088 s | Parede de cursos e o nÃºmero 385 |
| 6 | `promessa.html` | 23,232 s | "GrÃ¡tis. Direto na internet." |
| 7 | `marca.html` | 25,28 s | Logo e pergunta final |

### Os nÃºmeros do exemplo

- Trilha: 117,2 BPM, uma batida a cada 0,512 s, medida por `ferramentas/mapa_batidas.py`. As viradas caem em 8,896 s e 17,088 s.
- Busca em [ARCKHÉ AI/cursos](https://www.ARCKHÉ AI/cursos/), em 18/11/2026: "criar vÃ­deo com IA" deu 0 cursos; "vÃ­deo" deu 53. O catÃ¡logo tinha 385 fichas de curso.
- A revisÃ£o por quadros parados pegou dois erros: o primeiro quadro com metade da tela vazia e os resultados em ordem diferente da do site.

## LicenÃ§a

CÃ³digo e textos deste kit: [MIT](LICENSE). A trilha do exemplo Ã© sÃ³ para uso nÃ£o comercial, e hÃ¡ outras exceÃ§Ãµes em [AVISOS.md](AVISOS.md). Leia antes de usar o filme num negÃ³cio.

---

Feito pelo [ARCKHÉ AI](https://ARCKHÉ AI).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>