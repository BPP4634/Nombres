from nombres import *

def main():
    Nombres = lee_nombres('./data/frecuencias_nombres.csv')
    print(Nombres)
    print(filtrar_por_genero(Nombres,'Mujer'))
    print(calcular_nombres(Nombres))
    print(calcular_top_nombres_de_año(Nombres,2015,20,'Mujer'))
    print(calcular_nombres_ambos_generos(Nombres))
    print(calcular_nombres_compuestos(Nombres))
    print(calcular_nombre_mas_frecuente_por_año(Nombres, 'Mujer'))
    print(calcular_frecuencia_por_año(Nombres,'ABRIL'))
    mostrar_evolucion_por_año(Nombres,"IKER")
    print(calcular_frecuencia_acumulada(Nombres,"ABRIL"))
    print(calcular_frecuencias_por_nombre(Nombres))
    mostrar_frecuencias_nombres(Nombres,20)

if __name__ == '__main__':
    main()