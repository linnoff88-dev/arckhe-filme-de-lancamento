# P7 · Trocar para a sua marca

**Para que serve:** tirar tudo o que ainda é do exemplo e deixar o filme com a sua identidade.

**Regra principal:** use o logo oficial como ele é. A IA pode reduzir e posicionar. Ela não redesenha, não recolore e não recria.

## Campos

| Campo | O que escrever | Exemplo |
|---|---|---|
| `[LOGO]` | Arraste o arquivo oficial para a conversa ou diga onde ele está no computador | Anexei na conversa |
| `[NOME]` | Nome como deve aparecer | Padaria Sol |
| `[CORES]` | Cores oficiais | `#E8622C` e `#FFF4E3` |
| `[FONTE]` | Fonte e arquivo, se houver | Sora, `filme/assets/fonts/Sora.ttf` |
| `[ENDEREÇO]` | Site ou contato final | padariasol.exemplo |
| `[FRASE FINAL]` | Última frase do filme | Seu pão de hoje já pode estar reservado. |

## Cole na IA

```text
Troque o exemplo pela minha marca na pasta filme/.

Logo oficial: [LOGO]
Nome: [NOME]
Cores: [CORES]
Fonte: [FONTE]
Endereço final: [ENDEREÇO]
Frase final: [FRASE FINAL]

Regras:
- Use o arquivo do logo sem redesenhar, recolorir, distorcer ou gerar outro parecido.
- Se o logo estiver ruim ou faltar, pare e me peça o arquivo.
- Procure tudo o que ainda é do exemplo: nome ARCKHÉ, ARCKHÉ AI, banners, números,
  textos de curso e a trilha. Me mostre a lista antes de trocar.
- Use apenas textos, números e telas já aprovados nos passos anteriores.
- Se a licença de uma fonte ou imagem não estiver clara, pergunte.

Depois do meu sim:
1. organize o logo no projeto e faça as trocas;
2. rode npx hyperframes@0.8.77 check dentro de filme/;
3. procure de novo por sobras do exemplo e me mostre o resultado;
4. gere as imagens paradas com npx hyperframes@0.8.77 snapshot . --at seguido de um segundo
   de cada cena, e me mostre as imagens;
5. confira comigo o arquivo checklists/antes-de-renderizar.md e pare.

Só depois que eu aprovar as imagens, gere o vídeo, dentro de filme/:
npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30
Me diga onde o arquivo ficou e me lembre de assistir com checklists/depois-de-gerar.md.
```

## Deu certo quando

Nenhum nome, número, imagem ou som do exemplo sobrou, e o logo está idêntico ao arquivo oficial.
