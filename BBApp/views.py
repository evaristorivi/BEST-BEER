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
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class UsuarioList(ListView):
    model = Usuario
    template_name="BBApp/usuarios/usuarios_list.html"

class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'
    template_name="BBApp/usuarios/usuarios_create.html"
    success_url = reverse_lazy('usuarios_list')

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = '__all__'
    template_name="BBApp/usuarios/usuarios_update.html"
    success_url = reverse_lazy('usuarios_list')

class UsuarioDelete(DeleteView):
    model = Usuario
    fields = '__all__'
    template_name="BBApp/usuarios/usuarios_update.html"
    success_url = reverse_lazy('usuarios_list')

class CervezaList(ListView):
    model = Cerveza
    template_name="BBApp/cervezas/cervezas_list.html"


class CervezaCreate(CreateView):
    model = Cerveza
    fields = '__all__'
    template_name="BBApp/cervezas/cervezas_create.html"
    success_url = reverse_lazy('cervezas_list')

class CervezaUpdate(UpdateView):
    model = Cerveza
    fields = '__all__'
    template_name="BBApp/cervezas/cervezas_update.html"
    success_url = reverse_lazy('cervezas_list')

class CervezaDelete(DeleteView):
    model = Cerveza
    fields = '__all__'
    template_name="BBApp/cervezas/cervezas_delete.html"
    success_url = reverse_lazy('cervezas_list')

class PubList(ListView):
    model = Pub
    template_name="BBApp/pubs_list.html"

class PubCreate(CreateView):
    model = Pub
    fields = '__all__'
    template_name="BBApp/pubs/pubs_create.html"
    success_url = reverse_lazy('pubs_list')

class PubUpdate(UpdateView):
    model = Pub
    fields = '__all__'
    template_name="BBApp/pubs/pubs_update.html"
    success_url = reverse_lazy('pubs_list')

class PubDelete(DeleteView):
    model = Pub
    fields = '__all__'
    template_name="BBApp/pubs/pubs_delete.html"
    success_url = reverse_lazy('pubs_list')

class VotacionesList(ListView):
    model = Votaciones
    template_name="BBApp/votaciones/votaciones_list.html"

class VotacionesCreate(CreateView):
    model = Votaciones
    fields = '__all__'
    template_name="BBApp/votaciones/votaciones_create.html"
    success_url = reverse_lazy('votaciones_list')

class VotacionesUpdate(UpdateView):
    model = Votaciones
    fields = '__all__'
    template_name="BBApp/votaciones/votaciones_update.html"
    success_url = reverse_lazy('votaciones_list')

class VotacionesDelete(DeleteView):
    model = Votaciones
    fields = '__all__'
    template_name="BBApp/votaciones/votaciones_delete.html"
    success_url = reverse_lazy('votaciones_list')
