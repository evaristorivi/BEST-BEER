# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from BBApp.models import *
from django.views.generic import ListView

class UsuarioList(ListView):
    model = Usuario
    template_name="templates/BBApp/usuarios_list.html"

class CervezaList(ListView):
    model = Cerveza

class PubList(ListView):
    model = Pub

class VotacionesList(ListView):
    model = Votaciones
