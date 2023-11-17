import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import objetos as m

def verificar_colision(voxelarray, x, y, z, largo, ancho, alto):
    return np.any(voxelarray[x:x+largo, y:y+ancho, z:z+alto])

def plot_vehiculos(vehiculo, voxelarray):
    for i in range(vehiculo.cant):
        while True:
            x, y, z = vehiculo.crear_vehiculo(f"{vehiculo.nombre}_{i+1}")
            if not verificar_colision(voxelarray, x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto):
                voxelarray[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = True
                break
            else:
                print("¡Colisión detectada! Por favor, ingrese nuevas coordenadas.")

        ax.clear()
        ax.voxels(voxelarray, edgecolor='k')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.draw()
        plt.pause(0.1)  

# Crear el array de voxels
voxelarray = np.zeros((15, 15, 10), dtype=bool)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show(block=False)

globo = m.Globo("globo")
avion = m.Avion("avion")
zepellin = m.Zepellin("zepellin")
elevador = m.Elevador("elevador")

plot_vehiculos(globo, voxelarray)
plot_vehiculos(avion, voxelarray)
plot_vehiculos(zepellin, voxelarray)
plot_vehiculos(elevador, voxelarray)
