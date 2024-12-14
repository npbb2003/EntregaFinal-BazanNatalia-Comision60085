from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CopiaImpresa(models.Model):
    superficie = models.CharField(max_length=40)
    tamanio = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"Copia impresa de superficie {self.superficie}, tamaño {self.tamanio} ${self.precio}"


class Fotolibro(models.Model):
    tamanio = models.IntegerField()
    cant_hojas = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"Fotolibro tamaño {self.tamanio} con {self.cant_hojas} hojas: ${self.precio}"


class SesionFotografica(models.Model):

    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}: {self.descripcion}, ${self.precio}"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user}{self.imagen}"
