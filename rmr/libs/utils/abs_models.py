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
        ordering = ['name',]

    def __unicode__(self):
        return self.name
    
class Abs_UniqueNamed_Model(models.Model):    
    """
    A Class that has a name and description attr unique.
    """
    
    name = models.CharField(_("Name"), max_length=250,unique=True)
#    description = models.TextField(_('Description'), null=True,blank=True)
    
    class Meta:
        abstract = True
        ordering = ['name',]

    def __unicode__(self):
        return self.name

class Abs_AsJson_Model(models.Model):    
    """
    A Class that has 2 methods: _prepare_json and as_json
    """
    
    class Meta:
        abstract = True
        
    def _prepare_json(self):
        
        json = {}
        json['id'] = self.id        
        json['name'] = self.name
        
        return json
    
    def as_json(self):
        "this book in json format"
        from django.utils import simplejson
        from django.core.serializers.json import DjangoJSONEncoder
        
        return simplejson.dumps(self._prepare_json(), cls=DjangoJSONEncoder)


class Abs_UserConected_Model(models.Model):
    "a model conected to a user"
    
    user = models.ForeignKey('auth.User')
    
    class Meta:
        abstract = True