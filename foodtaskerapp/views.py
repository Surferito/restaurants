from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import RestaurantForm, RegistroUsuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from .models import Restaurante, Plato, Usuario, TipoComida, Comentario


# Create your views here.
@login_required(login_url='/restaurant/sign-in/')
def restaurants(request):
    template_name = "restaurant/prueba.html"
    queryset = Restaurante.objects.all()
    context = {
        "restaurantes": queryset
    }
    return render(request, template_name, context)

def preferidos_por_usuario(request, name):
    print(name)
    name_lowercase = name.lower()
    template_name = "restaurant/preferidos_usuario.html"
    queryuser = User.objects.filter(username=name_lowercase)
    queryset = Usuario.objects.filter(user=queryuser)
    print('usuarios', queryset)
    queryset1 = Comentario.objects.filter(user=queryset)
    print('comentarios: ', queryset1)
    context = {
        "usuarios": queryset,
        "comentarios": queryset1
    }
    return render(request, template_name, context)

def mis_preferidos(request):
    template_name = "restaurant/mis_preferidos.html"
    queryset = Usuario.objects.all()
    print('usuarios', queryset)
    queryset1 = Comentario.objects.all()
    print('comentarios: ', queryset1)
    context = {
        "usuarios": queryset,
        "comentarios": queryset1
    }
    return render(request, template_name, context)


def probando_forms(request):
    form = PruebaForms(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return redirect(mis_preferidos)
    if form.errors:
        errors = form.errors

    template_name = "restaurant/prueba_form.html"
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


def home(request):
    return render(request, 'restaurant/index.html', {'prueba': 1007})

@login_required(login_url='/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})

#pilla el user y redirecciona a su perfil, lo utilizo para el login y signup
def account_redirect(request):
    name = request.user.username
    return redirect('/' + name)


def usuario_sign_up(request):
    user_form = RegistroUsuario()

    if request.method == "POST":
        user_form = RegistroUsuario(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"],
            ))

            return redirect(account_redirect)

    return render(request, 'restaurant/sign_up.html', {
        "user_form": user_form,
    })