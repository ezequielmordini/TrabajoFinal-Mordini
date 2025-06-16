from django.urls import path, include
from . import views
from .views import  detalle_partido, compra_exitosa
from .views import CompraEntradaListView



app_name = 'entradas'

urlpatterns = [
    path('', views.lista_partidos, name='lista_partidos'),  
    path('partido/<int:pk>/', views.detalle_partido, name='detalle_partido'),  
    path('compra_exitosa/', views.compra_exitosa, name='compra_exitosa'),
    path('<int:pk>/', detalle_partido, name='detalle_partido'),
    #path('mis-compras/', mis_compras, name='mis_compras'),
    path('mis-entradas/', CompraEntradaListView.as_view(), name='mis_entradas'),
]
