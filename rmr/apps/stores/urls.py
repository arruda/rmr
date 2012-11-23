# -*- coding: utf-8 -*-
"""
    apps.stores.urls
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('stores.views',   
     
   url(r'^new/$', 'new', name='new_store'),     
)
