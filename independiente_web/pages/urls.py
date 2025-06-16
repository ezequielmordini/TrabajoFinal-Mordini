from django.urls import path
from .views import (
    NoticiaListView,
    NoticiaDetailView,
    NoticiaCreateView,
    NoticiaUpdateView,
    NoticiaDeleteView,
    home
)

urlpatterns = [
    path('', home, name='home'),  
    path('noticias/', NoticiaListView.as_view(), name='noticia_list'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('noticias/crear/', NoticiaCreateView.as_view(), name='noticia_create'),
    path('noticias/<int:pk>/editar/', NoticiaUpdateView.as_view(), name='noticia_update'),
    path('noticias/<int:pk>/eliminar/', NoticiaDeleteView.as_view(), name='noticia_delete'),
]
