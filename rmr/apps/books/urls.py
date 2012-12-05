# -*- coding: utf-8 -*-
"""
    apps.books.urls
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('books.views', 
 
   url(r'^$', 'mybooks', name='my_books'),     
   url(r'^search/$', 'filter', name='filter_books'),     
   url(r'^new/$', 'new', name='new_book'),       
##   url(r'^edit/(?P<id_book>\d+)/$', 'edit', name='edit_book'),       
#   url(r'^mark_bought/(?P<id_book>\d+)/$', 'mark_as_bought', name='mark_as_bought'),       
   url(r'^new_genre_ajax/$', 'new_genre_ajax', name='ajax_new_genre'),        
)
