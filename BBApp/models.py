# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
class Votos(models.Model):
    una_estrella = models.IntegerField(default=0)
    dos_estrella = models.IntegerField(default=0)
    tres_estrella = models.IntegerField(default=0)
    cuatro_estrella = models.IntegerField(default=0)
    cinco_estrella = models.IntegerField(default=0)

    usuarios = models.ManyToManyField(Usuarios)

class Cervezas(models.Model):
   	nombre_cerveza = models.CharField(max_length=200)
   	observaciones = models.TextField()
   	fotos = models.FileField(upload_to='fotos/%Y/%m/%d')

   	puntuacion = models.ManyToManyField(Votos)

class Pubs(models.Model):
    nombre_Pub = models.CharField(max_length=200)
    direccion_pub = models.CharField(max_length=200)

    Cerveza = models.ManyToManyField(Cervezas)
    
