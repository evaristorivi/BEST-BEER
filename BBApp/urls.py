from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^usuario/$', UsuarioList.as_view(),name="Usuario"),
]