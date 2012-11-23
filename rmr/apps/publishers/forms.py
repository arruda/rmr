# -*- coding: utf-8 -*-
"""
    apps.publishers.forms
    ~~~~~~~~~~~~~~

    publishers forms
    
    :copyright: (c) 2012 by arruda.
"""


from django import forms
from django.utils.translation import ugettext_lazy as _

from publishers.models import Publisher


class NewPublisherForm(forms.ModelForm):
    "a new Publisher form"
    
    class Meta:
        model = Publisher
        exclude = ('user',)
        