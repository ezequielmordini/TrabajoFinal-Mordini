from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio', 'nacimiento']
        
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

