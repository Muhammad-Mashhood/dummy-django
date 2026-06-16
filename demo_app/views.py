# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Book

def index(request):
    books = Book.objects.all()
    title = _("Book List")
    return render(request, 'index.html', {'books': books, 'title': title})