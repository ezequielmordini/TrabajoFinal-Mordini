from django.urls import path, include
from . import views
from .views import  detalle_partido, compra_exitosa
from .views import CompraEntradaListView
from .views import (
    EntradaPartidoListView,
    EntradaPartidoCreateView,
    EntradaPartidoUpdateView,
    EntradaPartidoDeleteView,
)



app_name = 'entradas'

urlpatterns = [
    path('', views.lista_partidos, name='lista_partidos'),  
    path('partido/<int:pk>/', views.detalle_partido, name='detalle_partido'),  
    path('compra_exitosa/', views.compra_exitosa, name='compra_exitosa'),
    path('<int:pk>/', detalle_partido, name='detalle_partido'),
    #path('mis-compras/', mis_compras, name='mis_compras'),
    path('mis-entradas/', CompraEntradaListView.as_view(), name='mis_entradas'),

    path('admin/partidos/', EntradaPartidoListView.as_view(), name='admin_partido_list'),
    path('admin/partidos/nuevo/', EntradaPartidoCreateView.as_view(), name='admin_partido_create'),
    path('admin/partidos/<int:pk>/editar/', EntradaPartidoUpdateView.as_view(), name='admin_partido_edit'),
    path('admin/partidos/<int:pk>/borrar/', EntradaPartidoDeleteView.as_view(), name='admin_partido_delete'),

]
