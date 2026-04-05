# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Index, UniqueConstraint

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        # No changes needed for this model as it does not have any unique_together or index_together
        pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        # No changes needed for this model as it does not have any unique_together or index_together
        pass