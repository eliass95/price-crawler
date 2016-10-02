import time
import threading
from managedata import *
from crawler import *

# Exibe lista de produtos adicionados.
def list_products(itens):
    print("\nLISTA DE PRODUTOS -------------------------------------------------\n")
    for i in itens:
        print("{} - {} - ".format(itens.index(i) + 1, i.produto[0:55].ljust(50)),
            i.precos[-1]["Preco"], "\n   ",  i.url[0:35], "\n")
    print("\n-------------------------------------------------------------------\n")


# Solicita a url, cria objeto priceCrawler e adiciona aos itens.
def add_product(itens):
    url = input("\nADICIONAR Produto \nInsira a url do produto: ")
    prod = priceCrawler(url)
    prod.get_price()

    itens.append(prod)

    return itens


# Exibe o histórico dos preços de todos itens ou apenas de um.
def history(itens):
    selec = input("\nSelecionar um produto específico? (s/n)")
    try:
        if selec[0].lower() == "s":
            num = int(input("Insira o numero do produto: "))
            print("\n" * 3)
            itens[num-1].show_history()

        else:
            print("\n" * 3)
            for i in itens:
                print("\n"*2)
                i.show_history()
    except:
        print("\n" * 3)
        for i in itens:
            print("\n"*2)
            i.show_history()

    cont = input("Pressione uma tecla para continuar")


# Deleta um item da lista.
def del_product(itens):
    try:
        num = int(input("DELETAR produto \nInsira o numero do produto: "))
        selec = input("Realmente deseja deletar {}? (s/n)".format(itens[num-1].produto[0:30]))

        if selec[0].lower() == "s":
            itens.pop(num-1)
            print("Item Deletado!")

        else:
            print("Deletar produto Cancelado!")

    except:
        print("Deletar produto Cancelado!")

    return itens


# Coleta todos os preços de uma lista.
def get_all_prices(itens):
    for i in itens:
        print("Coletando preço item: {}".format(i.produto[0:25]))
        i.get_price()
    print("Preços coletados!")
    time.sleep(1)

    return itens


# Inicia a thread que irá coletar os preços automaticamente.
def crawl_prices():
        t = threading.Thread(target=executeThread)
        t.start()


# Thead que coletará os preços da lista de hora em hora.
def executeThread():
    while True:
        try:
            # Carrega arquivo
            I = load_file("data/product_data.txt")

            print("Os preços estão sendo coletados de hora!")
            get_all_prices(I)

            # Salvar arquivo
            save_file(I, "data/product_data.txt")

            # Aguarda tempo para coletar preços novamente.
            time.sleep(3600)
        except:
            print("...")
            time.sleep(120)
