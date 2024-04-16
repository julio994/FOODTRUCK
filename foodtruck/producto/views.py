from django.shortcuts import render,get_object_or_404
from .models import Producto
# Create your views here.

def producto(request,id_restaurante):

    lista_productos = Producto.objects.filter(id=id_restaurante)
    return render(request, "producto/producto.html",{"productos":lista_productos})