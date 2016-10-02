import os
import pickle

# Cria pasta se não existir
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Criando pasta " + directory)
        os.makedirs(directory)

# Cria arquivo se já não existir
def create_file(path):
    if not os.path.exists(path):
        with open(path, "wb") as f:
            print("Criando arquivo " + path)

# Carrega dados do arquivo para a memoria
def load_file(path):
    create_file(path)
    with open(path, "rb") as f:
        product_data = pickle.load(f)

    return product_data

# Salva da memoria para o arquivo
def save_file(data, path):
    with open(path, mode="wb") as f:
        pickle.dump(data, f)
        print("Dados salvos no arquivo.")
