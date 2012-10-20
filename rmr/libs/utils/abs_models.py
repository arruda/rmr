# -*- coding: utf-8 -*-
"""
    libs.utils.abs_models
    ~~~~~~~~~~~~~~

    Abstract models
    
    :copyright: (c) 2012 by arruda.
"""


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Abs_Named_Model(models.Model):    
    """
    A Class that has a name and description attr.
    """
    
    name = models.CharField(_("Name"), max_length=250)
#    description = models.TextField(_('Description'), null=True,blank=True)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
