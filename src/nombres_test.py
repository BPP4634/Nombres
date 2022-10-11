from nombres import *

Nombres = lee_nombres('./data/frecuencias_nombres.csv')
print(Nombres)
NombresGenero = filtrar_por_genero(Nombres,'Mujer')
print(NombresGenero)
NombresGenero2 = calcular_nombres(Nombres)
print(NombresGenero2)
TopNombres = calcular_top_nombres_de_año(Nombres,2015,20,'Mujer')
print(TopNombres)
NombresAmbos = calcular_nombres_ambos_generos(Nombres)
print(NombresAmbos)
NombresCom = calcular_nombres_compuestos(Nombres)
print(NombresCom)