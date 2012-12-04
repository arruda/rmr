# -*- coding: utf-8 -*-
"""
    apps.authors.forms
    ~~~~~~~~~~~~~~

    Authors forms
    
    :copyright: (c) 2012 by arruda.
"""


from django import forms
from django.utils.translation import ugettext_lazy as _

from authors.models import Author


class NewAuthorForm(forms.ModelForm):
    "a new Author form"
    
    class Meta:
        model = Author
#        exclude = ('user',)
        