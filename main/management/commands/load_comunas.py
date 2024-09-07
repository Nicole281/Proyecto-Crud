import csv
from django.core.management.base import BaseCommand
from main.models import Comuna

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Abrir el archivo especificando la codificación correcta
        with open('data/comunas.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Saltar la primera línea (encabezado)
            
            for fila in reader:
                # Crear la instancia de Comuna con los valores del CSV
                Comuna.objects.create(nombre=fila[0], cod=fila[1], region_id=fila[3])
