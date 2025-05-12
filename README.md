# ocr-wordsearch-solver
Projeto de visão computacional com deep learning para resolver caça-palavras em portugues a partir de imagens usando OCR.

## Image Treat

# Detcção se é uma imagem ou um print
A imagem é convertida para tons de cinza e, em seguida, é aplicada uma limiarização (threshold).  
Depois, as duas versões da imagem são comparadas para verificar **quantos pixels são diferentes**.  
Com base na porcentagem de diferença, é possível decidir se a imagem é uma **foto** (imagem da tela) ou um **print** (captura direta da tela).

# Tratamento da imagem



## 🧩 Detecção e Resolução de Caça-Palavras
Este projeto realiza a detecção automática e resolução de um caça-palavras a partir de uma imagem. O processo é dividido em várias etapas:

- Detecção das palavras-alvo: Primeiramente, o sistema identifica as palavras que devem ser procuradas no caça-palavras, geralmente listadas ao lado ou abaixo da grade.
- Identificação da área do caça-palavras: Em seguida, é localizada a região da imagem onde está a grade com as letras do caça-palavras.
- Reconhecimento de caracteres (OCR): Cada letra da grade é detectada individualmente. Esta etapa pode ser demorada, pois envolve o reconhecimento caractere por caractere.
- Montagem da matriz de letras: Com os caracteres extraídos, é montada uma matriz representando o conteúdo da grade.
- Resolução do caça-palavras: Utilizando um algoritmo de busca, o sistema percorre a matriz para encontrar as palavras-alvo nas direções possíveis (horizontal, vertical, diagonal, etc.).

## 🧰 Tecnologias utilizadas
- Python
- OpenCV
- Tesseract OCR
- NumPy

## Como Usar
1. Adicionar o arquivo para processamento no direotiro data
2. Necessario ter instalado o engine tesseract e adicionado ao seu Path
    - [Tesseract](https://github.com/tesseract-ocr/tesseract) 
3. O caça palavras tem que seguir uma estrutura onde as palavras a serem pesquisadas estão agrupadas na mesma região (facilitando a indificação)
4. Instale as **dependências do projeto**:

    ```bash
    pip install -r requirements.txt
    ```