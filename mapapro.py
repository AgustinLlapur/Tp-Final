import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import objetos as m

def verificar_coordenadas(x, y, z, largo, ancho, alto, limites):
    return x + largo <= limites[0] and y + ancho <= limites[1] and z + alto <= limites[2]

def verificar_colision(voxelarray, x, y, z, largo, ancho, alto, limites):
    if not verificar_coordenadas(x, y, z, largo, ancho, alto, limites):
        print("Las coordenadas exceden los límites del mapa.")
        return True
    return np.any(voxelarray[x:x+largo, y:y+ancho, z:z+alto])

def obtener_coordenadas(nombre_vehiculo, num_vehiculo):
    try:
        x, y, z = map(int, input(f"Ingrese la posición para {nombre_vehiculo}_{num_vehiculo}: ").split())
        return x, y, z
    except ValueError:
        print("Error: Ingrese números enteros para las coordenadas.")
        return None, None, None

def plot_vehiculos(vehiculo, voxelarray):
    for i in range(1, vehiculo.cant + 1): 
        while True:
            x, y, z = obtener_coordenadas(vehiculo.nombre, i)
            if x is None or y is None or z is None:
                continue
            
            limites_mapa = voxelarray.shape
            if verificar_coordenadas(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, limites_mapa):
                if not verificar_colision(voxelarray, x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, limites_mapa):
                    if vehiculo.nombre == "Avion": # Slicing especifico para el avion
                        voxelarray[x:x+4,y:y + 1,z:z +1] = True
                        voxelarray[x + 2:x + 3, y - 1:y + 2, z:z +1] = True
                        voxelarray[x:x+1,y:y + 1,z:z +2] = True
                    else:
                        voxelarray[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = True

                    color = vehiculo.color  # Accedemos al color definido en el objeto vehículo
                    ax.clear()
                    ax.voxels(voxelarray, edgecolor='k', facecolors=color, alpha=0.8)  
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

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show(block=False)

globo = m.Globo("Globo")
avion = m.Avion("Avion")
zepellin = m.Zepellin("Zepellin")
elevador = m.Elevador("Elevador")

# Colocamos los vehículos en el mapa

plot_vehiculos(globo, voxelarray)
plot_vehiculos(avion, voxelarray)
plot_vehiculos(zepellin, voxelarray)
plot_vehiculos(elevador, voxelarray)

