import os
import json

# Cria pasta se não existir
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Criando pasta " + directory)
        os.makedirs(directory)

# Cria arquivo se já não existir
def create_file(path, data="[]"):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as dataFile:
            dataFile.write(data)
            print("Criando arquivo " + path)

# Carrega dados do arquivo para a memoria
def load_file(path):
    create_file(path)
    with open(path) as dataFile:
        product_data = json.load(dataFile)

    return product_data

# Salva da memoria para o arquivo
def save_file(data, path):
    with open(path, mode="w", encoding="utf-8") as dataFile:
        json.dump(data, dataFile)
        print("Dados salvos no arquivo.")
