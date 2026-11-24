# Film by Conversation

[![Film by Conversation: your launch film made just by talking with AI](guia/assets/banner-en.jpg)](https://linnoff88-dev.github.io/

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

You have a good business, but no video to show it. **Film by Conversation** is a free, open kit for making a launch film about 30 seconds long. You don’t need editing software. You make it by talking with Claude Code, an AI that creates files on your computer. It’s for people with a small business, people looking for work, or people who want extra income and have never edited video. You need a computer, a paid Claude plan, and photos of your business taken on your phone. Numbers are optional. The AI checks what you need to install.

**What you need:** a computer and a paid Claude plan. The kit is free. As of 18/11/2026, the cheapest plan with Claude Code, Pro, cost [US$ 20 per month](https://claude.com/pricing) with monthly billing. Every plan has usage limits, and we haven’t measured how much usage one film takes. **Tested on Linux; Windows and Mac have not been tested.** On those systems, check the [official Claude Code minimum requirements](https://code.claude.com/docs/en/setup). They don’t guarantee the film will work, so try the sample film first.

**Free programs:** The AI may need to install Node.js, which runs the program that assembles the film; FFmpeg, which combines image and sound; Chrome, which draws each frame; and Python, which measures the music if you use any. You approve each installation first.

## 📖 User guide

Full guide, without technical terms: **https://linnoff88-dev.github.io/

First time? Open [COMECE-AQUI.md](COMECE-AQUI.md).

## Ask the AI to get started

Open Claude Code in this folder and paste:

```text
Read COMECE-AQUI.md and this project's prompts/ folder. Then explain in simple language
how we’ll make a launch film about 30 seconds long for my business.
Check what needs to be installed using the technical setup section of the README, and ask
for my approval before installing anything. Ask one question at a time about my business,
the problem it solves, and the real photos, screens, and numbers I have. Don’t change any
files before I say yes. Don’t publish or send anything. Talk with me in English.
```

The kit's prompts are written in Portuguese, and the AI can walk you through them in English.

After that, just ask `follow the file prompts/P1`, and so on. You don’t need to open the files.

## What’s here

| Folder or file | What it’s for |
|---|---|
| [COMECE-AQUI.md](COMECE-AQUI.md) (in Portuguese) | The short path for people who have never edited video |
| [prompts/](prompts/) (in Portuguese) | P1 to P7, prompts to paste into the AI, with the fields explained |
| [amostra/METODO-DA-AMOSTRA.md](amostra/METODO-DA-AMOSTRA.md) (in Portuguese) | How to make a short film for a business and show it only to its owner |
| [checklists/](checklists/) | What to check before generating, after generating, and before sending |
| [filme/](filme/) | The sample film, ready to edit |
| [ferramentas/mapa_batidas.py](ferramentas/mapa_batidas.py) | Measures the music and points out where to cut |
| [guia/](guia/) | The project page in Portuguese, English, and Spanish |
| [AVISOS.md](AVISOS.md) (in Portuguese) | Third-party licenses and limits on using the soundtrack and brand |

## The sample film

The sample is about ARCKHÉ AI itself: [`guia/assets/filme-ARCKHÉ.mp4`](guia/assets/filme-ARCKHÉ.mp4). It’s 28.9 s long, at 1920x1080 and 30 frames per second, with 7 scenes, music, and sound effects.

---

## The process, from start to finish

🧠 = session with you · ⚙️ = script · 🤖 = AI

Run ⚙️ commands inside the specified folder. Paste 🤖 prompts into Claude Code, opened at the project root.

| # | Step | Command or prompt | Who |
|---|---|---|---|
| 1 | Explain your business, audience, and the problem | The initial conversation in [COMECE-AQUI.md](COMECE-AQUI.md) (in Portuguese) | 🧠 |
| 2 | Write the story of the problem | [P1](prompts/P1-historia-do-problema.md) (in Portuguese) | 🤖 + 🧠 approves |
| 3 | Gather real photos, screens, and numbers | [P2](prompts/P2-telas-e-numeros-reais.md) (in Portuguese) | 🧠 provides, 🤖 organizes |
| 4 | Arrange the scenes as still images | [P3](prompts/P3-imagens-paradas.md) (in Portuguese) | 🤖 |
| 5 | Generate frames to review | In `filme/`: `npx hyperframes@0.8.77 snapshot . --at 2,9,17` | ⚙️ |
| 6 | Approve the frames | Open `filme/snapshots/` and say what to change | 🧠 |
| 7 | Measure the music, if any | From the root: `python3 ferramentas/mapa_batidas.py filme/assets/audio/trilha.wav` (replace with your music file) | ⚙️ |
| 8 | Animate and cut to the beat | [P4](prompts/P4-musica-e-batida.md) (in Portuguese) | 🤖 |
| 9 | Add sounds only to visible actions | [P5](prompts/P5-sons-nas-acoes.md) (in Portuguese) | 🤖 |
| 10 | Replace anything that still belongs to the sample with your brand, and show the still images | [P7](prompts/P7-sua-marca.md) (in Portuguese) | 🤖 + 🧠 provides the logo |
| 11 | Review and approve the images | [Checklist before generating](checklists/antes-de-renderizar.md) (in Portuguese) and, in `filme/`: `npx hyperframes@0.8.77 check` | ⚙️ + 🧠 |
| 12 | Generate the video after approval | In `filme/`: `npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30` | ⚙️ |
| 13 | Watch it and request corrections by second | [Checklist after generating](checklists/depois-de-gerar.md) (in Portuguese) and [P6](prompts/P6-revisao-por-segundo.md) (in Portuguese); then return to step 11 | 🧠 + 🤖 |
| 14 | Review it before showing anyone | [Checklist](checklists/antes-de-enviar.md) (in Portuguese) | 🧠 |
| 15 | Make one for another business, if you want | [Sample method](amostra/METODO-DA-AMOSTRA.md) (in Portuguese) | 🧠 |

P6 comes after P7 because the review looks at the film generated with your brand.

## Technical setup

### What you need

- **Claude Code**, included in [paid Claude plans](https://claude.com/pricing). On Windows and Mac, use the [Claude app](https://code.claude.com/docs/en/desktop-quickstart), the **Code** tab, **Local**, and **Open folder…**. On Linux, use the [official installation](https://code.claude.com/docs/en/setup). Rendering happens on your computer; the cost is your AI plan.
- **Node.js** with `npx`. Tested with version 24.22.3.
- **FFmpeg and FFprobe**. Tested with version 6.1.1.
- **Chrome for rendering**. Run `npx hyperframes@0.8.77 doctor` in `filme/` to see what’s missing. It also says when a newer version of HyperFrames is available. This kit stays on 0.8.77 so the film comes out the same way.
- **Python 3 with `numpy` and `scipy`**, only to measure the music.

Tested on Linux ARM64. Windows and Mac have not been tested with the kit. The official Claude Code minimum requirements are Windows 10 version 1809 or macOS 13, with 4 GB of memory, an x64 or ARM64 processor, and internet access. That doesn’t guarantee the film will work. The minimum requirements for generating it haven’t been measured.

### Run the sample film

```bash
cd filme
npx hyperframes@0.8.77 check
npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30
```

The result is saved in `filme/renders/filme.mp4`. Rendering took about 20 s on this machine, with Linux ARM64 and 118 GB of memory. It takes longer on a typical computer.

The kit uses 1920x1080 by default. For WhatsApp and Instagram, ask for 1080x1920 in [P3](prompts/P3-imagens-paradas.md). This format has not been tested with the kit.

### How it works inside

Each scene is an HTML page in `filme/compositions/`, animated with GSAP. `filme/index.html` says when each scene, the music, and each sound effect starts. HyperFrames 0.8.77 opens everything in a browser without a window, records it frame by frame, and creates the MP4.

| Scene | File | Starts at | What it does |
|---|---|---|---|
| 1 | `pilha.html` | 0 s | Saved videos stack up |
| 2 | `queda.html` | 4.288 s | The stack falls: "The after never came." |
| 3 | `barras.html` | 8.896 s | The turning point: "Learn. Practice. Evolve." |
| 4 | `busca.html` | 11.968 s | Real search in the catalog |
| 5 | `parede.html` | 17.088 s | Wall of courses and the number 385 |
| 6 | `promessa.html` | 23.232 s | "Free. Right on the internet." |
| 7 | `marca.html` | 25.28 s | Logo and final question |

### The sample’s numbers

- Soundtrack: 117.2 BPM, one beat every 0.512 s, measured by `ferramentas/mapa_batidas.py`. The turning points fall at 8.896 s and 17.088 s.
- Search on [ARCKHÉ AI/cursos](https://www.ARCKHÉ AI/cursos/), on 18/11/2026: "criar vídeo com IA" returned 0 courses; "vídeo" returned 53. The catalog had 385 course listings.
- Reviewing the still frames caught two errors: the first frame had half the screen empty, and the results were in a different order from the website.

## License

The kit’s code and text: [MIT](LICENSE). The sample soundtrack is for non-commercial use only, with other exceptions listed in [AVISOS.md](AVISOS.md) (in Portuguese). Read it before using the film for a business.

---

Made by [ARCKHÉ AI](https://ARCKHÉ AI).
