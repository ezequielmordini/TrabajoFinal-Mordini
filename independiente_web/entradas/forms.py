from django import forms
from .models import EntradaPartido, TipoEntrada

class EntradaPartidoForm(forms.ModelForm):
    class Meta:
        model = EntradaPartido
        fields = ['titulo', 'ubicacion', 'descripcion', 'fecha_partido', 'imagen']

class TipoEntradaForm(forms.ModelForm):
    class Meta:
        model = TipoEntrada
        fields = ['partido', 'nombre', 'precio', 'stock']
