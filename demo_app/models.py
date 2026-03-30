# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import UniqueConstraint, Index

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(fields=['name'], name='unique_author_name')
        ]
        indexes = [
            Index(fields=['name'], name='author_name_index')
        ]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'], name='unique_book_title_author')
        ]
        indexes = [
            Index(fields=['title'], name='book_title_index')
        ]