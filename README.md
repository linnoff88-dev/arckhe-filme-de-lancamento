# Filme por conversa

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Filme por conversa: seu filme de lanêÂ§amento feito sêÂ³ conversando com a IA](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

VocêÂª tem um negêÂ³cio bom e nenhum vêÂ­deo que mostre isso. O **filme por conversa** êÂ© um kit grêÂ¡tis e aberto para fazer um filme de lanêÂ§amento de cerca de 30 segundos, sem programa de ediêÂ§êÂ£o, conversando em portuguêÂªs com o Claude Code, uma IA que cria arquivos no seu computador. Serve para quem tem um pequeno negêÂ³cio, procura trabalho ou quer uma renda extra e nunca editou vêÂ­deo. VocêÂª precisa de um computador, de um plano pago do Claude e de fotos do negêÂ³cio feitas no celular; nêÂºmeros, sêÂ³ se tiver. A IA confere o que falta instalar.

**O que precisa:** computador e plano pago do Claude. O kit êÂ© grêÂ¡tis; o plano mais barato com Claude Code, o Pro, custava [US$ 20 por mêÂªs](https://claude.com/pricing) em 18/11/2026, no pagamento mensal. Todo plano tem limite de uso, e nêÂ£o medimos quanto um filme consome. **Testado em Linux; Windows e Mac ainda sem teste.** Nesses sistemas, confira o [mêÂ­nimo oficial do Claude Code](https://code.claude.com/docs/pt/setup), que nêÂ£o garante o filme, e teste primeiro com o filme de exemplo.

**Programas gratuitos:** a IA pode precisar instalar Node.js, que roda o programa que monta o filme; FFmpeg, que junta imagem e som; Chrome, que desenha cada quadro; e Python, que mede a mêÂºsica, se vocêÂª usar uma. VocêÂª aprova antes.

## ê°Å¸ââ Guia de uso

Guia completo, sem termos têÂ©cnicos: **https://linnoff88-dev.github.io/

Primeira vez? Abra o [COMECE-AQUI.md](COMECE-AQUI.md).

## PeêÂ§a para a IA comeêÂ§ar

Abra o Claude Code nesta pasta e cole:

```text
Leia o COMECE-AQUI.md e a pasta prompts/ deste projeto. Depois me explique em linguagem
simples como vamos fazer um filme de lanêÂ§amento de cerca de 30 segundos para o meu negêÂ³cio.
Confira o que falta instalar usando a seêÂ§êÂ£o de instalaêÂ§êÂ£o têÂ©cnica do README e peêÂ§a minha
aprovaêÂ§êÂ£o antes de instalar. FaêÂ§a uma pergunta por vez sobre o negêÂ³cio, o problema que ele
resolve e as fotos, telas e nêÂºmeros reais que eu tenho. NêÂ£o mude nenhum arquivo antes do meu
sim. NêÂ£o publique nem envie nada. Converse comigo em portuguêÂªs.
```

Depois, basta pedir `siga o arquivo prompts/P1`, e assim por diante. VocêÂª nêÂ£o precisa abrir os arquivos.

## O que tem aqui

| Pasta ou arquivo | Para que serve |
|---|---|
| [COMECE-AQUI.md](COMECE-AQUI.md) | O caminho curto para quem nunca editou vêÂ­deo |
| [prompts/](prompts/) | P1 a P7, os pedidos para colar na IA, com os campos explicados |
| [amostra/METODO-DA-AMOSTRA.md](amostra/METODO-DA-AMOSTRA.md) | Como fazer um filme curto para um negêÂ³cio e mostrar sêÂ³ ao dono |
| [checklists/](checklists/) | O que conferir antes de gerar, depois de gerar e antes de enviar |
| [filme/](filme/) | O filme de exemplo, editêÂ¡vel |
| [ferramentas/mapa_batidas.py](ferramentas/mapa_batidas.py) | Mede a mêÂºsica e aponta onde cortar |
| [guia/](guia/) | A pêÂ¡gina do projeto em portuguêÂªs, inglêÂªs e espanhol |
| [AVISOS.md](AVISOS.md) | LicenêÂ§as de terceiros e limites de uso da trilha e da marca |

## O filme de exemplo

O exemplo fala do prêÂ³prio ARCKHê AI: [`guia/assets/filme-ARCKHê.mp4`](guia/assets/filme-ARCKHê.mp4). SêÂ£o 28,9 s em 1920x1080, a 30 quadros por segundo, com 7 cenas, mêÂºsica e efeitos.

---

## O processo, do inêÂ­cio ao fim

ê°Å¸Â§Â  = sessêÂ£o com a pessoa êÂ· ê¢Å¡â¢ê¯Â¸Â = script êÂ· ê°Å¸Â¤â = IA

Rode os comandos ê¢Å¡â¢ê¯Â¸Â dentro da pasta indicada. Os pedidos ê°Å¸Â¤â sêÂ£o colados no Claude Code, aberto na raiz do projeto.

| # | Passo | Comando ou pedido | Quem |
|---|---|---|---|
| 1 | Contar o negêÂ³cio, o pêÂºblico e o problema | conversa inicial do [COMECE-AQUI.md](COMECE-AQUI.md) | ê°Å¸Â§Â  |
| 2 | Escrever a histêÂ³ria do problema | [P1](prompts/P1-historia-do-problema.md) | ê°Å¸Â¤â + ê°Å¸Â§Â  aprova |
| 3 | Juntar fotos, telas e nêÂºmeros reais | [P2](prompts/P2-telas-e-numeros-reais.md) | ê°Å¸Â§Â  entrega, ê°Å¸Â¤â organiza |
| 4 | Montar as cenas como imagens paradas | [P3](prompts/P3-imagens-paradas.md) | ê°Å¸Â¤â |
| 5 | Gerar os quadros para conferir | na pasta `filme/`: `npx hyperframes@0.8.77 snapshot . --at 2,9,17` | ê¢Å¡â¢ê¯Â¸Â |
| 6 | Aprovar os quadros | abrir `filme/snapshots/` e dizer o que muda | ê°Å¸Â§Â  |
| 7 | Medir a mêÂºsica, se houver | na raiz: `python3 ferramentas/mapa_batidas.py filme/assets/audio/trilha.wav` (troque pelo arquivo da sua mêÂºsica) | ê¢Å¡â¢ê¯Â¸Â |
| 8 | Animar e cortar na batida | [P4](prompts/P4-musica-e-batida.md) | ê°Å¸Â¤â |
| 9 | PêÂ´r sons sêÂ³ nas aêÂ§êÂµes visêÂ­veis | [P5](prompts/P5-sons-nas-acoes.md) | ê°Å¸Â¤â |
| 10 | Trocar o que ainda êÂ© do exemplo pela sua marca e mostrar as imagens paradas | [P7](prompts/P7-sua-marca.md) | ê°Å¸Â¤â + ê°Å¸Â§Â  entrega o logo |
| 11 | Conferir e aprovar as imagens | [checklist antes de gerar](checklists/antes-de-renderizar.md) e, em `filme/`: `npx hyperframes@0.8.77 check` | ê¢Å¡â¢ê¯Â¸Â + ê°Å¸Â§Â  |
| 12 | Gerar o vêÂ­deo depois da aprovaêÂ§êÂ£o | em `filme/`: `npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30` | ê¢Å¡â¢ê¯Â¸Â |
| 13 | Assistir e pedir correêÂ§êÂµes por segundo | [checklist depois de gerar](checklists/depois-de-gerar.md) e [P6](prompts/P6-revisao-por-segundo.md); depois volte ao passo 11 | ê°Å¸Â§Â  + ê°Å¸Â¤â |
| 14 | Conferir antes de mostrar a alguêÂ©m | [checklist](checklists/antes-de-enviar.md) | ê°Å¸Â§Â  |
| 15 | Fazer para outro negêÂ³cio, se quiser | [mêÂ©todo da amostra](amostra/METODO-DA-AMOSTRA.md) | ê°Å¸Â§Â  |

P6 vem depois de P7 porque a revisêÂ£o olha o filme jêÂ¡ gerado com a sua marca.

## InstalaêÂ§êÂ£o têÂ©cnica

### O que precisa

- **Claude Code**, incluêÂ­do nos [planos pagos do Claude](https://claude.com/pricing). No Windows e no Mac, use o [app Claude](https://code.claude.com/docs/pt/desktop-quickstart), aba **Code**, **Local** e **Open folderê¢â¬Â¦**. No Linux, use a [instalaêÂ§êÂ£o oficial](https://code.claude.com/docs/pt/setup). O render êÂ© local; o custo êÂ© o plano da IA.
- **Node.js** com `npx`. Testado com a versêÂ£o 24.22.3.
- **FFmpeg e FFprobe**. Testado com a versêÂ£o 6.1.1.
- **Chrome para render**. Rode `npx hyperframes@0.8.77 doctor` em `filme/` para ver o que falta. Ele tambêÂ©m avisa que existe versêÂ£o mais nova do HyperFrames; este kit fica fixo na 0.8.77 para o filme sair igual.
- **Python 3 com `numpy` e `scipy`**, sêÂ³ para medir a mêÂºsica.

Testado em Linux ARM64. Windows e Mac nêÂ£o foram testados com o kit. O mêÂ­nimo oficial do Claude Code êÂ© Windows 10 versêÂ£o 1809 ou macOS 13, com 4 GB de memêÂ³ria, processador x64 ou ARM64 e internet. Isso nêÂ£o garante o filme: o mêÂ­nimo para gerêÂ¡-lo nêÂ£o foi medido.

### Rodar o filme de exemplo

```bash
cd filme
npx hyperframes@0.8.77 check
npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30
```

O resultado fica em `filme/renders/filme.mp4`. O render levou cerca de 20 s nesta mêÂ¡quina, com Linux ARM64 e 118 GB de memêÂ³ria. Num computador comum leva mais.

O kit usa 1920x1080 por padrêÂ£o. Para WhatsApp e Instagram, peêÂ§a 1080x1920 no [P3](prompts/P3-imagens-paradas.md). Esse formato ainda nêÂ£o foi testado no kit.

### Como funciona por dentro

Cada cena êÂ© uma pêÂ¡gina HTML em `filme/compositions/`, animada com GSAP. O `filme/index.html` diz quando cada cena, mêÂºsica e efeito entra. O HyperFrames 0.8.77 abre tudo num navegador sem janela, grava quadro a quadro e entrega o MP4.

| Cena | Arquivo | ComeêÂ§a em | O que faz |
|---|---|---|---|
| 1 | `pilha.html` | 0 s | VêÂ­deos salvos se empilham |
| 2 | `queda.html` | 4,288 s | A pilha cai: "O depois nêÂ£o chegou." |
| 3 | `barras.html` | 8,896 s | A virada: "Aprenda. Pratique. Evolua." |
| 4 | `busca.html` | 11,968 s | Busca real no catêÂ¡logo |
| 5 | `parede.html` | 17,088 s | Parede de cursos e o nêÂºmero 385 |
| 6 | `promessa.html` | 23,232 s | "GrêÂ¡tis. Direto na internet." |
| 7 | `marca.html` | 25,28 s | Logo e pergunta final |

### Os nêÂºmeros do exemplo

- Trilha: 117,2 BPM, uma batida a cada 0,512 s, medida por `ferramentas/mapa_batidas.py`. As viradas caem em 8,896 s e 17,088 s.
- Busca em [ARCKHê AI/cursos](https://www.ARCKHê AI/cursos/), em 18/11/2026: "criar vêÂ­deo com IA" deu 0 cursos; "vêÂ­deo" deu 53. O catêÂ¡logo tinha 385 fichas de curso.
- A revisêÂ£o por quadros parados pegou dois erros: o primeiro quadro com metade da tela vazia e os resultados em ordem diferente da do site.

## LicenêÂ§a

CêÂ³digo e textos deste kit: [MIT](LICENSE). A trilha do exemplo êÂ© sêÂ³ para uso nêÂ£o comercial, e hêÂ¡ outras exceêÂ§êÂµes em [AVISOS.md](AVISOS.md). Leia antes de usar o filme num negêÂ³cio.

---

Feito pelo [ARCKHê AI](https://ARCKHê AI).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>