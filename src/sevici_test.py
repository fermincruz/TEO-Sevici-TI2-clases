import sevici
from coordenadas import Coordenadas


def test_lee_estaciones():
    print("Test de la función lee_estaciones")
    datos = sevici.lee_estaciones("data/estaciones.csv")
    print(f"Se han leído {len(datos)} estaciones.")
    print("Mostrando las 3 primeras:")
    for e in datos[:3]:
        print("\t", e)
    print("Mostrando las 3 últimas:")
    for e in datos[-3:]:
        print("\t", e)
    print("=========================================================")
    print()

# TODO: Implementar test_estaciones_bicis_libres


def test_estaciones_bicis_libres():
    print("Test de la función estaciones_bicis_libres")
    datos = sevici.lee_estaciones("data/estaciones.csv")
    estaciones_con_bicis = sevici.estaciones_bicis_libres(datos)
    print("Se muestran las primeras 10 estaciones obtenidas:")
    for e in estaciones_con_bicis[:10]:
        print("\t", e)
    print("Se muestran ahora las 3 últimas estaciones obtenidas:")
    for e in estaciones_con_bicis[-3:]:
        print("\t", e)
    print("=========================================================")
    print()


def test_estaciones_cercanas():
    print("Test de la función estaciones_cercanas")
    datos = sevici.lee_estaciones("data/estaciones.csv")
    estaciones_con_bicis = sevici.estaciones_cercanas(
        datos, Coordenadas(37.357659, -5.9863))
    print("Se muestran las estaciones obtenidas:")
    for e in estaciones_con_bicis:
        print("\t", e)
    print("=========================================================")
    print()


# TODO: Implementar test_estaciones_cercanas
if __name__ == '__main__':
    test_lee_estaciones()
    # TODO: Invocar a las nuevas funciones de test
    test_estaciones_bicis_libres()
    test_estaciones_cercanas()
