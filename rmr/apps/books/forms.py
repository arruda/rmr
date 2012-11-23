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

from books.models import Book, Genre


class NewBookForm(forms.ModelForm):
    "a new book form"
    
    class Meta:
        model = Book
        exclude = ('user',)
        
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(NewBookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = user.author_set.all()     
        self.fields['publisher'].queryset = user.publisher_set.all() 
        self.fields['purchase_store'].queryset = user.store_set.all()    
    

class NewGenreForm(forms.ModelForm):
    "a new Genre form"
    
    class Meta:
        model = Genre
        exclude = ('user',)
        
    

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
    
    BOOK_DESIRED_WITH_BLANK=[('','---------'),] + [(k,v.__unicode__()) for k,v in Book.DESIRE_CHOICES] 
    
    purchased = forms.BooleanField(label=_('Purchased'), required=False)
    order = forms.ChoiceField(label=_('Order by'), choices=ORDER_CHOICES,initial='name', required=False)
    desired = forms.ChoiceField(label=_('Desired'), choices=BOOK_DESIRED_WITH_BLANK ,initial='',required=False)
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BookFilterForm, self).__init__(*args, **kwargs)
        
        self.fields['author'] = forms.ModelChoiceField(
                                                       label=_('Author'),
                                                       queryset=self.user.author_set.all(),
                                                       required=False)
        
        self.fields['publisher'] = forms.ModelChoiceField(
                                                       label=_('Publisher'),
                                                       queryset=self.user.publisher_set.all(),
                                                       required=False)
        
        self.fields['genres'] = forms.ModelChoiceField(
                                                       label=_('Genre'),
                                                       queryset=self.user.genre_set.all(),
                                                       required=False)
        
         
        

    def get_books(self):
        "return the books based upon this form data"
        
        books = Book.objects.filter(user=self.user).order_by('name')
        
        #get order
        order_by = self.cleaned_data.get('order',None)
        print order_by
        if order_by:
            books = books.order_by(order_by)
            
            
        author = self.cleaned_data.get('author',None)        
        if author:
            books = books.filter(author=author)
            
        publisher = self.cleaned_data.get('publisher',None)        
        if publisher:
            books = books.filter(publisher=publisher)            
            
        genres = self.cleaned_data.get('genres',None)        
        if genres:
            books = books.filter(genres=genres)
            
        desired = self.cleaned_data.get('desired',None)        
        if desired:
            books = books.filter(desired=desired)
            
        purchased = self.cleaned_data.get('purchased',None)        
        if purchased:
            books = books.filter(purchased=purchased)
            
            
            
        return books