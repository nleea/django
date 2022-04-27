from django.contrib.auth.models import User
from django.forms import *
from django.contrib.auth.forms import UserCreationForm


class AuthForms(UserCreationForm, ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'password1': 'sss'
        }
        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Primer Nombre'
                }),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido'
                }),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo'
                }),
            'password1': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña'
                }),
            'password2': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Repita Contraseña'
                })
        }
