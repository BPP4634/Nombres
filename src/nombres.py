'''
5. calcular_nombres_ambos_generos: recibe una lista de tuplas de tipo FrecuenciaNombre, y
devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.
6. calcular_nombres_compuestos: recibe una lista de tuplas de tipo FrecuenciaNombre y un género
de tipo str, y devuelve un conjunto {str} con los nombres que contienen más de una palabra. El
género puede ser ‘Hombre’, ‘Mujer’ o tener un valor None, en cuyo caso se incluyen en el conjunto
todos los nombres. El valor por defecto del género es None.
7. calcular_nombre_mas_frecuente_por_año: recibe una lista de tuplas de tipo FrecuenciaNombre y
un género de tipo str, y devuelve una lista de tuplas (año, nombre, frecuencia) de tipo (int, str, int)
ordenada por año con el nombre más frecuente de cada año. El género puede ser ‘Hombre’,
‘Mujer’ o tener un valor None, en cuyo caso se incluyen en la lista todos los nombres. El valor por
defecto del género es None. Se calculará en primer lugar la lista de años y, posteriormente, se
buscará el nombre más frecuente para cada año.
8. calcular_frecuencia_por_año: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de
tipo str, y devuelve una lista de tuplas (año, frecuencia) de tipo (int, int) ordenada por año con la
frecuencia del nombre en cada año. En el caso de que un nombre se use para hombres y mujeres,
se sumarán ambas frecuencias.
9. mostrar_evolucion_por_año: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre de
tipo str, y genera un gráfico con la evolución de la frecuencia del nombre a lo largo de los años
(Figura 2). Se usarán las siguientes instrucciones para generar la gráfica:
plt.plot(años, frecuencias)
plt.title("Evolución del nombre '{}'".format(nombre))
plt.show()
Ejercicio: Nombres 3
Donde años y frecuencias se extraen del resultado de la función calcular_frecuencia_por_año.
10. calcular_frecuencia_acumulada: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre
de tipo str, y devuelve la frecuencia acumulada del nombre en todos los años.
11. calcular_frecuencias_por_nombre: recibe una lista de tuplas de tipo FrecuenciaNombre, y
devuelve un diccionario {str: int} que relaciona cada nombre con la frecuencia acumulada del
nombre.
12. mostrar_frecuencias_nombres: recibe una lista de tuplas de tipo FrecuenciaNombre y un número
límite de tipo int, y genera un diagrama de barras con las frecuencias de los nombres más
populares, en orden decreciente de popularidad y con un máximo de límite nombres (Figura 3). El
valor por defecto del límite es 10. Se usarán las siguientes instrucciones para generar la gráfica:
plt.bar(nombres, frecuencias)
plt.xticks(rotation=80)
plt.title("Frecuencia de los {} nombres más comunes".format(limite))
plt.show()'''

import csv
from matplotlib import pyplot as plt
from collections import namedtuple

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'anyo,nombre,frecuencia,genero')

def lee_nombres(fichero):
    Nombres = []
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for anyo,nombre,frecuencia,genero in lector:
            anyo = int(anyo)
            frecuencia = int(frecuencia)
            Nombres.append(FrecuenciaNombre(anyo,nombre,frecuencia,genero))
        return Nombres

def filtrar_por_genero(Nombres, genero):
    nomgen = []
    for nombre in Nombres:
        if nombre.genero == genero:
            nomgen.append(nombre)
    return nomgen

def calcular_nombres(Nombres, genero=None):
    namegen = {set}
    if genero!=None:
        Nombres = filtrar_por_genero(Nombres, genero)
    for nombre in Nombres:
        namegen.add(nombre[1])
    return namegen

def calcular_top_nombres_de_año(Nombres, anyo, lim=10, genero=None):
    topnom = []
    if genero!=None:
        Nombres = filtrar_por_genero(Nombres, genero)
    for nombre in Nombres:
        if nombre.anyo == anyo:
            topnom.append((nombre.nombre,nombre.frecuencia))
    topnom = sorted(topnom, key=lambda nom : nom[1], reverse = True)
    return topnom[:lim]