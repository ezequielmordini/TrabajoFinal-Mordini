from django.db import models
from django.contrib.auth.models import User

class EntradaPartido(models.Model):
    titulo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_partido = models.DateTimeField()
    imagen = models.ImageField(upload_to='entradas', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha_partido.strftime('%d/%m/%Y')}"

class TipoEntrada(models.Model):
    partido = models.ForeignKey(EntradaPartido, on_delete=models.CASCADE, related_name='tipos_entrada')
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.partido.titulo}"

class CompraEntrada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_entrada = models.ForeignKey(TipoEntrada, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_entrada} x {self.cantidad}"
