# -*- coding: utf-8 -*-
"""
    apps.accounts.models
    ~~~~~~~~~~~~~~

    account related models
    
    :copyright: (c) 2012 by arruda.
"""

from decimal import  Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    "represents a user profile, for now it has only information about the quota"
    
    user = models.ForeignKey('auth.User')
    quota =  models.DecimalField(_("Quota"),max_digits=10, decimal_places=2,default=Decimal("0"),null=True, blank=True)

    
    class Meta:
        app_label = 'accounts'
        
    def __unicode__(self):
        "return the user email"
        return self.user.email
    