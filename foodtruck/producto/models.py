from django.db import models

class Producto(models.Model):
    name=models.CharField(max_length=200, verbose_name="nombre")
    price=models.IntegerField(verbose_name="precio")
    image= models.ImageField(verbose_name="Imagen", upload_to="imagen")


