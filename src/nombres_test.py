from nombres import *

Nombres = lee_nombres('./data/frecuencias_nombres.csv')
print(Nombres)
NombresGenero = filtrar_por_genero(Nombres,'Mujer')
print(NombresGenero)
NombresGenero2 = calcular_nombres(Nombres)
print(NombresGenero2)
TopNombres = calcular_top_nombres_de_año(Nombres,2015,20,'Mujer')
print(TopNombres)