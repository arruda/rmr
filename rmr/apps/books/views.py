# -*- coding: utf-8 -*-
"""
    apps.books.views
    ~~~~~~~~~~~~~~

    views for books
    
    :copyright: (c) 2012 by arruda.
"""

from utils.decorators import ajax_login_required, JsonResponse

#your data
from books.models import Book

@ajax_login_required
def list_books(request):
    "list the books of the logged user"
    
    books = Book.objects.filter()
    books_json = []
    for book in books:
        books_json.append(book._prepare_json())
        
    return JsonResponse({'books':books_json})

    