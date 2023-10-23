from collections import namedtuple
import math

'''
Tupla con nombre que representa una coordenada con latitud y longitud en grados
'''
Coordenadas = namedtuple('Coordenadas','latitud, longitud')

    
#funcion para el cálculo de la calcular_distancia
def calcula_distancia(c1, c2):
    '''
    Toma como entrada las coordenadas de dos puntos y devuelve la distancia euclídea. 
    @param coordenada1: coordenadas de un punto.
    @type coordenada1: Coordenadas(float, float)
    @param coordenada2: coordenadas de un punto 
    @type coordenada2: Coordenadas(float, float)
    @return: La distancia euclídea entre los dos puntos
    @rtype: float
    '''
    return math.sqrt((c1.latitud - c1.latitud)**2 + 
                     (c2.longitud - c1.longitud)**2)


def calcular_media_coordenadas (coordenadas):
    '''
    Calcula un punto cuya latitud es la media de las latitudes de las coordenadas que
    se pasan como parámetro y cuya longitud es la media de las longitudes de las coordenadas que se pasan
    como parámetro.

    @param coordenadas: lista de tuplas Coordenadas(latitud, longitud)
    @type: Coordenadas (float, float)
    @return:   Una tupla (media_latitud, media_longitud) con la media de las latitudes de los centros
    y la media de las longitudes.
    @rtype: Coordenadas (float, float)
    '''
    num_elem = len(coordenadas)
    media_latitud = sum(c.latitud for c in coordenadas)/num_elem
    media_longitud = sum(c.longitud for c in coordenadas)/num_elem
    return Coordenadas(media_latitud, media_longitud)
