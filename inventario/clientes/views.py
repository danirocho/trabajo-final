from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(nombre__icontains=q) | Q(apellido__icontains=q) | Q(numero_documento__icontains=q)
            )
        return queryset

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/crear_cliente.html'
    success_url = reverse_lazy('lista_clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/editar_cliente.html'
    success_url = reverse_lazy('lista_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/eliminar_cliente.html'
    success_url = reverse_lazy('lista_clientes')
