# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.translation import ugettext as _
from .models import Book

def index(request):
    books = Book.objects.all()
    # ugettext is deprecated
    title = _("Book List")
    return render(request, 'index.html', {'books': books, 'title': title})
