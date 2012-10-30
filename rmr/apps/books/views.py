# -*- coding: utf-8 -*-
"""
    apps.books.views
    ~~~~~~~~~~~~~~

    views for books
    
    :copyright: (c) 2012 by arruda.
"""
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#sliver objects
from sliver.views import ModelResource, CollectionResource
from sliver.mixins import JSONMixin

from utils.decorators import ajax_login_required

#your data
from books.models import Book


#def list_books(request):
#    "list the books of the logged user"
#    books =

class BookCollectionResource(JSONMixin, CollectionResource):
    model = Book
    
    @method_decorator(ajax_login_required)
    def dispatch(self, *args, **kwargs):
        return super(BookCollectionResource, self).dispatch(*args, **kwargs)

class BookResource(JSONMixin, ModelResource):
    model = Book