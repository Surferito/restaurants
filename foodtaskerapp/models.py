from django.db import models
from django.contrib.auth.models import User

class TipoComida(models.Model):
    tipo = models.CharField(max_length=200)
    def __str__(self):
        return self.tipo

class Restaurante(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    logo = models.ImageField(upload_to='restaurant_logo/', blank=True)
    tipo = models.ForeignKey(TipoComida, verbose_name="tipo de comida")
    google_id = models.CharField(max_length=500, blank=True)
    rating = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=500, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Plato(models.Model):
    restaurante = models.ForeignKey(Restaurante, verbose_name="Restaurantes")
    time = models.DateTimeField(auto_now_add=True)
    plato = models.CharField(max_length=200)
    precio = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.plato

# Añadimos campos al usuario
class Usuario(models.Model):
   user = models.OneToOneField(User)
   time = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   restaurants = models.ManyToManyField(Restaurante)
   platos = models.ManyToManyField(Plato)
   class Meta:
       db_table = 'usuario'
       ordering = ['-time']
       verbose_name_plural = 'usuarios'

   def __str__(self):
        return self.user.username

class Comentario_restaurante(models.Model):
    user = models.ForeignKey(Usuario)
    restaurante = models.ForeignKey(Restaurante)
    comentario = models.TextField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comentario

class Comentario_plato(models.Model):
    user = models.ForeignKey(Usuario)
    plato = models.ForeignKey(Plato)
    comentario = models.TextField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comentario

class Fotos_plato(models.Model):
    user = models.ForeignKey(Usuario)
    foto = models.ImageField(upload_to='dishes/', blank=True, null=True)
    plato = models.ForeignKey(Plato)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.time