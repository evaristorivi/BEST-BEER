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
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from BBApp.views import *
from BBApp.forms import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from BBApp import views

router = routers.DefaultRouter()
router.register(r'usuariosapi', views.UserViewSet)
router.register(r'cervezasapi', views.CervezaAPI)
router.register(r'pubsapi', views.PubsAPI)
router.register(r'votacionesapi', views.VotacionesAPI)


urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^$', VotacionesList.as_view(), name="home"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^usuarios/$', UsuarioList.as_view(), name="usuarios_list"),
    url(r'^usuarios/delete/(?P<pk>\d+)', UsuarioDelete.as_view(), name="usuarios_delete"),
    url(r'^cervezas/$', CervezaList.as_view(), name="cervezas_list"),
    url(r'^cervezas/create', CervezaCreate.as_view(), name="cervezas_create"),
    url(r'^cervezas/update/(?P<pk>\d+)', CervezaUpdate.as_view(), name="cervezas_update"),
    url(r'^cervezas/delete/(?P<pk>\d+)', CervezaDelete.as_view(), name="cervezas_delete"),
    url(r'^pubs/$', PubList.as_view(), name="pubs_list"),
    url(r'^pub/create', PubCreate.as_view(), name="pubs_create"),
    url(r'^pub/update/(?P<pk>\d+)', PubUpdate.as_view(), name="pubs_update"),
    url(r'^pub/delete/(?P<pk>\d+)', PubDelete.as_view(), name="pubs_delete"),
    url(r'^votaciones/$', VotacionesList.as_view(), name="votaciones_list"),
    url(r'^votaciones/create', crearVoto, name="crearVoto"),
    url(r'^api-rest', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

