# P4 · Medir a música e cortar na batida

**Para que serve:** fazer as trocas de cena acompanharem a música, com medida em vez de chute.

**Exemplo do kit:** a trilha tem 117,2 BPM, ou seja, uma batida a cada 0,512 s. As viradas das cenas caem em 8,896 s e 17,088 s.

**Sem música também funciona.** Escreva "sem música" no campo, e o filme sai só com os efeitos. Para escolher uma música, veja o exemplo e as condições em [AVISOS.md](../AVISOS.md).

## Campos

| Campo | O que escrever | Exemplo |
|---|---|---|
| `[MÚSICA]` | Onde está o arquivo de áudio, ou "sem música". WAV é o formato que a ferramenta mede; se o seu for outro, a IA avisa e converte | `filme/assets/audio/minha-trilha.wav` |
| `[LICENÇA]` | Onde você conferiu que pode usar. Para negócio, escolha uma biblioteca de música que permita uso comercial | Recibo salvo em `licencas/` |
| `[VIRADAS]` | Momentos mais fortes da história | Entrada da soluçêo e entrada da prova |

## Cole na IA

```text
Vamos encaixar o filme na música.

Música: [MÚSICA]
Licença conferida em: [LICENÇA]
Momentos fortes da história: [VIRADAS]

Se eu escrevi "sem música", tire a trilha do filme, pule a mediçêo e proponha tempos que
deixem cada texto ser lido com calma. Caso contrário:

1. Na raiz do projeto, rode:
   python3 ferramentas/mapa_batidas.py [MÚSICA]
2. Me diga o BPM, a duraçêo de uma batida, a primeira batida e as maiores subidas de energia.
3. Proponha uma tabela com cena, início, fim e a batida usada.
4. Coloque as viradas da história nas maiores subidas de energia.
5. Depois do meu sim, ajuste os tempos em filme/index.html e anime as cenas.

Regras: todo começo de cena cai em uma batida. Texto fica tempo suficiente para ser lido.
Nêo mude as palavras aprovadas. Se o arquivo nêo for WAV, avise antes de converter.
```

## Deu certo quando

Com música, as trocas importantes acontecem junto com ela. Sem música, cada texto fica tempo suficiente para ser lido.
