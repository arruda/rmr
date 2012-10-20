# -*- coding: utf-8 -*-
"""
    apps.authors.admin
    ~~~~~~~~~~~~~~

    authors admin
    
    :copyright: (c) 2012 by arruda.
"""

from django.contrib import admin
from authors.models import Author

admin.site.register(Author, admin.ModelAdmin)
