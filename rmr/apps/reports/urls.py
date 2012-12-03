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
   url(r'^monthly_expenses_vs_quota/$', 'monthly_expenses_vs_quota', name='report_monthly_expenses_vs_quota'),   
   url(r'^stats/$', 'stats', name='stats'),     
)
