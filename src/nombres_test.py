from nombres import *

Nombres = lee_nombres('./data/frecuencias_nombres.csv')
print(Nombres)
NombresGenero = filtrar_por_genero(Nombres,'Mujer')
print(NombresGenero)
NombresGenero2 = calcular_nombres(Nombres,None)
print(NombresGenero2)