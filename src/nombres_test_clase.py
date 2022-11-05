from nombres_clase import *

def main():
    Nombres = lee_nombres('./data/frecuencias_nombres.csv')
    test_lectura_frecuencia_nombres(Nombres)
    print(filtrar_por_genero(Nombres,'MUJER'))
    print(calcular_nombres(Nombres))
    print(calcular_top_nombres_de_año(Nombres,2017,28))
    print(calcular_nombres_ambos_generos(Nombres))
    print(calcular_nombres_compuestos(Nombres))
    print(calcular_nombre_mas_frecuente_por_año(Nombres, 'HOMBRE'))
    print(calcular_frecuencia_por_año(Nombres,'JORGE'))
    mostrar_evolucion_por_año(Nombres,"IKER")
    print(calcular_frecuencia_acumulada(Nombres,"ABRIL"))
    print(calcular_frecuencias_por_nombre(Nombres))
    mostrar_frecuencias_nombres(Nombres,20)

def test_lectura_frecuencia_nombres(listado):
    print("Se han leído", len(listado), "elementos.")
    print("Primero:", listado[0])
    print("Último:", listado[1])

if __name__ == '__main__':
    main()