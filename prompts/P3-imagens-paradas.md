# P3 · Imagens paradas antes de animar

**Para que serve:** aprovar a aparência de cada cena enquanto corrigir ainda é rápido.

**Exemplo do kit:** olhando os quadros parados, a revisão pegou um primeiro quadro com metade da tela vazia.

## Campos

| Campo | O que escrever | Exemplo |
|---|---|---|
| `[HISTÓRIA]` | A versão aprovada no P1 | Versão 2 |
| `[CORES]` | Duas ou três cores da marca | Laranja `#E8622C` e creme |
| `[FONTE]` | Fonte da marca, se tiver | Sora |
| `[FORMATO]` | 1920x1080, deitado, ou 1080x1920, em pé, para WhatsApp e Instagram. O formato em pé ainda não foi testado no kit | 1920x1080 |
| `[SEGUNDOS]` | Um momento de cada cena. Se não souber, peça para a IA escolher | 2, 6, 10, 14, 19, 24, 27 |

## Cole na IA

```text
Monte as cenas do filme na pasta filme/, usando o exemplo que já está lá como modelo.

História aprovada: [HISTÓRIA]
Cores: [CORES]
Fonte: [FONTE]
Formato: [FORMATO], cerca de 30 segundos. Se for 1080x1920, adapte todas as cenas e me avise
que esse formato ainda não foi testado no kit.

Nesta etapa, quero ver a composição final de cada cena, ainda sem ajustar animação, música
ou sons. Cada cena tem uma ideia só, texto grande e o material real aprovado no P2.

Depois, dentro de filme/, gere os quadros:
npx hyperframes@0.8.77 snapshot . --at [SEGUNDOS]

Abra as imagens geradas e me diga, para cada uma: se há texto cortado, área vazia demais,
letra pequena ou elemento sobreposto. Mostre onde estão os arquivos. Pare e espere minha
aprovação antes de animar.
```

## Deu certo quando

Cada quadro parado já se entende sozinho, sem som e sem movimento.
