# ocr-wordsearch-solver
 Projeto de visão computacional com deep learning para resolver caça-palavras em portugues a partir de imagens usando OCR.

adicionar arquivo para processamento no direotiro data

Necessario ter instalado o engine tesseract e adicionado ao seu Path

Para detectar a região das palavras primeiramente determinar a região predominante das palavras detectadas em uma imagem (ex: canto superior direito, canto inferior no meio ...)

A detecção da regiao da foto foi feita apartir de seguinte logica: achado os cantos medios do eixo x e y, é feita uma contagem com as palavras (detecções com mais de 4 letras) para detectar se estão mais passando ou ficando para tras dos cantos medios. Com isso é possivel estimar a posição, visto que se as porcentagens ficassme proximas então era considerado no meio (canto medio de determinado eixo), caso fossem para mais significativas para alguma extremidade então a tendencia é que as palavras estejam nessa extremidade.

​A função detect_words_region tem como objetivo identificar a região predominante das palavras detectadas em uma imagem, utilizando os dados fornecidos pelo OCR (Optical Character Recognition) do Tesseract. Essa análise é baseada na posição das palavras em relação ao centro da imagem, considerando apenas aquelas com mais de quatro caracteres.​

🧭 Detecção da Região Predominante do Texto na Imagem
A função detect_words_region tem como objetivo identificar onde o texto está concentrado em uma imagem, com base na saída do OCR (Optical Character Recognition) do Tesseract.

Essa análise considera palavras com mais de 4 letras e verifica se elas estão posicionadas majoritariamente à esquerda, direita, acima ou abaixo do centro da imagem — retornando regiões como:
"right top", "left down", "middle middle", etc.

🧠 Lógica de Funcionamento
1. Determinação do Centro da Imagem
A imagem é dividida horizontal e verticalmente ao meio, definindo os pontos médios dos eixos X e Y.
Esses pontos são usados como referência para classificar onde cada palavra está localizada.

2. Análise das Palavras Detectadas
Para cada palavra com mais de 4 letras:

Calcula-se o centro da bounding box (caixa que envolve a palavra).

Verifica-se se esse centro está:

à direita ou esquerda do ponto médio no eixo X;

acima ou abaixo do ponto médio no eixo Y.

Palavras são filtradas para evitar ruídos e garantir uma análise mais precisa.

3. Contagem por Região
São mantidos 4 contadores:

left e right: para o eixo horizontal

top e down: para o eixo vertical

Cada palavra qualificada incrementa o contador correspondente à sua posição.

4. Cálculo de Proporções
Com os dados coletados:

Se mais de 60% das palavras estão em uma extremidade, ela é considerada predominante.

Se entre 40% e 60%, considera-se a posição como central (middle).

Se abaixo de 40%, considera-se a extremidade oposta como predominante.

5. Resultado Final
A função retorna uma string indicando a região predominante combinando os dois eixos:
