# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from BBApp.models import Usuario
from BBApp.models import Cerveza
from BBApp.models import Pub
from BBApp.models import Votaciones

from django.views.generic import ListView

class UsuarioList(ListView):
    model = Usuario
    template_name="BBApp/usuarios_list.html"

class CervezaList(ListView):
    model = Cerveza

class PubList(ListView):
    model = Pub

class VotacionesList(ListView):
    model = Votaciones
