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

from books.forms import BookFilterForm, NewBookForm

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

    
@login_required
@render_to("books/new.html")
def new(request):
    "create a new book for the logged user"
    
    if request.method == 'POST':
        form = NewBookForm(request.user,request.POST)
        if form.is_valid():             
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            form.save_m2m()
            return redirect('filter_books')
    else:
        form = NewBookForm(request.user)
    
    return locals()

    

