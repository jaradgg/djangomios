from django.db import models

# Create your models here.
# mapeo orm

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ('servicio')
        verbose_name_plural = ("servicios")
    
    def __str__(self):
        return self.titulo