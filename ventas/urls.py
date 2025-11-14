from django.urls import path
from .views import crear_venta, VentaListView, VentaDetailView

app_name = 'ventas'

urlpatterns = [
    path('crear/', crear_venta, name='crear_venta'),
    path('lista/', VentaListView.as_view(), name='lista_ventas'),
    path('detalle/<int:pk>/', VentaDetailView.as_view(), name='detalle_venta'),
]
