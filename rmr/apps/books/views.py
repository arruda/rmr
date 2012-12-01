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


from utils.decorators import ajax_login_required, JsonResponse

from books.forms import BookFilterForm, NewBookForm, NewGenreForm

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

@login_required
@render_to("books/new_genre.html")
def new_genre(request):
    "create a new genre for the logged user"
    
    if request.method == 'POST':
        form = NewGenreForm(request.POST)
        if form.is_valid():             
            genre = form.save(commit=False)
            genre.user = request.user
            genre.save()
            form.save_m2m()
            return redirect('filter_books')
    else:
        form = NewGenreForm()
    
    return locals()

    
@ajax_login_required
def new_genre_ajax(request):
    "create a new genre for the logged user, using ajax"
    
    if request.method == 'POST':
        form = NewGenreForm(request.POST)
        if form.is_valid():             
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            form.save_m2m()
            return JsonResponse({'model':"genre",'id':object.id, 'name':object.name})
        else:
            return JsonResponse({'errors': form.errors})
    
    return JsonResponse({})


