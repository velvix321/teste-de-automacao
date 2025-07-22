from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
resposta = requests.get(url)
html = resposta.text
soup = BeautifulSoup(html, "html.parser")

livros = soup.find_all("article", class_="product_pod")

for livro in livros:
    titulo = livro.h3.a.get("title")
    preco = livro.find("p", class_="price_color").text.replace("Â£", "")
    print(titulo)
    print(preco)
    print("-" * 40)