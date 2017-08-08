from django.contrib import admin

# Register your models here.

from foodtaskerapp.models import Restaurant, Carta

admin.site.register(Restaurant)
admin.site.register(Carta)