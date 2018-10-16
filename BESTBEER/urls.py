"""BESTBEER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from BBApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/$', UsuarioList.as_view(), name="usuarios_list"),
    url(r'^usuario/create', UsuarioCreate.as_view(), name="usuarios_create"),
    url(r'^usuario/update/(?P<pk>\d+)', UsuarioUpdate.as_view(), name="usuarios_update"),
    url(r'^cerveza/$', CervezaList.as_view(), name="cervezas_list"),
    url(r'^pub/$', PubList.as_view(), name="pubs_list"),
    url(r'^votacion/$', VotacionesList.as_view(), name="votaciones_list"),
]
