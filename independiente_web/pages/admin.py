from django.contrib import admin
from .models import Noticia
from .models import Partido


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha')
    search_fields = ('titulo', 'subtitulo', 'cuerpo')   

admin.site.register(Partido)
