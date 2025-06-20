from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    ESTADO_SOCIO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    
    estado_socio = models.CharField(max_length=10, choices=ESTADO_SOCIO_CHOICES, default='activo')
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return settings.STATIC_URL + 'avatares/bochini.png'
