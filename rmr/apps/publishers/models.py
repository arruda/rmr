# -*- coding: utf-8 -*-
"""
    apps.publishers.models
    ~~~~~~~~~~~~~~

    publisher models
    
    :copyright: (c) 2012 by arruda.
"""

from utils.abs_models import Abs_Named_Model


class Publisher(Abs_Named_Model):
    
    class Meta:
        app_label = 'publishers'