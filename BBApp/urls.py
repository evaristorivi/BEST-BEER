from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path, include
from BBApp.views import *

urlpatterns = [
    url(r'^usuario/$', UsuarioList.as_view(),name="UsuarioList"),
    url(r'^cerveza/$', CervezaList.as_view()),
    url(r'^pub/$', PubList.as_view()),
    url(r'^votaciones/$', VotacionesList.as_view()),
]


