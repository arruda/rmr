# -*- coding: utf-8 -*-
"""
    libs.utils.decorators
    ~~~~~~~~~~~~~~

    here are the generic decorators for RMR
    
    :copyright: (c) 2012 by arruda.
"""
from functools import wraps

from django.utils import simplejson
from django.http import HttpResponse

def ajax_login_required(view_func):
    
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        json = simplejson.dumps({ 'not_authenticated': True })
        return HttpResponse(json, mimetype='application/json')
    
    return wrap


#def requirement_check(function):
#    """
#    Check if the user logged in is a owner of the given enterprise(enterprise_id kwarg)
#    """
#    from enterprises.models import Enterprise, EnterpriseMember
#    @wraps(function)
#    def wrapper(request, *args, **kwargs):
#        enterprise = Enterprise.get_from_user_or_404(request.user)
#        
#        get_kwargs  = {
#                       'enterprise': enterprise,
#                       'user':request.user,                           
#                       }
#        if owner:
#            get_kwargs['member_type'] = EnterpriseMember.MEMBER_TYPE.owner
#            
#        member = get_object_or_404(EnterpriseMember, **get_kwargs)
#                
#        return function(request, *args, **kwargs)       
#    
#    return wrapper