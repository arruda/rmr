# -*- coding: utf-8 -*-
"""
    apps.accounts.models
    ~~~~~~~~~~~~~~

    account related models
    
    :copyright: (c) 2012 by arruda.
"""
import datetime
from decimal import  Decimal

from django.db import models
from django.db.models import Sum
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
    
    def used_monthly_quota(self,month=0):
        """Return the amount of the used quota for a given month, if none given then consider this
            If a month is given, then it will consider the actual month - the given... so if the user wants to see
            1 month behind, then should pass 1, if want to see 2 months behind, then pass 2.
        """
        
        today = datetime.date.today()
        total_purchased = self.user.book_set.filter(purchased=True,
                                  purchase_date__year=today.year,
                                  purchase_date__month=(today.month-month)
                                  ).aggregate(
                                      Sum("purchase_value")
                                  )['purchase_value__sum']
        return total_purchased