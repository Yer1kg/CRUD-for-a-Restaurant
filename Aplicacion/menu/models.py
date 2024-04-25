from django.db import models
from django.utils import timezone
from datetime import timedelta

def default_fecha_caducidad():
    return timezone.now() + timedelta(minutes=1)

class plato(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    precio = models.PositiveBigIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Usar la función en lugar del lambda para el valor predeterminado
    fecha_caducidad = models.DateTimeField(default=default_fecha_caducidad)



    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.precio)