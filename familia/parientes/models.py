from django.db import models
class Primo(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    profesion = models.CharField(max_length=64)
    fecha_de_entrega = models.DateField()

class Tio(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    profesion = models.CharField(max_length=64)
    fecha_de_entrega = models.DateField()

class Sobrino(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    fecha_de_entrega = models.DateField()
# Create your models here.
