from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
