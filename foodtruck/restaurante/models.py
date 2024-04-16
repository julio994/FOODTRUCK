from django.db import models

# Create your models here.


class Restaurante(models.Model):
    name = models.TextField(verbose_name="Nombre",max_length=200)
    image = models.ImageField()
    contact = models.TextField(verbose_name="contacto")


    def __str__(self) -> str:
        return self.name