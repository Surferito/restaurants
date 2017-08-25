from django import forms

from django.contrib.auth.models import User

from foodtaskerapp.models import Restaurante, Plato, Comentario_plato, Fotos_plato


class RegistroUsuario(forms.ModelForm):
    error_messages = {
        'duplicate_username': 'Este usuario ya existe :('
    }
    class Meta:
        model = User
        fields = ("username", "email", "password",)
        labels = {
            "email": "E-mail",
            "username": "Nombre de usuario",
            "password": "Contraseña"
        }
        help_texts = {
            'username': None,
            'password': None,
        }
        widgets = {
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "username": forms.TextInput(attrs={'class':'form-control'}),
            "password": forms.PasswordInput(attrs={'class':'form-control'})
        }
        error_messages = {
            'username': {
                'required': ("¿Pretendes crear una cuenta sin escribir tu nombre de usuario?"),
                'invalid': ("¿Qué tipo de nombre de usuario quieres poner? "),
            },
            'password': {
                'required': ("Escribe una contraseña hijo mio!"),
            }
        }
    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User._default_manager.get(username=username)
            #if the user exists, then let's raise an error message

            raise forms.ValidationError(
              self.error_messages['duplicate_username'],  #user my customized error message

              code='duplicate_username',   #set the error message key

                )
        except User.DoesNotExist:
            return username

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ("name", "tipo",)
        labels = {
            "name": "Nombre",
            "tipo": "Tipo de restaurante"
        }
        widgets = {
            "name": forms.EmailInput(attrs={'class':'form-control'}),
            "tipo": forms.Select(attrs={'class':'form-control'})
        }

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ("plato", "precio")
        labels = {

            "plato": "Foto del plato",
            "precio": "Precio del plato",
        }
        widgets = {
            "plato": forms.TextInput(attrs={'class':'form-control'}),
            "precio": forms.NumberInput(attrs={'class':'form-control'})
        }

class Fotos_platoForm(forms.ModelForm):
    class Meta:
        model = Fotos_plato
        fields = ("foto",)
        labels = {
            "foto": "Foto del plato",
        }
        widgets = {
            "foto": forms.FileInput(attrs={'class':'form-control'})
        }

