# Película por conversación

[![Película por conversación: tu película de lanzamiento hecha solo conversando con la IA](guia/assets/banner-es.jpg)](https://inematds.github.io/filme-de-lancamento/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Tienes un buen negocio y ningún video que lo muestre. **Película por conversación** es un kit gratis y abierto para hacer una película de lanzamiento de unos 30 segundos, sin programa de edición, conversando con Claude Code, una IA que crea archivos en tu computadora. Sirve para quien tiene un pequeño negocio, busca trabajo o quiere un ingreso extra y nunca editó videos. Necesitas una computadora, un plan pago de Claude y fotos del negocio tomadas con el celular; números, solo si tienes. La IA revisa qué falta instalar.

**Qué necesitas:** una computadora y un plan pago de Claude. El kit es gratis; el plan más barato con Claude Code, Pro, costaba [US$ 20 al mes](https://claude.com/pricing) el 18/11/2026, con pago mensual. Todos los planes tienen un límite de uso y no medimos cuánto consume una película. **Probado en Linux; Windows y Mac todavía no se probaron.** En esos sistemas, consulta los [requisitos mínimos oficiales de Claude Code](https://code.claude.com/docs/es/setup), que no garantizan que la película funcione, y prueba primero con la película de ejemplo.

**Programas gratis:** quizá la IA necesite instalar Node.js, que ejecuta el programa que arma la película; FFmpeg, que une imagen y sonido; Chrome, que dibuja cada cuadro; y Python, que mide la música, si usas una. Apruebas antes de instalar.

## 📖 Guía de uso

Guía completa, sin términos técnicos: **https://inematds.github.io/filme-de-lancamento/guia/es/**

¿Es tu primera vez? Abre [COMECE-AQUI.md](COMECE-AQUI.md).

## Pídele a la IA que empiece

Abre Claude Code en esta carpeta y pega:

```text
Lee COMECE-AQUI.md y la carpeta prompts/ de este proyecto. Después explícame con palabras
simples cómo haremos una película de lanzamiento de unos 30 segundos para mi negocio.
Revisa qué falta instalar usando la sección de instalación técnica del README y pídeme
aprobación antes de instalar. Haz una pregunta a la vez sobre el negocio, el problema que
resuelve y las fotos, pantallas y cifras reales que tengo. No cambies ningún archivo antes
de que te diga que sí. No publiques ni envíes nada. Conversa conmigo en español.
```

Las instrucciones del kit están en portugués, y la IA puede explicártelas en español.

Después, solo tienes que pedir `sigue el archivo prompts/P1`, y así sucesivamente. No necesitas abrir los archivos.

## Qué hay aquí

| Carpeta o archivo | Para qué sirve |
|---|---|
| [COMECE-AQUI.md](COMECE-AQUI.md) (en portugués) | El camino corto para quien nunca editó videos |
| [prompts/](prompts/) (en portugués) | P1 a P7, las instrucciones para pegar en la IA, con los campos explicados |
| [amostra/METODO-DA-AMOSTRA.md](amostra/METODO-DA-AMOSTRA.md) (en portugués) | Cómo hacer una película corta para un negocio y mostrársela solo a su dueño |
| [checklists/](checklists/) | Qué revisar antes de generar, después de generar y antes de enviar |
| [filme/](filme/) | La película de ejemplo, editable |
| [ferramentas/mapa_batidas.py](ferramentas/mapa_batidas.py) | Mide la música e indica dónde cortar |
| [guia/](guia/) | La página del proyecto en portugués, inglés y español |
| [AVISOS.md](AVISOS.md) (en portugués) | Licencias de terceros y límites de uso de la música y la marca |

## La película de ejemplo

El ejemplo habla del propio INEMA.CLUB: [`guia/assets/filme-inema.mp4`](guia/assets/filme-inema.mp4). Dura 28,9 s, está en 1920x1080, a 30 cuadros por segundo, y tiene 7 escenas, música y efectos.

---

## El proceso, de principio a fin

🧠 = sesión con la persona · ⚙️ = script · 🤖 = IA

Ejecuta los comandos ⚙️ dentro de la carpeta indicada. Pega las instrucciones 🤖 en Claude Code, abierto en la raíz del proyecto.

| # | Paso | Comando o instrucción | Quién |
|---|---|---|---|
| 1 | Contar sobre el negocio, el público y el problema | conversación inicial de [COMECE-AQUI.md](COMECE-AQUI.md) | 🧠 |
| 2 | Escribir la historia del problema | [P1](prompts/P1-historia-do-problema.md) | 🤖 + 🧠 aprueba |
| 3 | Reunir fotos, pantallas y cifras reales | [P2](prompts/P2-telas-e-numeros-reais.md) | 🧠 entrega, 🤖 organiza |
| 4 | Armar las escenas como imágenes fijas | [P3](prompts/P3-imagens-paradas.md) | 🤖 |
| 5 | Generar los cuadros para revisar | en la carpeta `filme/`: `npx hyperframes@0.8.77 snapshot . --at 2,9,17` | ⚙️ |
| 6 | Aprobar los cuadros | abrir `filme/snapshots/` y decir qué hay que cambiar | 🧠 |
| 7 | Medir la música, si hay | en la raíz: `python3 ferramentas/mapa_batidas.py filme/assets/audio/trilha.wav` (cámbialo por el archivo de tu música) | ⚙️ |
| 8 | Animar y cortar al ritmo | [P4](prompts/P4-musica-e-batida.md) | 🤖 |
| 9 | Añadir sonidos solo a las acciones visibles | [P5](prompts/P5-sons-nas-acoes.md) | 🤖 |
| 10 | Cambiar lo que todavía pertenece al ejemplo por tu marca y mostrar las imágenes fijas | [P7](prompts/P7-sua-marca.md) | 🤖 + 🧠 entrega el logo |
| 11 | Revisar y aprobar las imágenes | [lista de verificación antes de generar](checklists/antes-de-renderizar.md) y, en `filme/`: `npx hyperframes@0.8.77 check` | ⚙️ + 🧠 |
| 12 | Generar el video después de aprobarlo | en `filme/`: `npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30` | ⚙️ |
| 13 | Verlo y pedir correcciones segundo a segundo | [lista de verificación después de generar](checklists/depois-de-gerar.md) y [P6](prompts/P6-revisao-por-segundo.md); después vuelve al paso 11 | 🧠 + 🤖 |
| 14 | Revisarlo antes de mostrárselo a alguien | [lista de verificación](checklists/antes-de-enviar.md) | 🧠 |
| 15 | Hacerlo para otro negocio, si quieres | [método de la muestra](amostra/METODO-DA-AMOSTRA.md) | 🧠 |

P6 va después de P7 porque la revisión se hace sobre la película ya generada con tu marca.

## Instalación técnica

### Qué necesitas

- **Claude Code**, incluido en los [planes pagos de Claude](https://claude.com/pricing). En Windows y Mac, usa la [app Claude](https://code.claude.com/docs/es/desktop-quickstart), pestaña **Code**, **Local** y **Open folder…**. En Linux, usa la [instalación oficial](https://code.claude.com/docs/es/setup). El render se hace localmente; el costo es el plan de la IA.
- **Node.js** con `npx`. Probado con la versión 24.22.3.
- **FFmpeg y FFprobe**. Probados con la versión 6.1.1.
- **Chrome para renderizar**. Ejecuta `npx hyperframes@0.8.77 doctor` en `filme/` para ver qué falta. También avisa si existe una versión más reciente de HyperFrames; este kit usa la versión fija 0.8.77 para que la película salga igual.
- **Python 3 con `numpy` y `scipy`**, solo para medir la música.

Probado en Linux ARM64. El kit no se probó en Windows ni Mac. Los requisitos mínimos oficiales de Claude Code son Windows 10 versión 1809 o macOS 13, con 4 GB de memoria, procesador x64 o ARM64 e internet. Eso no garantiza que la película funcione: no se midieron los requisitos mínimos para generarla.

### Ejecutar la película de ejemplo

```bash
cd filme
npx hyperframes@0.8.77 check
npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30
```

El resultado queda en `filme/renders/filme.mp4`. El render tardó unos 20 s en esta computadora, con Linux ARM64 y 118 GB de memoria. En una computadora común tarda más.

Por defecto, el kit usa 1920x1080. Para WhatsApp e Instagram, pide 1080x1920 en [P3](prompts/P3-imagens-paradas.md). Ese formato todavía no se probó con el kit.

### Cómo funciona por dentro

Cada escena es una página HTML en `filme/compositions/`, animada con GSAP. `filme/index.html` indica cuándo empieza cada escena, la música y cada efecto. HyperFrames 0.8.77 abre todo en un navegador sin ventana, graba cuadro por cuadro y entrega el MP4.

| Escena | Archivo | Empieza en | Qué hace |
|---|---|---|---|
| 1 | `pilha.html` | 0 s | Los videos guardados se apilan |
| 2 | `queda.html` | 4,288 s | La pila cae: "El después no llegó." |
| 3 | `barras.html` | 8,896 s | El cambio: "Aprende. Practica. Evoluciona." |
| 4 | `busca.html` | 11,968 s | Búsqueda real en el catálogo |
| 5 | `parede.html` | 17,088 s | Pared de cursos y el número 385 |
| 6 | `promessa.html` | 23,232 s | "Gratis. Directo en internet." |
| 7 | `marca.html` | 25,28 s | Logo y pregunta final |

### Las cifras del ejemplo

- Música: 117,2 BPM, un ritmo cada 0,512 s, medido por `ferramentas/mapa_batidas.py`. Los cambios ocurren a los 8,896 s y 17,088 s.
- Búsqueda en [inema.club/cursos](https://www.inema.club/cursos/), el 18/11/2026: "criar vídeo com IA" dio 0 cursos; "vídeo" dio 53. El catálogo tenía 385 fichas de cursos.
- La revisión de los cuadros fijos detectó dos errores: el primer cuadro tenía la mitad de la pantalla vacía y los resultados aparecían en un orden distinto al del sitio.

## Licencia

El código y los textos de este kit: [MIT](LICENSE). La música del ejemplo es solo para uso no comercial y hay otras excepciones en [AVISOS.md](AVISOS.md). Lee el archivo antes de usar la película en un negocio.

---

Hecho por [INEMA.CLUB](https://inema.club).
