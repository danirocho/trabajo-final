from django import forms
from django.forms import inlineformset_factory
from .models import Venta, ItemVenta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['codigo', 'cliente']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar Venta'))

# Formset para los items de la venta
ItemVentaFormSet = inlineformset_factory(
    Venta, ItemVenta,
    fields=['producto', 'cantidad', 'precio_unitario'],
    extra=1,
    can_delete=True
)
