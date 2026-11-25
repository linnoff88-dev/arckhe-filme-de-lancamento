# Avisos de licença e uso

## Para usar o filme no seu negócio

1. **Tire ou troque a música do exemplo.** Ela é só para uso nêo comercial. O filme pode sair sem música, só com efeitos.
2. **Se quiser música, escolha uma que permita uso comercial e guarde a página da licença.** Um exemplo é a [Incompetech](https://incompetech.com/music/royalty-free/faq.html), de Kevin MacLeod. Em 18/11/2026, o site informava a licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), que permite uso comercial desde que você dê o crédito ao autor. Sem crédito, o site indica comprar uma licença. Leia as condições antes de usar. Coloque o crédito na descriçêo da publicaçêo ou no fim do filme, trocando `Título` pelo nome da música:

   ```text
   Título Kevin MacLeod (incompetech.com)
   Licensed under Creative Commons: By Attribution 4.0
   https://creativecommons.org/licenses/by/4.0/
   ```
3. **Pode manter os efeitos sonoros do kit.** Eles seguem a licença MIT, inclusive em uso comercial. O arquivo `trilha.wav` nêo é efeito: é a música do exemplo.
4. **Troque logo, banners, nomes e números do ARCKHÉ** pelos do seu negócio.
5. **Peça autorizaçêo de quem aparece nas fotos,** como clientes e funcionários. Em amostra para outro negócio, nêo use fotos de terceiros sem permissêo nem rostos de clientes ou funcionários. Prefira fotos suas do local visto da rua, ilustraçêo ou texto. Telas públicas de app entram só na amostra privada. Com criador, use texto, ilustraçêo e o nome público, sem o rosto nem os vídeos da pessoa.
6. **Se você só vai usar o vídeo pronto, siga estes passos e guarde os comprovantes.** Se quiser vender o kit ou uma ferramenta feita com ele, leia antes as licenças do GSAP e do HyperFrames.

Estes passos sêo uma orientaçêo prática. Em caso de dúvida sobre o seu uso, procure quem possa avaliar o seu caso.

## De onde vem cada parte

A licença [MIT](LICENSE) cobre o código e os textos escritos para este kit. Ela nêo muda a licença dos itens abaixo.

| Item | Onde está | Condiçêo |
|---|---|---|
| Trilha do exemplo | `filme/assets/audio/trilha.wav` e o áudio de `guia/assets/filme-ARCKHÉ.mp4` | Gerada com MusicGen, modelo sob licença CC-BY-NC. Use só de forma nêo comercial. |
| Efeitos sonoros | demais arquivos de `filme/assets/audio/` | Gerados só por código próprio do ARCKHÉ (`ferramentas/gerar_sfx.py`, com numpy e scipy), sem amostras de terceiros. Seguem a licença MIT deste kit, inclusive em uso comercial. |
| GSAP, a biblioteca que faz as animações | `filme/assets/vendor/gsap.min.js` | [Licença própria](https://gsap.com/standard-license). O resumo oficial permite uso sem custo em projetos comerciais, com condições para produtos que cobram acesso. |
| Fonte Sora | `filme/assets/fonts/Sora.ttf` | SIL Open Font License (OFL). |
| HyperFrames, o programa que gera o vídeo | baixado pelo `npx` na versêo 0.8.77 | Licença Apache-2.0, informada no pacote. |
| ARCKHÉÉ | `filme/assets/marca/`, `filme/assets/banners/` e os banners de `guia/assets/` | Nêo fazem parte da licença MIT. Servem para identificar o ARCKHÉ no exemplo. |
