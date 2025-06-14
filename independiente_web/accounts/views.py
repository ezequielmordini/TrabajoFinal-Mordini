from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from .models import Perfil
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import PerfilForm



def login_register_view(request):
    if request.method == 'POST':
        if 'login_submit' in request.POST:
            # Procesar login
            login_form = AuthenticationForm(request, data=request.POST)
            registro_form = RegistroForm()
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
        elif 'register_submit' in request.POST:
            # Procesar registro
            registro_form = RegistroForm(request.POST)
            login_form = AuthenticationForm()
            if registro_form.is_valid():
                user = registro_form.save()
                login(request, user)
                return redirect('home')
    else:
        login_form = AuthenticationForm()
        registro_form = RegistroForm()

    context = {
        'login_form': login_form,
        'registro_form': registro_form,
    }
    return render(request, 'accounts/login_register.html', context)

@login_required
def mi_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('accounts:mi_perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'accounts/editar_perfil.html', {'form': form})
