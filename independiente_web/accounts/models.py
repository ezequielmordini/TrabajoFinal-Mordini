from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/bochini.png', null=True, blank=True)
    bio = models.TextField(blank=True)
    nacimiento = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return settings.STATIC_URL + 'avatares/bochini.png'
