# -*- coding: utf-8 -*-
import requests
import lxml
from lxml import html

def run():
    "get all books from a given author in saraiva bookstore"    
        
    url = "http://www.skoob.com.br/livro/lista/tag:sarah%20dessen/tipo:autor"

    r = requests.get(url)
    root = lxml.html.fromstring(r.content)
    
    all_infos = root.cssselect("div.dados_lista_busca")
    
    for book_infos in all_infos:
        title = book_infos.cssselect("a.l15ab")[0].text_content()
        print title