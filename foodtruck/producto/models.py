from django.db import models
from django.utils import timezone


class Producto(models.Model):
    name=models.CharField(max_length=200, verbose_name="nombre")
    price=models.IntegerField(verbose_name="precio")
    image= models.ImageField(verbose_name="Imagen", upload_to="imagen")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion" )

