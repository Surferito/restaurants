from django.contrib import admin

# Register your models here.

from foodtaskerapp.models import Restaurante, Plato, Usuario, TipoComida, Comentario_restaurante, Comentario_plato, Fotos_plato

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

class Comentario_restauranteAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurante', 'comentario', 'time')

admin.site.register(Comentario_restaurante, Comentario_restauranteAdmin)

class Comentario_platoAdmin(admin.ModelAdmin):
    list_display = ('user', 'plato', 'comentario', 'time')

admin.site.register(Comentario_plato, Comentario_platoAdmin)

class Fotos_platoAdmin(admin.ModelAdmin):
    list_display = ('user', 'plato', 'time')

admin.site.register(Fotos_plato, Fotos_platoAdmin)