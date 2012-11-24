# -*- coding: utf-8 -*-
"""
    apps.accounts.views
    ~~~~~~~~~~~~~~

    views related to accounts, like login/logout and register
    
    :copyright: (c) 2012 by arruda.
"""

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from django.contrib.auth.models import User

from accounts.forms import RegistrationForm

@render_to('users/register.html')
def register(request): 
    if request.user != None and request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            #Create the user
            email = form.cleaned_data.get('email')
            passwd = form.cleaned_data.get('password1')
            
            user = User(email=email)
            user.set_password(passwd)            
            user.save()
            user.username = user.pk 
            user.save()
            user.backend='user_backends.email_username.EmailOrUsernameModelBackend'
                        
            #logs the new user
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return locals()