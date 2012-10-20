# -*- coding: utf-8 -*-
"""
    apps.authors.models
    ~~~~~~~~~~~~~~

    authors models
    
    :copyright: (c) 2012 by arruda.
"""


from decimal import  Decimal
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from taggit.managers import TaggableManager

from utils.abs_models import Abs_Named_Model

class Author(Abs_Named_Model):
    "a book author"
    
    class Meta:
        app_label = 'authors'