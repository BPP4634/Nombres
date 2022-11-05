import csv
from matplotlib import pyplot as plt
from collections import namedtuple

def parsea_genero(cadena):
    return cadena.upper()

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'anyo,nombre,frecuencia,genero')

def lee_nombres(fichero):
    Nombres = []
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for anyo,nombre,frecuencia,genero in lector:
            anyo = int(anyo)
            frecuencia = int(frecuencia)
            genero = parsea_genero(genero)
            Nombres.append(FrecuenciaNombre(anyo,nombre,frecuencia,genero))
        return Nombres

def filtrar_por_genero(nombres, genero):
    result = []
    for nombre in nombres:
        if nombre.genero == genero:
            result.append(nombre)
    return result

def calcular_nombres(nombres, genero=None):
    result = set()
    if genero!=None:
        aux = filtrar_por_genero(nombres, genero)
    else:
        aux = nombres
    for nombre in aux:
        result.add(nombre[1])
    return result

def calcular_top_nombres_de_año(nombres, anyo, lim=10, genero=None):
    result = []
    if genero!=None:
        nombresfil = filtrar_por_genero(nombres, genero)
    else:
        nombresfil = nombres
    for nombre in nombresfil:
        if nombre.anyo == anyo:
            result.append((nombre.nombre,nombre.frecuencia))
    result = sorted(result, key=lambda nom : nom[1], reverse = True)
    return result[:lim]

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

def calcular_nombre_mas_frecuente_por_año(nombres, genero=None):
    result = dict()
    if genero!=None:
        nombresfil = filtrar_por_genero(nombres,genero)
    else:
        nombresfil = nombres
    for nombre in nombresfil:
        if nombre.anyo in result:
            result[nombre.anyo] = max(result[nombre.anyo],nombre, key= lambda x:x.frecuencia)
        else:
            result[nombre.anyo] = nombre
    result = sorted(result.items(), reverse=True)
    return result

#[(nombre.nombre,nombre.frecuencia)]



def calcular_frecuencia_por_año(nombres,nombredado):
    result={}
    for nombre in nombres:
        if nombre.nombre == nombredado:
            if nombre.anyo in result:
                result[nombre.anyo] += nombre.frecuencia
            else:
                result[nombre.anyo] = nombre.frecuencia
    return sorted(result.items())

def mostrar_evolucion_por_año(nombres,nombre):
    años = []
    frecuencias = []
    for año, frecuencia in calcular_frecuencia_por_año(nombres,nombre):
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

def calcular_frecuencias_por_nombre(nombres):
    result = dict()
    for nombre in nombres:
        if nombre.nombre in result:
            result[nombre.nombre] += nombre.frecuencia
        else:
            result[nombre.nombre] = nombre.frecuencia
    return result

def mostrar_frecuencias_nombres(Nombres,limite=10):
    diccionario = calcular_frecuencias_por_nombre(Nombres)
    listado = sorted(diccionario.items(), key=lambda num : num[1], reverse = True)[:limite]
    claves = [clave for clave,_ in listado]
    valores = [valor for _,valor in listado]
    plt.bar(claves, valores)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()