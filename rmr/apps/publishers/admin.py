# -*- coding: utf-8 -*-
"""
    apps.publishers.admin
    ~~~~~~~~~~~~~~

    publishers admin
    
    :copyright: (c) 2012 by arruda.
"""

from django.contrib import admin
from publishers.models import Publisher

admin.site.register(Publisher, admin.ModelAdmin)
