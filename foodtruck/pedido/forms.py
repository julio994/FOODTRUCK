from django import forms
from .models import DetallePedido
from .models import Pedido

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido, Pedido
        fields = ['pedido', 'producto', 'cantidad', 'observaciones']
