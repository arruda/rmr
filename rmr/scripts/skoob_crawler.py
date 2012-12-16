# -*- coding: utf-8 -*-
import requests
import lxml
from lxml import html

main_url = "http://www.skoob.com.br"

def books_for_author(url=None):
    "return the books of a given author"
    print "acessing: %s" % url
    books_found = []

    r = requests.get(url)
    root = lxml.html.fromstring(r.content)
    
    
    all_infos = root.cssselect("div.dados_lista_busca")
    
    print "books in this page:"
    for book_infos in all_infos:
        title = book_infos.cssselect("a.l15ab")[0].text_content()
        books_found.append(title,)
#        print title
        
    next_page = None
    try:
        next_page = root.cssselect("div.proximo span.l13 a")[0].get("href")
        books_found.extend(books_for_author(main_url+next_page))
    except IndexError:
        pass
    
    return books_found

def run():
    "get all books from a given author in saraiva bookstore"    
        
    url = main_url+"/livro/lista/tag:sarah%20dessen/tipo:autor"
    books = books_for_author(url)
    print "============"
    for book in books:        
        print book