import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random as ran

def verificar_coordenadas(x, y, z, largo, ancho, alto, limites):
    """
    Verifica si las coordenadas del vehículo están dentro de los límites del mapa.

    Parámetros:
    x, y, z (int): Coordenadas del vehículo.
    largo, ancho, alto (int): Dimensiones del vehículo.
    limites (tuple): Límites del mapa en cada dimensión.

    Retorna:
    bool: True si las coordenadas están dentro de los límites, False en caso contrario.
    """
    return x + largo <= limites[0] and y + ancho <= limites[1] and z + alto <= limites[2]

def verificar_colision(voxelarray, x, y, z, largo, ancho, alto, limites):
    if not verificar_coordenadas(x, y, z, largo, ancho, alto, limites):
        print("Las coordenadas exceden los límites del mapa.")
        return True
    return np.any(voxelarray[x:x+largo, y:y+ancho, z:z+alto])

def obtener_coordenadas(nombre_vehiculo, num_vehiculo):
    try:
        x, y, z = ran.randint(0,15), ran.randint(0,15), ran.randint(0,10)
        # map(int, input(f"Ingrese la posición para {nombre_vehiculo}_{num_vehiculo}: ").split())
        return x, y, z
    except ValueError:
        print("Error: Ingrese coordenadas validas.")
        return None, None, None

