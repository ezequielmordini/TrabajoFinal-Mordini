from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm

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
