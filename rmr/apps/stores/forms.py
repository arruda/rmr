# -*- coding: utf-8 -*-
"""
    apps.stores.forms
    ~~~~~~~~~~~~~~

    stores forms
    
    :copyright: (c) 2012 by arruda.
"""


from django import forms
from django.utils.translation import ugettext_lazy as _

from stores.models import Store


class NewStoreForm(forms.ModelForm):
    "a new Store form"
    
    class Meta:
        model = Store
        exclude = ('user',)
        