# -*- coding: utf-8 -*-
"""
    apps.authors.views
    ~~~~~~~~~~~~~~

    authors views
    
    :copyright: (c) 2012 by arruda.
"""

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from utils.decorators import ajax_login_required, JsonResponse
from authors.forms import NewAuthorForm
    
@login_required
@render_to("authors/new.html")
def new(request):
    "create a new author for the logged user"
    
    if request.method == 'POST':
        form = NewAuthorForm(request.POST)
        if form.is_valid():             
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            form.save_m2m()
            return redirect('filter_books')
    else:
        form = NewAuthorForm()
    
    return locals()


@ajax_login_required
def new_ajax(request):
    "create a new author for the logged user, using ajax"
    
    if request.method == 'POST':
        form = NewAuthorForm(request.POST)
        if form.is_valid():             
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            form.save_m2m()
            return JsonResponse({'id':author.id, 'name':author.name})
        else:
            return JsonResponse({'errors': form.errors})
    
    return JsonResponse({})
