'''10. calcular_frecuencia_acumulada: recibe una lista de tuplas de tipo FrecuenciaNombre y un nombre
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
    namegen = set()
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

def calcular_nombres_ambos_generos(Nombres):
    genhset = set()
    genmset = set()
    genh = filtrar_por_genero(Nombres, 'Hombre')
    for gen in genh:
        genhset.add(gen[1])
    genm = filtrar_por_genero(Nombres, 'Mujer')
    for gen in genm:
        genmset.add(gen[1])
    return genhset & genmset

def calcular_nombres_compuestos(Nombres,genero=None):
    calnomcom = set()
    if genero!=None:
        Nombres = filtrar_por_genero(Nombres,genero)
    for nombre in Nombres:
        if ' ' in nombre.nombre:
            calnomcom.add(nombre.nombre)
    return calnomcom

def calcular_nombre_mas_frecuente_por_año(Nombres, genero=None):
    nomfrec = []
    nomfrectrue = []
    listadepaso = []
    if genero!=None:
        Nombres = filtrar_por_genero(Nombres,genero)
    for nombre in Nombres:
        nomfrec.append((nombre.anyo,nombre.nombre,nombre.frecuencia))
    nomfrec.sort()
    n = nomfrec[0][0]
    for nombre in nomfrec:
        if nombre[0]==n:
            listadepaso.append(nombre)
        else:
            listadepaso = sorted(listadepaso, key=lambda nom : nom[2], reverse = True)
            nomfrectrue.append(listadepaso[0])
            listadepaso.clear()
            listadepaso.append(nombre)
            n=n+1
    listadepaso = sorted(listadepaso, key=lambda nom : nom[2], reverse = True)
    nomfrectrue.append(listadepaso[0])
    listadepaso.clear()
    return nomfrectrue

def calcular_frecuencia_por_año(Nombres,nombredado):
    Nombres.sort()
    n=Nombres[0][0]
    listadepaso = []
    frecporan = []
    for nombre in Nombres:
        if nombre.anyo == n and nombre.nombre == nombredado:
            listadepaso.append(nombre.frecuencia)
        elif nombre.nombre==nombredado:
            frecporan.append((n,sum(listadepaso)))
            listadepaso.clear()
            listadepaso.append(nombre.frecuencia)
            n=nombre.anyo
    frecporan.append((n,sum(listadepaso)))
    listadepaso.clear()
    return frecporan

def mostrar_evolucion_por_año(Nombres,nombre):
    años = []
    frecuencias = []
    for año, frecuencia in calcular_frecuencia_por_año(Nombres,nombre):
        años.append(año)
        frecuencias.append(frecuencia)
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()

def calcular_frecuencia_acumulada(Nombres,nombre):
    frecuencia = []
    for nom in calcular_frecuencia_por_año(Nombres,nombre):
        frecuencia.append(nom[1])
    return sum(frecuencia)