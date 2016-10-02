from urllib.request import Request, urlopen
import re
import time
from datetime import datetime

class priceCrawler:
    def __init__(self, url):
        self.url = url
        self.produto = ""
        self.precos = []

        self.produto_regex = ""
        self.preco_regex = ""

        self.get_regex()
        self.get_product_name()

    # Define regex para site específico.
    def get_regex(self):
        if re.search("www.submarino.com", self.url) or re.search("www.americanas.com", self.url):
            self.produto_regex = r"description\" content=\"(.*?)\""
            self.preco_regex = r"price/salesPrice\".*?>(.*?)</span>"

        # Para utilizar em outros sites deve ser adicionado a expressão regular correspondente.

        else:
            self.produto_regex = ""
            self.preco_regex = ""
            print("Erro!")

    # Faz requisição ao site e salva o html.
    def get_html(self, url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req).read().decode('utf-8')

            return html
        except:
            print("Não foi possível acessar a url")
            return "ERRO"

    # Coleta o nome do produto
    def get_product_name(self):
        html = self.get_html(self.url)

        regex = re.compile(self.produto_regex)
        matches = re.findall(regex, html)
        self.produto = matches[0]

    # Coleta o preço do produto
    def get_price(self):
        html = self.get_html(self.url)

        regex = re.compile(self.preco_regex)
        matches = re.findall(regex, html)
        hora = time.strftime("%d %b %Y - %H:%M:%S", time.localtime())

        preco_atual = {"Data": hora, "Preco": matches[0]}
        self.precos.append(preco_atual)

    # Exibe histórico de preços
    def show_history(self):
        print("\nPRODUTO: {}".format(self.produto))
        print("\nURL: {}".format(self.url))
        print("-----------------------------------------------------------")

        for i in self.precos:
            print("DATA: {} - PREÇO: {}".format(i["Data"], i["Preco"]))
        print("-----------------------------------------------------------")
