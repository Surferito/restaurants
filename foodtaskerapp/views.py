from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import RestaurantForm, RegistroUsuario, PlatoForm, Fotos_platoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from .models import Restaurante, Plato, Usuario, TipoComida, Comentario_restaurante, Comentario_plato


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

    template_name = "restaurant/preferidos_usuario.html"

    queryuser = User.objects.get(username=name)
    queryset = Usuario.objects.filter(user=queryuser)
    print('usuarios', queryset)
    queryset1 = Comentario_restaurante.objects.filter(user=queryset)
    print('comentarios: ', queryset1)
    context = {
        "user": queryuser,
        "usuarios": queryset,
        "comentarios": queryset1
    }
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

def anadir_restaurante(request):
    restaurante_form = RestaurantForm()
    tipos = TipoComida.objects.all()

    if request.method == "POST":
        restaurante_form = RestaurantForm(request.POST)

        if restaurante_form.is_valid():
            restaurante_form.save()
            return redirect(account_redirect)

    return render(request, 'restaurant/anadir_restaurante.html', {
        "restaurant_form": restaurante_form,
        "tipos": tipos,
    })

def ajax_enviar_restaurantes(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        print("nombre del rest: ", name)
        address = request.POST['address']
        phone = request.POST['phone']
        rating = request.POST['rating']
        tipo = request.POST['tipo']


        print("tipo de comida: ", tipo)
        try:
            restaurante = Restaurante.objects.get(google_id=id)
            print("Restaurante ya guardado en la base de datos")
        except Restaurante.DoesNotExist:
            try:
                tipo_comida = TipoComida.objects.get(tipo__iexact=tipo)
            except TipoComida.DoesNotExist:
                tipo_comida = TipoComida(tipo=tipo)
                tipo_comida.save()
            restaurante = Restaurante(name=name, phone= phone, address = address, tipo = tipo_comida, google_id = id, rating = rating)
            restaurante.save()

        #guardamos usuario si no guardado y añadimos restaurante
        user_pk = request.user.pk
        print("este es el pk del user", user_pk)
        user = User.objects.get(pk=user_pk)
        print("user1.....", user)
        try:
            usuario = Usuario.objects.get(user=user)
            print('usuario = Usuario(user=user)')
        except Usuario.DoesNotExist:
            usuario = Usuario(user=user)
            usuario.save()
        usuario.restaurants.add(restaurante)
        print('usuario.restaurants.add(restaurante)')
        usuario.save()

        data = 'success$' + id
    return HttpResponse(data)

#estaria bien que esta funcion utilizara el id del restaurante nuestro no el id de google (por si el usuario no lo pilla de google)
def anadir_plato(request, id_restaurante):
    usuario_pk = request.user.pk
    user = User.objects.get(pk=usuario_pk)
    plato_form = PlatoForm()

    #le mandamos al template unicamente los platos del restaurante elegido
    restaurante_elegido = Restaurante.objects.get(google_id=id_restaurante)
    platos = Plato.objects.filter(restaurante=restaurante_elegido)

    if request.method == "POST":
        plato_form = PlatoForm(request.POST)
        #fotos_plato_form = Fotos_platoForm(request.POST, request.FILES)

        if plato_form.is_valid():

            #guardamos el plato, necesita el objeto restaurante. Se lo pasamos via url

            plato = plato_form.cleaned_data["plato"]
            print("Este es el plato del form: ", plato)
            nuevo_plato = Plato(restaurante= restaurante_elegido, plato= plato)
            nuevo_plato.save()
            print("plato guardado: ", nuevo_plato)

            #Guardamos el plato al usuario

            usuario = Usuario.objects.get(user=user)
            print("Guardamos el usuario con su restaurante", usuario)
            usuario.platos.add(nuevo_plato)
            usuario.save()
            print("Guardamos el plato del usuario", usuario)

            return redirect(account_redirect)

    return render(request, 'restaurant/anadir_plato.html', {
        "user": user,
        "plato_form": plato_form,
        "platos": platos,
        "restaurante": restaurante_elegido,
    })

#esta funcion devuelve el usuario actual dando por hecho que el usuario ya esta creado
def get_user(request):
    user_pk = request.user.pk
    print("este es el pk del user", user_pk)
    user = User.objects.get(pk=user_pk)
    usuario = Usuario.objects.get(user=user)
    return usuario