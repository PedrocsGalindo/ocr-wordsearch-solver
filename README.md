# ocr-wordsearch-solver
 Projeto de visão computacional com deep learning para resolver caça-palavras em portugues a partir de imagens usando OCR.

adicionar arquivo para processamento no direotiro data

Necessario ter instalado o engine tesseract e adicionado ao seu Path

Para detectar a região das palavras primeiramente determinar a região predominante das palavras detectadas em uma imagem (ex: canto superior direito, canto inferior no meio ...)

A detecção da regiao da foto foi feita apartir de seguinte logica: 