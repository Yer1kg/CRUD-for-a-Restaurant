from django.core.management.base import BaseCommand
from Aplicacion.menu.models import plato
from datetime import datetime

class Command(BaseCommand):
    help = 'Elimina platos que han caducado'

    def handle(self, *args, **kwargs):
        ahora = datetime.now()
        # Busca platos con fecha de caducidad en el pasado
        platos_caducados = plato.objects.filter(fecha_caducidad__lt=ahora)
        count = platos_caducados.count()
        # Elimina todos los platos caducados
        platos_caducados.delete()
        self.stdout.write(f'{count} platos eliminados.')
