# -*- coding: utf-8 -*-
"""
    apps.books.admin
    ~~~~~~~~~~~~~~

    admin for books
    
    :copyright: (c) 2012 by arruda.
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from books.models import Book, UserBook, Genre



class BookAdmin(admin.ModelAdmin):
    fieldsets = [
           (_('Book Informations'),               {'fields': ['name','synopsis','author','publisher','release_date','genres']}),
    ]

    
    list_display = ('name','author','publisher',)
    list_editable = ('author','publisher',)
    list_filter = ['genres__name','author__name','publisher__name']
    search_fields = ['name','author__name','publisher__name']
    
    
class UserBookAdmin(admin.ModelAdmin):
    fieldsets = [
           (_('Informations'),               {'fields': ['user','book','desired','purchased','purchase_value','purchase_date','purchase_store']}),
    ]

    
    list_display = ('user','book','desired','purchased','purchase_value','purchase_date','purchase_store')

admin.site.register(Book, BookAdmin)

admin.site.register(UserBook, UserBookAdmin)

admin.site.register(Genre, admin.ModelAdmin)
