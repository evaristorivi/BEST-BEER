from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import formset_factory
from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class SignUpForm(UserCreationForm):
    edadok = forms.BooleanField(required=True)
    acepto = forms.BooleanField(required=True)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'edadok', 'acepto',  'password1', 'password2',  )


class CrearVotoForm(forms.Form):
	voto = forms.IntegerField(max_value=5,min_value=0)
	cerveza = forms.ModelChoiceField(queryset=Cerveza.objects.all())
	pub = forms.ModelChoiceField(queryset=Pub.objects.all())
	captcha = ReCaptchaField()
