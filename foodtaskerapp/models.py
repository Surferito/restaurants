from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='restaurant_logo/', blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Carta(models.Model):
    restaurante = models.CharField(max_length=200)
    plato = models.CharField(max_length=200)

    def __str__(self):
        return self.restaurante