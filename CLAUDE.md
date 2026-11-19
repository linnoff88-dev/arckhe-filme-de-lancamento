# Filme por conversa

Kit aberto do INEMA para fazer um filme de lançamento de cerca de 30 s conversando com uma IA de código. O render é local, com HyperFrames.

## Conta e autor

Repo `inematds/filme-de-lancamento`. Autor e committer: `inematds <inematds@gmail.com>`.

## Testes

- Dentro de `filme/`: `npx hyperframes@0.8.77 check`
- Dentro de `filme/`: `npx hyperframes@0.8.77 render . -o renders/filme.mp4 --fps 30`
- Na raiz: `python3 ferramentas/mapa_batidas.py filme/assets/audio/trilha.wav` → 117,2 BPM e batida de 0,512 s

## Regras

- **Não citar a origem.** Nenhum arquivo do repo cita material, autor, comunidade, marca ou exemplo de terceiros que tenha inspirado o método. Escreva com palavras próprias. A lista de nomes vetados fica fora do repo, com o mantenedor. Rode a busca dessa lista antes de todo commit.
- Só números verificados. Sem preço de mercado e sem promessa de renda ou resultado.
- PT é a fonte. Ao mudar README ou guia, atualize também EN e ES com `inema-traduz`.
- Mudou o fluxo? Atualize "O processo, do início ao fim" no README no mesmo commit.
- `filme/` está validado: só mude com pedido explícito e rode os testes depois.
- Design do guia: `~/projetos/inema-design/DESIGN.md`, seção 2.
