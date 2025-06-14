from django.urls import path
from .views import (
    NoticiaListView,
    NoticiaDetailView,
    NoticiaCreateView,
    NoticiaUpdateView,
    NoticiaDeleteView
)
from . import views


urlpatterns = [
    path('', NoticiaListView.as_view(), name='noticia_list'),
    path('<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('crear/', NoticiaCreateView.as_view(), name='noticia_create'),
    path('<int:pk>/editar/', NoticiaUpdateView.as_view(), name='noticia_update'),
    path('<int:pk>/eliminar/', NoticiaDeleteView.as_view(), name='noticia_delete'),
    path('', views.home, name='home'),
]