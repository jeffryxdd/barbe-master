from django import forms
from django.forms import ModelForm
from .models import Servicio
from django.contrib.auth.forms import UserCreationForm

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['idServicio','nombreServicio','img','descripcionServicio','categoria']

class CustomUserCreationForm(UserCreationForm):
    pass 