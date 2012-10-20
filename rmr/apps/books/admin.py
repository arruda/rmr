# -*- coding: utf-8 -*-
"""
    apps.books.admin
    ~~~~~~~~~~~~~~

    admin for books
    
    :copyright: (c) 2012 by arruda.
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from books.models import Book

def func_attr(self, attr):
    return self.__getattribute__(attr)

def html_attr(desc, attr):
    func = lambda x: func_attr(x, attr)
    func.short_description = desc
    func.allow_tags = True
    return func

class Genres(str):
    short_description = 'Genres'
    
genres = Genres('genres__name')
#genres.__setattr__('short_description','Genres')# short_description = 'Genres'


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
           (_('Book Informations'),               {'fields': ['name','synopsis','author','publisher','release_date','desired','genres']}),
           (_('Purchase Informations'),               {'fields': ['purchased','purchase_value','purchase_date','purchase_store'], 'classes': ['collapse']}),
    ]

    
    list_display = ('name','author','publisher','desired','purchased','just_released')
    list_editable = ('author','publisher','desired','purchased',)
    list_filter = ['desired','purchased','genres__name','author__name','publisher__name']
    search_fields = ['name','author__name','publisher__name']

admin.site.register(Book, BookAdmin)
