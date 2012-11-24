# -*- coding: utf-8 -*-
"""
    apps.accounts.forms
    ~~~~~~~~~~~~~~

    account forms
    
    :copyright: (c) 2012 by arruda.
"""


from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    "Form that register a enterprise and a owner user for it"
#    
    email = forms.EmailField(label=_("Email"))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification."))
#    
#    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data.lower()).count() > 0:
            raise forms.ValidationError(_("This email is already been used"))

        return data
#    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2