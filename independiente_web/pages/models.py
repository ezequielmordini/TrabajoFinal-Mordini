from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    imagen = models.ImageField(upload_to='noticias/')
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo