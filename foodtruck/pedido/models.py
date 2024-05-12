from django.db import models
from django.utils import timezone
from cliente.models import Cliente
from restaurante.models import Restaurante

from producto.models import Producto



class Pedido(models.Model): 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Puedes ajustar esto según tu modelo de usuario/cliente
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetallePedido')
    fecha_pedido = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return  f"Pedido de {self.cliente} - {self.fecha_pedido}"
    
    

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    observaciones = models.TextField(default="sin observaciones")

    def _str_(self):
        return f"{self.pedido} - {self.producto} - Cantidad: {self.cantidad}"
    


