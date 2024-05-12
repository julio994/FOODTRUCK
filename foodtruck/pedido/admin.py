from django.contrib import admin
from .models import Pedido, DetallePedido, Producto

# Register your models here.

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1  # Muestra espacio para agregar un nuevo detalle de pedido
    fields = ['producto', 'cantidad', 'observaciones']
    verbose_name = 'Detalle de Pedido'
    verbose_name_plural = 'Detalles de Pedido'


    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # Eliminar el filtro de productos para permitir seleccionar cualquier producto
        formset.form.base_fields['producto'].queryset = Producto.objects.all()
        return formset


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_pedido',)
    inlines = [DetallePedidoInline]
    list_display = ['cliente', 'restaurante', 'fecha_pedido']
    


admin.site.register(Pedido,PedidoAdmin)


