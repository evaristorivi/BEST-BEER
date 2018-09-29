# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuarios(models.Model):
    choice_text = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    pub_date = models.DateTimeField('date published')


class Cervezas(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	votes = models.IntegerField(default=0)
   	docfile = models.FileField(upload_to='fotos/%Y/%m/%d')

class Pubs(models.Model):
    choice_text = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)