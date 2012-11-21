# -*- coding: utf-8 -*-
"""
    apps.books.views
    ~~~~~~~~~~~~~~

    views for books
    
    :copyright: (c) 2012 by arruda.
"""

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from books.forms import BookFilterForm

from books.models import Book

@login_required
@render_to("books/list.html")
def filter(request):
    "list the books of the logged user"
    
    
    filter_params = {}
    
    filter_form = BookFilterForm(request.user,request.GET)
        
    
    
    if filter_form.is_valid():        
        books = filter_form.get_books()
        
    return locals()

    