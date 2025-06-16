from django.shortcuts import render, get_object_or_404, redirect
from .models import EntradaPartido, TipoEntrada, CompraEntrada
from django.contrib.auth.decorators import login_required
from django import forms
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class CompraForm(forms.Form):
    tipo_entrada_id = forms.IntegerField(widget=forms.HiddenInput())
    cantidad = forms.IntegerField(min_value=1)

@login_required
def detalle_partido(request, pk):
    partido = get_object_or_404(EntradaPartido, pk=pk)
    tipos = partido.tipos_entrada.all()

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            tipo_entrada = get_object_or_404(TipoEntrada, pk=form.cleaned_data['tipo_entrada_id'])
            cantidad = form.cleaned_data['cantidad']

            if cantidad > tipo_entrada.stock:
                form.add_error('cantidad', 'No hay stock suficiente')
            else:
                CompraEntrada.objects.create(
                    usuario=request.user,
                    tipo_entrada=tipo_entrada,
                    cantidad=cantidad
                )
                tipo_entrada.stock -= cantidad
                tipo_entrada.save()
                return redirect('entradas:compra_exitosa')

    else:
        form = CompraForm()

    return render(request, 'entradas/detalle_partido.html', {
        'partido': partido,
        'tipos': tipos,
        'form': form,
    })

def compra_exitosa(request):
    return render(request, 'entradas/compra_exitosa.html')

def lista_partidos(request):
    partidos = EntradaPartido.objects.all().order_by('fecha_partido')
    return render(request, 'entradas/lista_partidos.html', {'partidos': partidos})


class CompraEntradaListView(LoginRequiredMixin, ListView):
    model = CompraEntrada
    template_name = 'entradas/mis_entradas.html'  
    context_object_name = 'compras'

# Solo mostrar las entradas compradas del usuario actual
    def get_queryset(self):
        return CompraEntrada.objects.filter(usuario=self.request.user).order_by('-fecha_compra')