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
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from BBApp.forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.usuario.localidad = form.cleaned_data.get('localidad')
            user.usuario.estado_civil = form.cleaned_data.get('estado_civil')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})





class UsuarioList(ListView):
    model = Usuario
    template_name="BBApp/usuarios/usuarios_list.html"



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
    template_name="BBApp/pubs/pubs_list.html"

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

class VotacionesCreate(LoginRequiredMixin, CreateView):
    model = Votaciones
    fields = '__all__'
    login_url = '/login/'
    template_name="BBApp/votaciones/votaciones_create.html"
    success_url = reverse_lazy('votaciones_list')

