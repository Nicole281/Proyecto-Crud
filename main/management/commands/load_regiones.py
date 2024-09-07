import csv
from django.core.management.base import BaseCommand
from main.models import Region

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Asegúrate de especificar la codificación correcta al abrir el archivo
        with open('data/comunas.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Se salta la primera fila (encabezado)
            
            nombre_regiones = [] 
            for fila in reader:
                if fila[2] not in nombre_regiones:
                    Region.objects.create(nombre=fila[2], cod=fila[3])
                    nombre_regiones.append(fila[2])
            print(nombre_regiones)
