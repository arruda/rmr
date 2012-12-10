# -*- coding: utf-8 -*-
import requests
import lxml
from lxml import html

def run():
    "get all books from a given author in saraiva bookstore"    
        
    
    url = "http://www.livrariasaraiva.com.br/pesquisaweb/pesquisaweb.dll/pesquisa?ID=B16209CE7DC0C0A0005030518&PAC_ID=18659&FILTRON1=B&ESTRUTN1=0301&ORDEMN2=E&PALAVRASN1=sarah%20dessen"
    
    
    r = requests.get(url)
    root = lxml.html.fromstring(r.content)
    
    books_tables = root.cssselect("table.separador_lista")
    
    for table in books_tables:
        title = table.cssselect("h1.titulo_produto")[0].text_content()
        author_publisher = table.cssselect("h2.titulo_autor")[0].text_content()
        publisher = author_publisher.split('/')[1].split(" (")[0]
        price = table.cssselect("font.precoPor")[0].text_content().split(u"Por\xa0R$\xa0")[1]
        print title, publisher, price
