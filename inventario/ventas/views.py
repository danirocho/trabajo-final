from django.shortcuts import render, redirect
from .models import Venta, ItemVenta
from .forms import VentaForm, ItemVentaFormSet
from productos.models import Producto
from django.views.generic import ListView, DetailView

def crear_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        formset = ItemVentaFormSet(request.POST)
        if venta_form.is_valid() and formset.is_valid():
            venta = venta_form.save()
            items = formset.save(commit=False)
            total_venta = 0
            for item in items:
                item.venta = venta
                item.subtotal = item.cantidad * item.precio_unitario
                item.save()

                # Descontar stock
                producto = item.producto
                producto.stock -= item.cantidad
                producto.save()

                total_venta += item.subtotal

            venta.total = total_venta
            venta.save()
            return redirect('ventas:lista_ventas')
    else:
        venta_form = VentaForm()
        formset = ItemVentaFormSet()
    
    return render(request, 'ventas/crear_venta.html', {
        'venta_form': venta_form,
        'formset': formset
    })

class VentaListView(ListView):
    model = Venta
    template_name = 'ventas/lista_ventas.html'
    
class VentaDetailView(DetailView):
    model = Venta
    template_name = 'ventas/detalle_venta.html'