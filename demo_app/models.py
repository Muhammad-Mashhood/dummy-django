# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Index, UniqueConstraint

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        indexes = [Index(fields=['name'])]
        constraints = [UniqueConstraint(fields=['name'], name='unique_author_name')]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        indexes = [Index(fields=['title'])]
        constraints = [UniqueConstraint(fields=['title', 'author'], name='unique_book_title_author')]