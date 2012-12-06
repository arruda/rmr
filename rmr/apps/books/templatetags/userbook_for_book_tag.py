#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django import template
register = template.Library()
from books.models import UserBook

@register.simple_tag(takes_context=True)
def get_userBook_for_Book(context,book, user):
    
    try:
        context['userBook'] = book.users.get(user=user)
    except UserBook.DoesNotExist:
        context['userBook'] = None
    return ''
