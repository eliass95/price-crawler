from managedata import *
from mainfunctions import *

def main():
    while True:
        print("\n" * 50)

        # Carrega o arquivo para variavel itens
        try:
            itens = load_file("data/product_data.txt")
            list_products(itens)
        except:
            itens = []
            print(".. Nenhum produto adicionado ainda.\n")

        # Exibe as opções
        print("0) Coletar preços de hora em hora\n")
        print("1) Adicionar produto")
        print("2) Ver historico de preço")
        print("3) Coletar preço agora")
        print("4) Deletar produto")
        print("5) Sair")
        print("--------------------------")
        op = input("Selecione uma opção: ")

        if op == "0":
            crawl_prices()

        elif op == "1":
            itens = add_product(itens)

        elif op == "2":
            history(itens)

        elif op == "3":
            itens = get_all_prices(itens)

        elif op == "4":
            itens = del_product(itens)

        elif op == "5":
            print("Encerrando... ")
            break

        else:
            print("Selecione uma opção válida")

        save_file(itens, "data/product_data.txt")


create_project_dir("data")

# Habilitar a função crawl_prices para coletar
# preços automaticamente de hora em hora

# crawl_prices()

main()
