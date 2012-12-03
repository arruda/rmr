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
    
    @property
    def quota(self):
        "return the user quota for the actual month or creates it based in the last existing, or a new one with 0 quota"
        today = datetime.date.today()
        
        try:
            return self.quotas.get(date__month=today.month, date__year=today.year)
        except Quota.DoesNotExist:
            last_month_quota = 0
            try:
                last_month_quota = self.quotas.all()[0].quota
            except:
                pass
            new_month_quota = self.quotas.create(date=today,quota=last_month_quota)
            return new_month_quota
        
class Quota(models.Model):    
    """
    Represents an user's monthly quota
    """
    user = models.ForeignKey(UserProfile,related_name="quotas")
    date = models.DateField(_("Date"),  default=datetime.date.today)
    
    quota =  models.DecimalField(_("Quota"),max_digits=10, decimal_places=2,default=Decimal("0"),null=True, blank=True)
    
    class Meta:
        app_label = 'accounts'
        ordering = ['-date',]
        
    def __unicode__(self):
        "return the user email"
        return "%s - %s - %s/%s" % (self.quota, self.user.user.email, self.date.month, self.date.year)
    