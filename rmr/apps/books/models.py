# -*- coding: utf-8 -*-
"""
    apps.books.models
    ~~~~~~~~~~~~~~

    books models
    
    :copyright: (c) 2012 by arruda.
"""
from decimal import  Decimal
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from taggit.managers import TaggableManager

from utils.abs_models import Abs_Named_Model, Abs_AsJson_Model


class Book(Abs_Named_Model, Abs_AsJson_Model):
    "a book. simple as that"
    #author
    #publisher    
    #purchase_store
    
    DESIRE_CHOICES = Choices(
                             (1,'curious',_("Curious About")),
                             (2,'collection',_("Complete Collection")),
                             (3,'survive',_("Can Survive Without It")),
                             (4,'wait',_("Can Wait a Little Longer")),
                             (5,'now',_("I NEED THIS... NOW!!!")),
                     )
    
    author = models.ForeignKey('authors.Author',related_name='books')
    publisher = models.ForeignKey('publishers.Publisher',related_name='books')
    
    synopsis = models.TextField(_('Synopsis'), null=True,blank=True)
    genres = TaggableManager(verbose_name=_("Genres"),help_text=_("A comma-separated list of genres."))
    
    release_date =  models.DateField(_("Release Date"), default=datetime.date.today, null=True, blank=True)
    desired = models.PositiveSmallIntegerField(_("Desired"), choices=DESIRE_CHOICES, default=DESIRE_CHOICES.curious)
    
    #purchase data
    purchase_store = models.ForeignKey('stores.Store',related_name='books',null=True,blank=True)
    purchased       = models.BooleanField(_("Purchased?"),default=False)
    purchase_value = models.DecimalField(_("Purchase Value"),max_digits=10, decimal_places=2,default=Decimal("0"), null=True, blank=True)
    purchase_date =  models.DateField(_("Purchase Date"),  null=True, blank=True)#, default=datetime.date.today,)
    
    
    def just_released(self):
        "returns True if the release_date - this date is less then one year"
        release_time=datetime.timedelta(days=365)
        return datetime.date.today() - self.release_date < release_time
    
    just_released.short_description = 'Just Released?'
    
    class Meta:
        app_label = 'books'
        
    def _prepare_json(self):       
        book_json = super(Book, self)._prepare_json()
        
        book_json['author'] = None if self.author == None else self.author._prepare_json()
        book_json['publisher'] = None if self.publisher == None else self.publisher._prepare_json()
        book_json['synopsis'] = [self.synopsis,]
#        book_json['genres'] = [self.synopsis,]
        book_json['release_date'] = [self.release_date,]
        book_json['desired'] = [self.desired, self.DESIRE_CHOICES[self.desired-1][1]._proxy____unicode_cast()]
        book_json['purchase_store'] = None if self.purchase_store == None else self.purchase_store._prepare_json()
        book_json['purchased'] = [self.purchased, ]
        book_json['purchase_value'] = [self.purchase_value, ]
        book_json['purchase_date'] = [self.purchase_date, ]
        
        return book_json
    
        
    def save(self, *args, **kwargs):
        """
        If the task is assigned to someone, then add this member to the project members
        """
        #if has a purchase value or date then mark as purchased
        if self.purchase_value or self.purchase_date or self.purchase_store:
            self.purchased = True
        
        super(Book, self).save(*args, **kwargs)
        
        