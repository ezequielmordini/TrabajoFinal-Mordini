from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_register_view



app_name = 'accounts'

urlpatterns = [
   path('login/', login_register_view, name='login_register'),  # ✅ Usamos esta
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    #path('perfil/', editar_perfil, name='editar_perfil'),
]
