from django.contrib import admin
from .models import Restaurante
# Register your models here.


class RestauranteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Restaurante,RestauranteAdmin)
