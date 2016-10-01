from managedata import *
from crawler import *
import time

def main():
    create_project_dir("data")
    create_file("data/product_data.txt")

    while True:
        print("\n" * 50)

        try:
            item = load_product()
        except:
            print("Nenhum produto foi adicionado ainda...")
            item = add_product()

        print("1 - Alterar produto")
        print("2 - Ver historico de preco")
        print("3 - Coletar preço")
        print("4 - Sair")
        op = input("Selecione uma opção: ")

        if op == "1":
            confirm = input("\nEssa opção irá substituir o produto anterior, deseja continuar? (s/n)")
            if confirm[0].lower() == "s":
                item = add_product()
            else:
                print("\nNenhuma alteração foi feita.")
                time.sleep(2)
                continue

        elif op == "2":
            item.show_history()
            cont = input("\nPressione qualquer tecla para continuar... ")
            continue

        elif op == "3":
            item.get_price()
            print("Coletando preço atual...")
            time.sleep(2)

        elif op == "4":
            print("Saindo...")
            break

        save_product(item)

# Carrega dados do arquivo e atribui a classe item.
def load_product():
    product_data = load_file("data/product_data.txt")
    item = priceCrawler(product_data[0])
    item.produto = product_data[1]
    item.precos = product_data[2]
    return item

# Coleta dados da classe item e grava para o aquivo
def save_product(item):
    item_info = [item.url, item.produto, item.precos]
    save_file(item_info, "data/product_data.txt")

def add_product():
    url = input("\nURL DO PRODUTO: ")
    item = priceCrawler(url)
    print("\nPRODUTO ADICIONADO: " + item.produto)
    item.get_price()
    return item

main()
