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

from authors.models import Author
from publishers.models import Publisher
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
    
#    purchased = forms.ChoiceField(label=_('Purchased'),choices=((False, _('No')), (True, _('Yes'))), required=False)
    order = forms.ChoiceField(label=_('Order by'), choices=ORDER_CHOICES,initial='name', required=False)
#    desired = forms.ChoiceField(label=_('Desired'), choices=BOOK_DESIRED_WITH_BLANK ,initial='',required=False)
    
            
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BookFilterForm, self).__init__(*args, **kwargs)

        self.fields['author'] = forms.ModelChoiceField(
                                                       label=_('Author'),
                                                       queryset=Author.objects.all(),
                                                       required=False)
        
        self.fields['publisher'] = forms.ModelChoiceField(
                                                       label=_('Publisher'),
                                                       queryset=Publisher.objects.all(),
                                                       required=False)
        
        self.fields['genres'] = forms.ModelChoiceField(
                                                       label=_('Genre'),
                                                       queryset=Genre.objects.all(),
                                                       required=False)
        
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
            
#            
#        #userbook infos
#        
#        purchased = self.cleaned_data.get('purchased',None)    
#        if purchased == "True":
#            books = books.filter(pk__in=self.user.books.filter(purchased=purchased))
#            
#            
#        desired = self.cleaned_data.get('desired',None)        
#        if desired:
#            books = books.filter(pk__in=self.user.books.filter(desired=desired))
            
        return books
    
    
class UserBookFilterForm(forms.Form):
    "filters parameters for a users books"
    
    ORDER_CHOICES = (
        ('book__name', _('Name')),
        ('book__author', _('Author')),
        ('book__publisher', _('Publisher')),
        ('book__genres', _('Genres')),
        ('book__release_date',  _('Release Date')),
        ('desired',  _('Desired Level')),
        ('purchase_store',  _('Purchase Store')),
        ('purchased',  _('Purchased')),
        ('purchase_value',  _('Purchase Value')),
        ('purchase_date',  _('Purchase Date'))
    )
    
    BOOK_DESIRED_WITH_BLANK=[('','---------'),] + [(k,v.__unicode__()) for k,v in UserBook.DESIRE_CHOICES] 
    
    purchased = forms.ChoiceField(label=_('Purchased'),choices=(('','---------'),(False, _('No')), (True, _('Yes'))), required=False)
    order = forms.ChoiceField(label=_('Order by'), choices=ORDER_CHOICES,initial='book__name', required=False)
    desired = forms.ChoiceField(label=_('Desired'), choices=BOOK_DESIRED_WITH_BLANK ,initial='',required=False)
    
            
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserBookFilterForm, self).__init__(*args, **kwargs)

        self.fields['author'] = forms.ModelChoiceField(
                                                       label=_('Author'),
                                                       queryset=Author.objects.all(),
                                                       required=False)
        
        self.fields['publisher'] = forms.ModelChoiceField(
                                                       label=_('Publisher'),
                                                       queryset=Publisher.objects.all(),
                                                       required=False)
        
        self.fields['genres'] = forms.ModelChoiceField(
                                                       label=_('Genre'),
                                                       queryset=Genre.objects.all(),
                                                       required=False)
        
    def get_books(self):
        "return the users books based upon this form data"
        
        books = UserBook.objects.all().order_by('book__name')
        
        #get order
        order_by = self.cleaned_data.get('order',None)
        if order_by:
            books = books.order_by(order_by)
            
            
        author = self.cleaned_data.get('author',None)        
        if author:
            books = books.filter(book__author=author)
            
        publisher = self.cleaned_data.get('publisher',None)        
        if publisher:
            books = books.filter(book__publisher=publisher)            
            
        genres = self.cleaned_data.get('genres',None)        
        if genres:
            books = books.filter(book__genres=genres)
            
        purchased = self.cleaned_data.get('purchased',"")    
        if purchased != "":
            purchased = True if purchased == "True" else False
            books = books.filter(purchased=purchased)
            
        desired = self.cleaned_data.get('desired',None)        
        if desired:
            books = books.filter(desired=desired)
#            
            
        return books
    
    

class MarkAsBoughtBookForm(forms.ModelForm):
    "mark a book as bought"
    
    class Meta:
        model = UserBook
#        exclude = ('user','name','publisher','author','')
        fields = ('purchase_store','purchase_value','purchase_date')
        
#    def __init__(self, user, *args, **kwargs):
#        self.user = user
#        super(MarkAsBoughtBookForm, self).__init__(*args, **kwargs)
#        self.fields['purchase_store'].queryset = user.store_set.all()    
        