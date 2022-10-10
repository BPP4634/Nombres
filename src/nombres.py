import csv
from matplotlib import pyplot as plt
from collections import namedtuple

Nombre = namedtuple('Nombre', 'anyo,nombre,frecuencia,genero')

def lee_nombres(fichero):
    Nombres = []
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for anyo,nombre,frecuencia,genero in lector:
            anyo = int(anyo)
            frecuencia = int(frecuencia)
            Nombres.append(Nombre(anyo,nombre,frecuencia,genero))
        return Nombres