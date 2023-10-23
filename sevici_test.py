import sevici


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


if __name__ == '__main__':
    test_lee_estaciones()
