# clientes/forms.py

from django import forms
from .models import Cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Incluye todos los campos del modelo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()             # Inicializa Crispy Forms
        self.helper.form_method = 'post'       # Método POST para enviar datos
        self.helper.add_input(Submit('submit', 'Guardar Cliente'))  # Botón
