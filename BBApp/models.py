# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
class Votaciones(models.Model):
    usuario = models.ManyToManyField(Usuario)
    voto = models.IntegerField(default=0)
    cerveza = models.ManyToManyField(Cerveza)
class Cerveza(models.Model):
   	nombre_cerveza = models.CharField(max_length=200)
   	observaciones = models.TextField()
   	foto = models.FileField(upload_to='fotos/%Y/%m/%d')
class Pertenencia(models.Model):
    nombre_pub = models.ManyToManyField(Pub)
    cerveza = models.ManyToManyField(Cerveza)
class Pub(models.Model):
    nombre_pub = models.CharField(max_length=200)
    direccion_pub = models.CharField(max_length=200)    
