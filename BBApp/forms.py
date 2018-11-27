from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    localidad = forms.CharField(max_length=30, required=False, help_text='Optional.')
    estado_civil = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'localidad', 'estado_civil',  'password1', 'password2',  )

class CreavotoForm:
        model = Votaciones
        fields = ('usuario', 'voto', 'cerveza', 'pub',  )


 