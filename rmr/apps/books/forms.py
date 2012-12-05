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

from books.models import Book, UserBook, Genre


class NewBookForm(forms.ModelForm):
    "a new book form"
    
    class Meta:
        model = Book
        
    
    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get("name")
        author = cleaned_data.get("author")
        
        if Book.objects.filter(name__iexact=name.lower(),author=author).count() > 0:
            raise forms.ValidationError(_("There is a book with this name and the same author already."))
        
        return cleaned_data
    

class NewGenreForm(forms.ModelForm):
    "a new Genre form"
    
    class Meta:
        model = Genre
#        exclude = ('user',)
        
    

class BookFilterForm(forms.Form):
    "filters parameters for books"
    
    ORDER_CHOICES = (
        ('name', _('Name')),
        ('author', _('Author')),
        ('publisher', _('Publisher')),
        ('genres', _('Genres')),
        ('release_date',  _('Release Date')),
#        ('desired',  _('Desired Level')),
#        ('purchase_store',  _('Purchase Store')),
#        ('purchased',  _('Purchased')),
#        ('purchase_value',  _('Purchase Value')),
#        ('purchase_date',  _('Purchase Date'))
    )
    
    BOOK_DESIRED_WITH_BLANK=[('','---------'),] + [(k,v.__unicode__()) for k,v in UserBook.DESIRE_CHOICES] 
    
    purchased = forms.ChoiceField(label=_('Purchased'),choices=((True, _('Yes')), (False, _('No'))), required=False)
    order = forms.ChoiceField(label=_('Order by'), choices=ORDER_CHOICES,initial='name', required=False)
#    desired = forms.ChoiceField(label=_('Desired'), choices=BOOK_DESIRED_WITH_BLANK ,initial='',required=False)
    
            
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BookFilterForm, self).__init__(*args, **kwargs)

    def get_books(self):
        "return the books based upon this form data"
        
        books = Book.objects.all().order_by('name')
        
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
            
#        desired = self.cleaned_data.get('desired',None)        
#        if desired:
#            books = books.filter(desired=desired)
            
        #userbook infos
        purchased = self.cleaned_data.get('purchased',None)        
        print "purchased:", purchased
        
        
        if purchased == "True":
            print "filtered"
            books = books.filter(pk__in=self.user.books.filter(purchased=purchased))
            
            
            
        return books
    
    

#class MarkAsBoughtBookForm(forms.ModelForm):
#    "mark a book as bought"
#    
#    class Meta:
#        model = Book
##        exclude = ('user','name','publisher','author','')
#        fields = ('purchase_store','purchase_value','purchase_date')
#        
#    def __init__(self, user, *args, **kwargs):
#        self.user = user
#        super(MarkAsBoughtBookForm, self).__init__(*args, **kwargs)
#        self.fields['purchase_store'].queryset = user.store_set.all()    
#        