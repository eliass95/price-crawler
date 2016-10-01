from managedata import *
from crawler import *

def main():
    create_project_dir("data")
    create_file("data/product_list.txt")
    product_list = load_file("data/product_list.txt")

    add_product(product_list)

    save_file(product_list, "data/product_list.txt")


def show_product_list(product_list):
    pass

def get_all_prices():
    pass

def add_product(product_list):
    url = input("Adicionar produto ---------------------------------------- \nURL DO PRODUTO: ")
    item = priceCrawler(url)
    print("\nPRODUTO ADICIONADO: " + item.produto)
    item.get_price()

    item_info = [item.url, item.produto, item.precos]
    create_product_file(item_info)
    #product_list.append([item.produto, item_path])

    return item

main()
