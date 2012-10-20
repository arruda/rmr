# -*- coding: utf-8 -*-
"""
    apps.stores.admin
    ~~~~~~~~~~~~~~

    stores admin
    
    :copyright: (c) 2012 by arruda.
"""

from django.contrib import admin
from stores.models import Store

admin.site.register(Store, admin.ModelAdmin)
