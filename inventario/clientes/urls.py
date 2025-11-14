from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('lista/', ClienteListView.as_view(), name='lista_clientes'),
    path('crear/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='eliminar_cliente'),
]
