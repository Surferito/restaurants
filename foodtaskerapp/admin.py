from django.contrib import admin

# Register your models here.

from foodtaskerapp.models import Restaurante, Plato, Usuario, TipoComida, Comentario

admin.site.register(TipoComida)

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('name', 'tipo', 'time_stamp')

admin.site.register(Restaurante, RestauranteAdmin)


class PlatoAdmin(admin.ModelAdmin):
    list_display = ('plato', 'restaurante', 'time')

admin.site.register(Plato, PlatoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated')

admin.site.register(Usuario, UsuarioAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurante', 'comentario', 'time')

admin.site.register(Comentario, ComentarioAdmin)