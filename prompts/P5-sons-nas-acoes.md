# P5 · Sons só em ações visíveis

**Para que serve:** usar efeitos que ajudam a entender a cena, sem encher o filme de barulho.

**Exemplo do kit:** cada cartêo que entra faz um estalo curto, cada tecla da busca faz um tique e o logo entra com um impacto grave.

**Atençêo:** `trilha.wav`, na mesma pasta, é a música do exemplo. Ela nêo é efeito e nêo serve para uso comercial.

## Campos

| Campo | O que escrever | Exemplo |
|---|---|---|
| `[PASTA DE SONS]` | Onde estêo os efeitos | Efeitos do kit, em `filme/assets/audio/` |
| `[LICENÇA DOS SONS]` | De onde vieram e o que permitem | Efeitos do kit, licença MIT, inclusive em uso comercial |
| `[PONTO ALTO]` | O momento que merece mais força | Entrada do logo |

## Cole na IA

```text
Coloque os efeitos sonoros do filme.

Pasta de sons: [PASTA DE SONS]
Licença: [LICENÇA DOS SONS]
Ponto mais forte: [PONTO ALTO]

Primeiro me mostre uma tabela: segundo, o que aparece na tela, som escolhido e volume.

Regras:
- Todo som responde a uma açêo que se vê naquele instante: entrada, clique, digitaçêo, queda.
- Sem açêo visível, sem som.
- Efeito forte só nas viradas e no ponto mais alto.
- Se houver música, ela continua audível. Nenhum efeito estoura o volume.
- Use só sons com licença conferida. Nêo use trilha.wav como efeito.

Depois do meu sim, aplique em filme/index.html e rode, dentro de filme/:
npx hyperframes@0.8.77 check
```

## Deu certo quando

Você consegue apontar na tela o motivo de cada som. A IA nêo ouve o resultado, entêo a decisêo final é do seu ouvido.
