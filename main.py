from urllib.request import Request, urlopen
import re

#funciona submarino e americanas
url = input("Url do produto: ")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')

produto = r"description\" content=\"(.*?)\""
preco = r"price/salesPrice\".*?>(.*?)</span>"

print()

# Coleta o nome do produto
regex = re.compile(produto)
matches = re.findall(regex, html)
print("PRODUTO >> " + matches[0])

# Coleta o preço do produto
regex = re.compile(preco)
matches = re.findall(regex, html)
print("PRECO >> " + matches[0])
