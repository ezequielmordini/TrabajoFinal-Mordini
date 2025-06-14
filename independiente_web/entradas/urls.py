from django.urls import path
from . import views
from .views import EntradaListView, detalle_partido, compra_exitosa


app_name = 'entradas'

urlpatterns = [
    path('', views.lista_partidos, name='lista_partidos'),  # Listado de partidos
    path('partido/<int:pk>/', views.detalle_partido, name='detalle_partido'),  # Detalle y compra
    path('compra_exitosa/', views.compra_exitosa, name='compra_exitosa'),
        path('', EntradaListView.as_view(), name='entrada_list'),
    path('<int:pk>/', detalle_partido, name='detalle_partido'),
]
