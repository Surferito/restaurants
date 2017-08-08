from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import UserForm, RestaurantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from .models import Restaurant, Carta
from .forms import PruebaForms

# Create your views here.
@login_required(login_url='/restaurant/sign-in/')
def restaurants(request):
    template_name = "restaurant/prueba.html"
    queryset = Restaurant.objects.all()
    context = {
        "restaurantes": queryset
    }
    return render(request, template_name, context)

def mis_preferidos(request):
    template_name = "restaurant/mis_preferidos.html"
    queryset = Carta.objects.all()
    context = {
        "platos": queryset
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

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})

def restaurant_sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"],
            ))

            return redirect(restaurant_home)


    return render(request, 'restaurant/sign_up.html', {
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })