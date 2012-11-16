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
 
   url(r'^$', 'list_books', name='list_books'),     
#    url(r'^$', BookCollectionResource.as_view(), name='api-books-collection'),     
#    url(r'^(?P<pk>\d+)/$', BookResource.as_view(), name='api-books-model'),   
)
