# Falhas

| data | o que quebrou | menor correção | tipo |
|---|---|---|---|
| 2026-11-18 | Capturas do `agent-browser` com caminho relativo caíram na pasta de outro projeto | Usar sempre caminho absoluto em `screenshot` | infra |
| 2026-11-18 | Primeiro quadro do filme saiu com metade da tela vazia | Deixar o primeiro cartão já visível no quadro 0 e conferir o quadro antes do render | prompt |
| 2026-11-18 | Resultados da busca no filme estavam em ordem diferente da do site | Copiar a ordem da captura real | prompt |
| 2026-11-18 | Capa gerada trocou a manchete pedida por "UM VÍDEO BASTA", que prometia demais | Editar a arte com o texto exato e conferir antes de usar | prompt |
