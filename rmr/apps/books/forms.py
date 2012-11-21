# -*- coding: utf-8 -*-
"""
    apps.books.forms
    ~~~~~~~~~~~~~~

    Book forms
    
    :copyright: (c) 2012 by arruda.
"""


from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from model_utils import Choices

from books.models import Book

class BookFilterForm(forms.Form):
    "filters parameters for books"
    
    ORDER_CHOICES = (
        ('name', _('Name')),
        ('author', _('Author')),
        ('publisher', _('Publisher')),
        ('genres', _('Genres')),
        ('release_date',  _('Release Date')),
        ('desired',  _('Desired Level')),
        ('purchase_store',  _('Purchase Store')),
        ('purchased',  _('Purchased')),
        ('purchase_value',  _('Purchase Value')),
        ('purchase_date',  _('Purchase Date'))
    )
    
#    TASK_STATUS_WITH_BLANK=[('','---------'),] + [(k,v.__unicode__()) for k,v in Task.STATUS] 
    
    order = forms.ChoiceField(label=_('Order by'), choices=ORDER_CHOICES,initial='name', required=False)
#    owner = forms.BooleanField(label=_('Owned by you'), required=False)
#    status = forms.ChoiceField(label=_('Status'), choices=TASK_STATUS_WITH_BLANK ,initial='', required=False)
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BookFilterForm, self).__init__(*args, **kwargs)
        
#        self.fields['project'] = forms.ModelChoiceField(label=_('Project'), queryset=self.member.enterprise.projects.all(),  required=False)
        

    def get_books(self):
        "return the books based upon this form data"
        
        books = Book.objects.filter().order_by('name')
        
        #get order
        order_by = self.cleaned_data.get('order',None)
        if order_by:
            books = books.order_by(order_by)
            
            
        return books