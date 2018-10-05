# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.nombre_usuario

class Cerveza(models.Model):
   	nombre_cerveza = models.CharField(max_length=200)
   	observaciones = models.TextField()
   	foto = models.FileField(upload_to='BBApp/images/%Y/%m/%d')

	def __str__(self):
		return self.nombre_cerveza

class Pub(models.Model):
    nombre_pub = models.CharField(max_length=200)
    direccion_pub = models.CharField(max_length=200)
    cerveza = models.ManyToManyField(Cerveza, through='Votaciones')

def __str__(self):
		return self.nombre_pub


class Votaciones(models.Model):
    usuario = models.ManyToManyField(Usuario)
    voto = models.IntegerField(default=0)
    cerveza = models.ForeignKey(Cerveza, on_delete=models.CASCADE)
    pub = models.ForeignKey(Pub, on_delete=models.CASCADE)

def __str__(self):
		return self.voto