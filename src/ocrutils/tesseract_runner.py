from pathlib import Path
import subprocess
import pandas as pd
import io


def img_to_data_dict(config : str) -> dict:
    img_path = Path.cwd().joinpath('src','data','wordsearch.png')  
    img_path = str(img_path)
    command = [
        "tesseract",
        'wordsearch.pgn',
        'stdout',           #resultado direto na saída
        config,
        'tsv'               #retorno não é somente o texto, tem mais informaçãos, similiar a usar image_to_data()
    ]
    result = subprocess.run(command, cwd= str(Path.cwd().joinpath('src','data')), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    df = pd.read_csv(io.StringIO(result.stdout), sep="\t")
    output_dict = df.to_dict(orient="list")
    return output_dict