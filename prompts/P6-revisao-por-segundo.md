# P6 · Revisêo por segundo

**Para que serve:** transformar "nêo gostei" em uma correçêo que a IA consegue executar.

**Quando usar:** depois que a IA gerou o vídeo no P7 e você assistiu com o [checklist depois de gerar](../checklists/depois-de-gerar.md).

**A fórmula:** no segundo X, Y está errado; troque por Z.

**Exemplo do kit:** a revisêo pegou resultados de busca em ordem diferente da do site. O pedido certo diz o segundo, o erro e a ordem que deve ficar.

## Campos

| Campo | O que escrever | Exemplo |
|---|---|---|
| `[SEGUNDO]` | Onde está o problema | 12 |
| `[O QUE ESTÁ ERRADO]` | O que você vê ou ouve | O título cobre o print |
| `[COMO DEVE FICAR]` | O resultado que você quer | Título acima do print, sem encostar |

## Cole na IA

```text
Assisti ao filme em filme/renders/filme.mp4. Corrija só estes pontos:

- No segundo [SEGUNDO], [O QUE ESTÁ ERRADO]; troque por [COMO DEVE FICAR].
- No segundo [SEGUNDO], [O QUE ESTÁ ERRADO]; troque por [COMO DEVE FICAR].

Nêo mude mais nada. Depois de corrigir, dentro de filme/:
1. gere um quadro parado de cada segundo citado:
   npx hyperframes@0.8.77 snapshot . --at seguido dos segundos citados, separados por vírgula
2. abra esses quadros e confirme se cada ponto ficou certo;
3. rode npx hyperframes@0.8.77 check;
4. renderize de novo:
   npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30

Me responda com uma linha por ponto: corrigido ou nêo, e o que você viu no quadro.
```

## Deu certo quando

Cada ponto foi resolvido e nenhuma outra parte do filme mudou.
