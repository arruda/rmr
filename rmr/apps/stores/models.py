# -*- coding: utf-8 -*-
"""
    apps.stores.models
    ~~~~~~~~~~~~~~

    desciption
    
    :copyright: (c) 2012 by arruda.
"""

from utils.abs_models import Abs_UniqueNamed_Model, Abs_UserConected_Model


class Store(Abs_UniqueNamed_Model):
    "a book store"
    
    class Meta:
        app_label = 'stores'
        ordering = ['name',]