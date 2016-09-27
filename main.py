from urllib.request import Request, urlopen
import re

url = input("Url do produto:")
keywords = input("Tipo de produto:")

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')

produto = r"<span itemprop=\"name\">(.*?)</span>"
preco = r"price/salesPrice\" content=\".*?\">(.*?)</span>"



# Coleta o nome do produto
regex = re.compile(produto)
matches = re.findall(regex, html)

for i in matches:
    if re.search(keywords, i):
        nomeproduto = i

print("Produto: " + nomeproduto)


# Coleta o preço do produto
regex = re.compile(preco)
matches = re.findall(regex, html)

print("Preço: " + matches[0])
