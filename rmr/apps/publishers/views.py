# -*- coding: utf-8 -*-
"""
    apps.publishers.views
    ~~~~~~~~~~~~~~

    publishers views
    
    :copyright: (c) 2012 by arruda.
"""

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from publishers.forms import NewPublisherForm
    
@login_required
@render_to("publishers/new.html")
def new(request):
    "create a new publisher for the logged user"
    
    if request.method == 'POST':
        form = NewPublisherForm(request.POST)
        if form.is_valid():             
            publisher = form.save(commit=False)
            publisher.user = request.user
            publisher.save()
            form.save_m2m()
            return redirect('filter_books')
    else:
        form = NewPublisherForm()
    
    return locals()