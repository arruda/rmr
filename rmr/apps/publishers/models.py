# -*- coding: utf-8 -*-
"""
    apps.publishers.models
    ~~~~~~~~~~~~~~

    publisher models
    
    :copyright: (c) 2012 by arruda.
"""

from utils.abs_models import Abs_UniqueNamed_Model, Abs_UserConected_Model


class Publisher(Abs_UniqueNamed_Model):
    "a book publisher"
    class Meta:
        app_label = 'publishers'
        ordering = ['name',]