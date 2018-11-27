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

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^usuarios/$', UsuarioList.as_view(), name="usuarios_list"),
    url(r'^usuarios/create', UsuarioCreate.as_view(), name="usuarios_create"),
    url(r'^usuarios/update/(?P<pk>\d+)', UsuarioUpdate.as_view(), name="usuarios_update"),
    url(r'^usuarios/delete/(?P<pk>\d+)', UsuarioDelete.as_view(), name="usuarios_delete"),
    url(r'^cervezas/$', CervezaList.as_view(), name="cervezas_list"),
    url(r'^cervezas/create', CervezaCreate.as_view(), name="cervezas_create"),
    url(r'^cervezas/update', CervezaUpdate.as_view(), name="cervezas_update"),
    url(r'^cervezas/delete', CervezaDelete.as_view(), name="cervezas_delete"),
    url(r'^pubs/$', PubList.as_view(), name="pubs_list"),
    url(r'^pub/create', PubCreate.as_view(), name="pubs_create"),
    url(r'^pub/update', PubUpdate.as_view(), name="pubs_update"),
    url(r'^pub/delete', PubDelete.as_view(), name="pubs_delete"),
    url(r'^votaciones/$', VotacionesList.as_view(), name="votaciones_list"),
    url(r'^votaciones/create', VotacionesCreate.as_view(), name="votaciones_create"),
    url(r'^votaciones/update', VotacionesUpdate.as_view(), name="votaciones_update"),
    url(r'^votaciones/delete', VotacionesDelete.as_view(), name="votaciones_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)