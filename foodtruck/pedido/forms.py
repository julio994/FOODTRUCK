# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Pedido, DetallePedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'restaurante']

DetallePedidoFormSet = inlineformset_factory(Pedido, DetallePedido, fields=('producto', 'cantidad', 'observaciones'), extra=1, can_delete=True)
