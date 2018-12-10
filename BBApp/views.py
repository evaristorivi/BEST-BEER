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
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from BBApp.models import *


from django.http import Http404,HttpResponseRedirect,HttpResponse

from django.contrib.auth import logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.detail import DetailView
import datetime                 
from BBApp.forms import *
from django.contrib.auth.models import Group
from rest_framework import serializers

from rest_framework import viewsets
from BBApp.serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.usuario.edadok = form.cleaned_data.get('edadok')
            user.usuario.acepto = form.cleaned_data.get('acepto')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})





class UsuarioList(UserPassesTestMixin,ListView):
    model = Usuario
    login_url='/login/'
    template_name="BBApp/usuarios/usuarios_list.html"
    def test_func(self):
        return self.request.user.is_staff == True

class UsuarioDelete(UserPassesTestMixin,DeleteView):
    model = User
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/usuarios/usuarios_delete.html"
    success_url = reverse_lazy('usuarios_list')
    def test_func(self):
        return self.request.user.is_staff == True

class CervezaList(UserPassesTestMixin,ListView):
    model = Cerveza
    login_url='/login/'
    template_name="BBApp/cervezas/cervezas_list.html"
    def test_func(self):
        return self.request.user.is_staff == True

class CervezaCreate(UserPassesTestMixin,CreateView):
    model = Cerveza
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/cervezas/cervezas_create.html"
    success_url = reverse_lazy('cervezas_list')
    def test_func(self):
        return self.request.user.is_staff == True

class CervezaUpdate(UserPassesTestMixin,UpdateView):
    model = Cerveza
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/cervezas/cervezas_update.html"
    success_url = reverse_lazy('cervezas_list')
    def test_func(self):
        return self.request.user.is_staff == True

class CervezaDelete(UserPassesTestMixin,DeleteView):
    model = Cerveza
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/cervezas/cervezas_delete.html"
    success_url = reverse_lazy('cervezas_list')
    def test_func(self):
        return self.request.user.is_staff == True

class PubList(UserPassesTestMixin,ListView):
    model = Pub
    login_url='/login/'
    template_name="BBApp/pubs/pubs_list.html"
    def test_func(self):
        return self.request.user.is_staff == True

class PubCreate(UserPassesTestMixin,CreateView):
    model = Pub
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/pubs/pubs_create.html"
    success_url = reverse_lazy('pubs_list')
    def test_func(self):
        return self.request.user.is_staff == True

class PubUpdate(UserPassesTestMixin,UpdateView):
    model = Pub
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/pubs/pubs_update.html"
    success_url = reverse_lazy('pubs_list')
    def test_func(self):
        return self.request.user.is_staff == True

class PubDelete(UserPassesTestMixin,DeleteView):
    model = Pub
    login_url='/login/'
    fields = '__all__'
    template_name="BBApp/pubs/pubs_delete.html"
    success_url = reverse_lazy('pubs_list')
    def test_func(self):
        return self.request.user.is_staff == True

class VotacionesList(ListView):
    model = Votaciones
    template_name="BBApp/votaciones/votaciones_list.html"
    ordering=['-voto']

class VotacionesCreate(LoginRequiredMixin, CreateView):
    model = Votaciones
    fields = '__all__'
    login_url = '/login/'
    template_name="BBApp/votaciones/votaciones_create.html"
    success_url = reverse_lazy('votaciones_list')
#    def form_valid(self, form):
#        form.votaciones.usuario = self.request.user
#        return super().form_valid(form)

@login_required(login_url='/login/')
def crearVoto(request):
    if request.method == 'POST':
        form1 = CrearVotoForm(request.POST)
        if form1.is_valid():
            votaciones = Votaciones()
            usuario = Usuario.objects.get(user=request.user)
            votaciones.usuario = usuario
            votaciones.voto = form1.cleaned_data.get('voto')
            votaciones.cerveza = form1.cleaned_data.get('cerveza')
            votaciones.pub = form1.cleaned_data.get('pub')
            votaciones.save()
            return HttpResponseRedirect('/votaciones/')
    else:
        form1 = CrearVotoForm()
    return render(request,'BBApp/votaciones/votaciones_create.html',{'votaciones':form1})
        



class UserViewSet(viewsets.ModelViewSet):
    """
    API 
    """
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class CervezaAPI(viewsets.ModelViewSet):
    """
    API 
    """
    
    queryset = Cerveza.objects.all()
    serializer_class = CervezaSerializer

class PubsAPI(viewsets.ModelViewSet):
    """
    API 
    """
    
    queryset = Pub.objects.all()
    serializer_class = PubsSerializer


class VotacionesAPI(viewsets.ModelViewSet):
    """
    API 
    """
    queryset = Votaciones.objects.all()
    serializer_class = VotacionesSerializer