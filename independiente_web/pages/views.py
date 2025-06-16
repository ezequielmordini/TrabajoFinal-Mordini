from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Noticia, Partido
from .forms import NoticiaForm
from django.shortcuts import render
from entradas.models import EntradaPartido

from .models import Noticia

def home(request):
    noticias = Noticia.objects.order_by('-fecha')[:5]
    print("Noticias encontradas:", noticias)

    proximo_partido = Partido.objects.order_by('fecha', 'hora').first()
    print("Próximo partido:", proximo_partido)

    return render(request, 'home.html', {
        'noticias': noticias,
        'proximo_partido': proximo_partido
    })




class NoticiaListView(ListView):
    model = Noticia
    template_name = 'pages/noticia_list.html'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'pages/noticia_detail.html'

class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'pages/noticia_form.html'
    success_url = reverse_lazy('noticia_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'pages/noticia_form.html'
    success_url = reverse_lazy('noticia_list')

class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = 'pages/noticia_confirm_delete.html'
    success_url = reverse_lazy('noticia_list')
