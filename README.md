# ocr-wordsearch-solver
 Projeto de visão computacional com deep learning para resolver caça-palavras em portugues a partir de imagens usando OCR.

adicionar arquivo para processamento no direotiro data

Necessario ter instalado o engine tesseract e adicionado ao seu Path

Por algum motivo o tesseract não faz a analise correta (caracteres da lingua portuguesa) executando pelo proprio python ou executando por linha de comando colocando os caminhos absolutos da sainda e imagem, mesmo com todas as configurações corretas. Necesseario que o cmd esteja no diretorio "data" do projeto. Não se sabe se tem que ta no diretorio da  imagem ou se tem que na no mesmo hd. 

O caça palavras tem que seguir uma estrutura onde as palavras a serem pesquisadas estão agrupadas na mesma região (facilitando a indificação)

Para detectar a região das palavras primeiramente determinar a região predominante das palavras detectadas em uma imagem (ex: canto superior direito, canto inferior no meio ...)

A detecção da regiao da foto foi feita apartir de seguinte logica: 