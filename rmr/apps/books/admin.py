# -*- coding: utf-8 -*-
"""
    apps.books.admin
    ~~~~~~~~~~~~~~

    admin for books
    
    :copyright: (c) 2012 by arruda.
"""
from django.contrib import admin
from books.models import Book

admin.site.register(Book, admin.ModelAdmin)
