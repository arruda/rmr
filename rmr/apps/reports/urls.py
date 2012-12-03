# -*- coding: utf-8 -*-
"""
    apps.reports.urls
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('reports.views',   
     
   url(r'^test_flot/$', 'test_flot', name='test_flot'),     
)
