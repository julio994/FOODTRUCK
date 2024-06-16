# views.py
from django.shortcuts import render, redirect
from .models import Pedido, DetallePedido, Producto
from .forms import PedidoForm, DetallePedidoFormSet

def pedido(request, id_producto):
    lista_productos = Producto.objects.filter(id=id_producto)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        detalle_pedido_formset = DetallePedidoFormSet(request.POST)

        if pedido_form.is_valid() and detalle_pedido_formset.is_valid():
            pedido = pedido_form.save()
            detalle_pedido_formset.instance = pedido
            detalle_pedido_formset.save()
            return redirect('success')

    else:
        pedido_form = PedidoForm()
        detalle_pedido_formset = DetallePedidoFormSet()

    return render(request, "pedido/pedido.html", {
        "productos": lista_productos,
        "pedido_form": pedido_form,
        "detalle_pedido_formset": detalle_pedido_formset
    })

def success(request):
    return render(request, 'success.html')
