# -*- coding: utf-8 -*-
"""
    apps.accounts.views
    ~~~~~~~~~~~~~~

    views related to accounts, like login/logout and register
    
    :copyright: (c) 2012 by arruda.
"""
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


from annoying.decorators import ajax_request

@ajax_request
def login_ajax(request):
    """
    Displays the login form and handles the login action.
    """

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            # Use default setting if redirect_to is empty
#            redirect_to = settings.LOGIN_REDIRECT_URL


            # Okay, security checks complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return {
                    'ok': True,
                    }
    else:
        form = AuthenticationForm(request)

    request.session.set_test_cookie()


    return {
            'login_form': form.errors,
            }
