from django.db import models

class plato(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    precio = models.PositiveBigIntegerField()
    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.precio)