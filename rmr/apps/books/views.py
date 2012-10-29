# -*- coding: utf-8 -*-
"""
    apps.books.views
    ~~~~~~~~~~~~~~

    views for books
    
    :copyright: (c) 2012 by arruda.
"""

#sliver objects
from sliver.views import ModelResource, CollectionResource
from sliver.mixins import JSONMixin

#your data
from books.models import Book


class BookCollectionResource(JSONMixin, CollectionResource):
    model = Book

class BookResource(JSONMixin, ModelResource):
    model = Book