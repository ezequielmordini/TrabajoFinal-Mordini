from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Noticia
from .forms import NoticiaForm
from django.shortcuts import render


def home(request):
    entradas = Entrada.objects.order_by('-fecha')[:5]  # Últimas 5
    return render(request, 'home.html', {'entradas': entradas})


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
