# -*- coding: utf-8 -*-
import datetime
from accounts.models import UserProfile

def run():
    "update all users quotas to have a new one this month"
    
    for up in UserProfile.objects.all():
        #by trying to retrieve the actual quota it will create a new one if this month doesn't have
        up.quota
        
