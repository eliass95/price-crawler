from urllib.request import Request, urlopen
import re


url = input("URL DO PRODUTO: ")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')

# Define regex para site específico.
if re.search("www.submarino.com", url) or re.search("www.americanas.com", url):
    produto = r"description\" content=\"(.*?)\""
    preco = r"price/salesPrice\".*?>(.*?)</span>"
else:
    produto = ""
    preco = ""
    print("Erro!")

print()

# Coleta o nome do produto
regex = re.compile(produto)
matches = re.findall(regex, html)
print("PRODUTO >> " + matches[0])

# Coleta o preço do produto
regex = re.compile(preco)
matches = re.findall(regex, html)
print("PRECO >> " + matches[0])

print("\n--------------------------------------\n")
