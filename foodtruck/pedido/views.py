from django.shortcuts import render
from .models import Producto
# Create your views here.

def pedido(request,id_producto):

    lista_productos = Producto.objects.filter(id=id_producto)
    return render(request, "pedido/pedido.html",{"productos":lista_productos})