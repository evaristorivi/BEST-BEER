# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Usuario,Cerveza,Pub,Votaciones

admin.site.register(Usuario)
admin.site.register(Cerveza)
admin.site.register(Pub)
admin.site.register(Votaciones)