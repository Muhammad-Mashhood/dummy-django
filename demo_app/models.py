# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import UniqueConstraint, Index

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        # No changes needed for this model, but we can add constraints if needed
        pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        # No changes needed for this model, but we can add constraints if needed
        pass