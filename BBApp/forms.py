from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import formset_factory

class SignUpForm(UserCreationForm):
    localidad = forms.CharField(max_length=30, required=False, help_text='Optional.')
    estado_civil = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'localidad', 'estado_civil',  'password1', 'password2',  )


class CrearVotoForm(forms.Form):
	voto = forms.IntegerField(max_value=5,min_value=0)
	cerveza = forms.ModelChoiceField(queryset=Cerveza.objects.all())
	pub = forms.ModelChoiceField(queryset=Pub.objects.all())