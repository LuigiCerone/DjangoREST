# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    #userId = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    thumbnailUrl = models.URLField(max_length=200)

    def __str__(self):
        return self.title

