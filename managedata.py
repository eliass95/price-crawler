import os
import json

# Cria arquivo se já não existir
def create_product_file(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as dataFile:
            dataFile.write("[]")
            print("Arquivo criado: " + path)
    else:
        print("Arquivo existente carregado.")


# Carrega dados do arquivo para a memoria
def load_file(path):
    create_product_file(path)
    with open(path) as dataFile:
        product_data = json.load(dataFile)

    return product_data


# Salva da memoria para o arquivo
def save_file(data, path):
    with open(path, mode="w", encoding="utf-8") as dataFile:
        json.dump(data, dataFile)
        print("Dados salvos no arquivo.")
