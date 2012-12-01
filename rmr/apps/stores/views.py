# -*- coding: utf-8 -*-
"""
    apps.stores.views
    ~~~~~~~~~~~~~~

    stores views
    
    :copyright: (c) 2012 by arruda.
"""

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from utils.decorators import ajax_login_required, JsonResponse

from stores.forms import NewStoreForm
    
@login_required
@render_to("stores/new.html")
def new(request):
    "create a new store for the logged user"
    
    if request.method == 'POST':
        form = NewStoreForm(request.POST)
        if form.is_valid():             
            store = form.save(commit=False)
            store.user = request.user
            store.save()
            form.save_m2m()
            return redirect('filter_books')
    else:
        form = NewStoreForm()
    
    return locals()


@ajax_login_required
def new_ajax(request):
    "create a new store for the logged user, using ajax"
    
    if request.method == 'POST':
        form = NewStoreForm(request.POST)
        if form.is_valid():             
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            form.save_m2m()
            return JsonResponse({'model':"store",'id':object.id, 'name':object.name})
        else:
            return JsonResponse({'errors': form.errors})
    
    return JsonResponse({})