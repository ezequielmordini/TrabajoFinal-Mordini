from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True, null=True)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Partido(models.Model):
    equipo_local = models.CharField(max_length=100)
    escudo_local = models.ImageField(upload_to='escudos/')
    equipo_visitante = models.CharField(max_length=100)
    escudo_visitante = models.ImageField(upload_to='escudos/')
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"

