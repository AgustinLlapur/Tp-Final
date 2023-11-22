import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import objetos as m

def verificar_limites(x, y, z, largo, ancho, alto, limites, es_avion=False):
    if es_avion:
        alas = (y - 1 >= 0 and y + 1 <= limites[0])
        return (x + 4 <= limites[0] and y + 2 <= limites[1] and z + 2 <= limites[2]) and alas
    return x + largo <= limites[0] and y + ancho <= limites[1] and z + alto <= limites[2]

def verificar_colision(voxelarray, x, y, z, largo, ancho, alto, limites, es_avion=False):
    if not verificar_limites(x, y, z, largo, ancho, alto, limites, es_avion):
        print("Las coordenadas exceden los límites del mapa.")
        return True
    if es_avion:
        return np.any(voxelarray[x:x+4,y:y + 1,z:z +1]) or \
               np.any(voxelarray[x+2:x+3, y-1:y+2, z:z+1]) or \
               np.any(voxelarray[x:x+1, y:y+1, z:z+2])
    else:
        return np.any(voxelarray[x:x+largo, y:y+ancho, z:z+alto])

def obtener_coordenadas(nombre_vehiculo, num_vehiculo):
    try:
        if nombre_vehiculo == "Elevador":
            x, y = map(int, input(f"Ingrese la posición para {nombre_vehiculo}_{num_vehiculo}: ").split())
            return x, y, 0, num_vehiculo
        else:
            x, y, z = map(int, input(f"Ingrese la posición para {nombre_vehiculo}_{num_vehiculo}: ").split())
            return x, y, z, num_vehiculo
    except ValueError:
        print("Error: Ingrese números enteros para las coordenadas.")
        return None, None, None

def plot_vehiculos(vehiculo, voxelarray, colors):
    for i in range(0, vehiculo.cant): 
        while True:
            x, y, z, numero = obtener_coordenadas(vehiculo.nombre, i)
            
            if x is None or y is None or z is None:
                continue
            
            limites_mapa = voxelarray.shape
            es_avion = (vehiculo.nombre == "PLANE")

            if verificar_limites(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, limites_mapa, es_avion):
                if not verificar_colision(voxelarray, x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, limites_mapa, es_avion):
                    if es_avion: # Slicing especifico para el avion
                        colors[x:x+4,y:y + 1,z:z +1] = vehiculo.color
                        colors[x + 2:x + 3, y - 1:y + 2, z:z +1] = vehiculo.color
                        colors[x:x+1,y:y + 1,z:z +2] = vehiculo.color
                        vehiculo.posicionar_avion(x, y, z, voxelarray)
                        
                    else:
                        vehiculo.posicionar(x, y, z, voxelarray)
                        colors[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = vehiculo.color
                    ax.clear()
                    ax.voxels(voxelarray, edgecolor='k', facecolors=colors, alpha=0.8)  
                    ax.set_xlabel("X")
                    ax.set_ylabel("Y")
                    ax.set_zlabel("Z")
                    plt.draw()
                    plt.pause(0.1) 
                    break  
                else:
                    print("¡Colisión detectada! Por favor, ingrese nuevas coordenadas.")
            else:
                print("Las coordenadas exceden los límites del mapa. Por favor, ingrese nuevas coordenadas.")


# Crear el array de voxels
voxelarray = np.zeros((15, 15, 10), dtype=bool)
colors = np.empty(voxelarray.shape, dtype=object)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show(block=False)

globo = m.Globo()
avion = m.Avion()
zepellin = m.Zepellin()
elevador = m.Elevador()

# Colocamos los vehículos en el mapa
vehiculos = [globo, avion, zepellin, elevador]

for vehiculo in vehiculos:
    plot_vehiculos(vehiculo, voxelarray, colors)

# plt.show()