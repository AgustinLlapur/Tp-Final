import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import objetos as m


voxelarray = np.zeros((15, 15, 10), dtype=bool)


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k', alpha=0.8)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


plt.show(block=False)


def plot_vehiculos(vehiculo):
    for i in range(vehiculo.cant):
        x, y, z = vehiculo.crear_vehiculo(f"{vehiculo.nombre}_{i+1}")
        voxelarray[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = True

        
        ax.clear()
        ax.voxels(voxelarray, edgecolor='k', alpha=0.8)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        
        plt.draw()
        plt.pause(0.1)  


globo = m.Globo("globo")
avion = m.Avion("avion")
zepellin = m.Zepellin("zepellin")
elevador = m.Elevador("elevador")


plot_vehiculos(globo)
plot_vehiculos(avion)
plot_vehiculos(zepellin)
plot_vehiculos(elevador)

