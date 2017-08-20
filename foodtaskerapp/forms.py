from django import forms

from django.contrib.auth.models import User

from foodtaskerapp.models import Restaurante


class RegistroUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username", "password",)
        labels = {
            "email": "E-mail",
            "username": "Nombre de usuario",
            "password": "Contraseña"
        }
        widgets = {
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "username": forms.TextInput(attrs={'class':'form-control'}),
            "password": forms.PasswordInput(attrs={'class':'form-control'})
        }

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ("name", "phone", "address", "logo")

