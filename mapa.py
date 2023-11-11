import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import objetos as obj
import main 


def mapa_vacio():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_title("Mapa Aliade")
    # Establecer los límites de los ejes x, y, z
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_zlim(0, 10)

    # Establecer los marcadores de los ejes x, y, z como enteros
    ax.set_xticks([i for i in range(0, 16, 2)])
    ax.set_yticks([i for i in range(0, 16, 2)])
    ax.set_zticks([i for i in range(0, 11, 2)])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
  
    plt.legend()
    plt.show()


mapa_vacio()
    