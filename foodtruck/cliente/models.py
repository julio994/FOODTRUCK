from django.db import models

class Cliente(models.Model):
    name = models.TextField(verbose_name="Nombre",max_length=200)
    contact = models.TextField(verbose_name="contacto")


    def __str__(self) -> str:
       
        return f"{self.id}- {self.name}"
