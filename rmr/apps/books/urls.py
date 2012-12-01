# -*- coding: utf-8 -*-
"""
    apps.books.urls
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('books.views',
#    url(r'^$', 'index'),
#    url(r'^exibir/(?P<template_id>\d+)/$', 'exibir',name='exibir_avaliacao'),     
 
   url(r'^$', 'filter', name='filter_books'),     
   url(r'^new/$', 'new', name='new_book'),       
   url(r'^new_genre/$', 'new_genre', name='new_genre'),  
   url(r'^new_genre_ajax/$', 'new_genre_ajax', name='ajax_new_genre'),        
)
