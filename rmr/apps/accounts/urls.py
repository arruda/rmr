# -*- coding: utf-8 -*-
"""
    apps.accounts.urls
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('accounts.views',
#    url(r'^$', 'index'),
#    url(r'^exibir/(?P<template_id>\d+)/$', 'exibir',name='exibir_avaliacao'),     
     
    url(r'^register/$', 'register', name='register_user'),  
     url(r'^$','index', name='index'),          
   url(r'^change_quota/$', 'ajax_change_quota', name='ajax_change_quota'),  
)
