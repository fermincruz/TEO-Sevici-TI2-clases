import csv
import folium
from collections import namedtuple
from coordenadas import Coordenadas, calcula_distancia

Estacion = namedtuple(
    'Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')


# Función de lectura que crea una lista de Estaciones
def lee_estaciones(ruta_csv):
    ''' Lee el fichero de datos y devuelve una lista de estaciones

    ENTRADA: 
       :param fichero: Nombre y ruta del fichero a leer
       :type fichero: str

    SALIDA: 
       :return: Lista de tuplas de tipo Estacion
       :rtype: [Estacion(str, int, int, int, Coordenadas(float, float))]

    Cada estación se representa con una tupla con los siguientes valores:
    - Nombre de la estación
    - Número total de bornetas
    - Número de bornetas vacías
    - Número de bicicletas disponibles
    - Coordenadas
    Usaremos el módulo csv de la librería estándar de Python para leer el
    fichero de entrada.
    Hay que saltar la línea de encabezado del fichero y comenzar a leer los datos
    a partir de la segunda línea.
    Hay que realizar un pequeño procesamiento con los datos numéricos. Hay que
    pasar del formato cadena (que es lo que se interpreta al leer el csv) a un
    valor numérico (para poder aplicar operaciones matemáticas si fuese necesario).
    También hay que crear una tupla con nombre de tipo Coordenadas
    '''
    with open(ruta_csv, encoding='utf-8') as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for nombre, bornetas, bornetas_vacias, bicis_disponibles, latitud, longitud in lector:
            bornetas = int(bornetas)
            bornetas_vacias = int(bornetas_vacias)
            bicis_disponibles = int(bicis_disponibles)
            latitud = float(latitud)
            longitud = float(longitud)
            coordenadas = Coordenadas(latitud, longitud)
            tupla = Estacion(nombre, bornetas, bornetas_vacias,
                             bicis_disponibles, coordenadas)
            res.append(tupla)
        return res


def estaciones_bicis_libres(estaciones, k=5):
    res = []
    for e in estaciones:
        if e.bicis_disponibles >= k:
            tupla = (e.bicis_disponibles, e.nombre)
            res.append(tupla)
    res.sort(reverse=True)
    return res


def estaciones_cercanas(estaciones, ubicacion_usuario, k=5):
    # En res hay que devolver tuplas formadas por (distancia, nombre, bicis disponibles)
    res = []
    for e in estaciones:
        if e.bicis_disponibles > 0:
            # Calculo la distancia entre la ubicación del usuario
            # y la ubicación de la estación e
            distancia = calcula_distancia(ubicacion_usuario, e.coordenadas)
            res.append(
                (distancia, e.nombre, e.bicis_disponibles)
            )
    res.sort()
    return res[:k]
