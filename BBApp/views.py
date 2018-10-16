# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from BBApp.models import Usuario
from BBApp.models import Cerveza
from BBApp.models import Pub
from BBApp.models import Votaciones
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.views.generic import ListView

class UsuarioList(ListView):
    model = Usuario
    template_name="BBApp/usuarios_list.html"

class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'
    template_name="BBApp/usuarios_create.html"

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = '__all__'
    template_name="BBApp/usuarios_update.html"

class CervezaList(ListView):
    model = Cerveza
    template_name="BBApp/cervezas_list.html"

class PubList(ListView):
    model = Pub
    template_name="BBApp/pubs_list.html"

class VotacionesList(ListView):
    model = Votaciones
    template_name="BBApp/votaciones_list.html"
