# -*- coding: utf-8 -*-
"""
    apps.authors.admin
    ~~~~~~~~~~~~~~

    authors admin
    
    :copyright: (c) 2012 by arruda.
"""

from django.contrib import admin
from accounts.models import UserProfile, Quota

admin.site.register(UserProfile, admin.ModelAdmin)
admin.site.register(Quota, admin.ModelAdmin)
