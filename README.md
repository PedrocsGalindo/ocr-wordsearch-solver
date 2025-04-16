# ocr-wordsearch-solver
 Projeto de visão computacional com deep learning para resolver caça-palavras em portugues a partir de imagens usando OCR.

adicionar arquivo para processamento no direotiro data

Necessario ter instalado o engine tesseract e adicionado ao seu Path

Para detectar a região das palavras primeiramente determinar a região predominante das palavras detectadas em uma imagem (ex: canto superior direito, canto inferior no meio ...)

A detecção da regiao da foto foi feita apartir de seguinte logica: achado os cantos medios do eixo x e y, é feita uma contagem com as palavras (detecções com mais de 4 letras) para detectar se estão mais passando ou ficando para tras dos cantos medios. Com isso é possivel estimar a posição, visto que se as porcentagens ficassme proximas então era considerado no meio (canto medio de determinado eixo), caso fossem para mais significativas para alguma extremidade então a tendencia é que as palavras estejam nessa extremidade.

​A função detect_words_region tem como objetivo identificar a região predominante das palavras detectadas em uma imagem, utilizando os dados fornecidos pelo OCR (Optical Character Recognition) do Tesseract. Essa análise é baseada na posição das palavras em relação ao centro da imagem, considerando apenas aquelas com mais de quatro caracteres.​

🧠 Lógica de Funcionamento
Determinação do Centro da Imagem:

A imagem é dividida horizontal e verticalmente ao meio, calculando-se os pontos médios dos eixos X e Y.​

Análise das Palavras Detectadas:

Para cada palavra com mais de quatro letras, calcula-se o ponto central da sua caixa delimitadora (bounding box).

Compara-se esse ponto com os pontos médios da imagem para determinar em qual região (esquerda/direita e superior/inferior) a palavra se encontra.​

Contagem por Região:

Incrementa-se contadores para cada uma das quatro regiões: esquerda, direita, superior e inferior.​

Determinação da Região Predominante:

Calcula-se a proporção de palavras em cada região.

Se uma região contém mais de 60% das palavras, ela é considerada predominante.

Se nenhuma região atinge esse limiar, mas uma delas contém mais de 40%, a posição é considerada central.

Caso contrário, a região oposta é considerada predominante.​

Resultado Final:

A função retorna uma string indicando a região predominante, combinando as informações horizontais e verticais, como 'right top', 'middle down', etc.

Se nenhuma palavra com mais de quatro letras for detectada, a função retorna None.​


"O idealizador deste projeto reconhece que existem abordagens mais eficazes para essa análise. Em vez de realizar apenas a contagem simples dos elementos, uma alternativa seria somar as distâncias entre os pontos, de forma a obter uma ponderação mais precisa da distribuição.