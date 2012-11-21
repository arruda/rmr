# -*- coding: utf-8 -*-
"""
    apps.books.admin
    ~~~~~~~~~~~~~~

    admin for books
    
    :copyright: (c) 2012 by arruda.
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from books.models import Book, Genre



class BookAdmin(admin.ModelAdmin):
    fieldsets = [
           (_('Book Informations'),               {'fields': ['name','synopsis','author','publisher','release_date','desired','genres']}),
           (_('Purchase Informations'),               {'fields': ['purchased','purchase_value','purchase_date','purchase_store'], 'classes': ['collapse']}),
    ]

    
    list_display = ('name','author','publisher','desired','purchased','purchase_date','purchase_value')
    list_editable = ('author','publisher','desired','purchased','purchase_value','purchase_date')
    list_filter = ['desired','purchased','genres__name','author__name','publisher__name','purchase_date']
    search_fields = ['name','author__name','publisher__name']

admin.site.register(Book, BookAdmin)

admin.site.register(Genre, admin.ModelAdmin)
