# -*- coding: utf-8 -*-
"""
    apps.publishers.urls
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('publishers.views',   
     
   url(r'^new/$', 'new', name='new_publisher'),     
)
