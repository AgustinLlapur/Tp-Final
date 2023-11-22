import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D


class Vehiculo:
    def __init__(self, nombre, largo, ancho, alto, vida, cant, color):
        self.nombre = nombre
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.vida = vida
        self.cant = cant
        self.color = color  # Añadimos el atributo de color

    def recibir_disparo(self):
        self.vida -= 1
        return self
    
    def posicionar(self, x, y, z, voxelarray):
        voxelarray[x:x+self.largo, y:y+self.ancho, z:z+self.alto] = True

class Globo(Vehiculo):
    def __init__(self):
        super().__init__("BALLOON", 3, 3, 3, 1, 5, "blue")
        

class Zepellin(Vehiculo):
    def __init__(self):
        super().__init__("ZEPELLIN", 5, 2, 2, 3, 2, "green")

        
class Avion(Vehiculo):
    def __init__(self):
        super().__init__("PLANE", 4, 3, 2, 2, 3, "red")

    def rotar(self):
        self.ancho, self.largo = self.largo, self.ancho

    def posicionar_avion(self, x, y, z, voxelarray):
        voxelarray[x:x+4,y:y + 1,z:z +1] = True
        voxelarray[x + 2:x + 3, y - 1:y + 2, z:z +1] = True
        voxelarray[x:x+1,y:y + 1,z:z +2] = True

class Elevador(Vehiculo):
    def __init__(self):
        super().__init__("ELEVATOR", 1, 1, 10, 4, 1, "purple")

class Mapa:
    def __init__(self):
        self.x_size = 15
        self.y_size = 15
        self.z_size = 10
        self.voxelarray = np.zeros((self.x_size, self.y_size, self.z_size), dtype=bool)
        self.colors = np.empty((self.x_size, self.y_size, self.z_size), dtype=object)  # RGBA values
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d') 

    def verificar_limites(self, x, y, z, largo, ancho, alto, es_avion=False):
        if es_avion:
            alas = (y - 1 >= 0 and y + 1 <= self.y_size)
            return (x + 4 <= self.x_size and y + 2 <= self.y_size and z + 2 <= self.z_size) and alas
        return x + largo <= self.x_size and y + ancho <= self.y_size and z + alto <= self.z_size

    def verificar_colision(self, x, y, z, largo, ancho, alto, es_avion=False):
        if not self.verificar_limites(x, y, z, largo, ancho, alto, es_avion):
            print("Las coordenadas exceden los límites del mapa.")
            return True
        if es_avion:
            return np.any(self.voxelarray[x:x+4, y:y+1, z:z+1]) or \
                   np.any(self.voxelarray[x+2:x+3, y-1:y+2, z:z+1]) or \
                   np.any(self.voxelarray[x:x+1, y:y+1, z:z+2])
        else:
            return np.any(self.voxelarray[x:x+largo, y:y+ancho, z:z+alto])

    def obtener_coordenadas_usuario(self, nombre_vehiculo, num_vehiculo):
        try:
            if nombre_vehiculo == "ELEVATOR":
                x, y = map(int, input(f"Ingrese la posición para {nombre_vehiculo}_{num_vehiculo}: ").split())
                return x, y, 0, num_vehiculo
            else:
                x, y, z = map(int, input(f"Ingrese la posición para {nombre_vehiculo}_{num_vehiculo}: ").split())
                return x, y, z, num_vehiculo
        except ValueError:
            print("Error: Ingrese números enteros para las coordenadas.")
            return None, None, None

    def obtener_coordenadas_pc(self):
        x, y, z = ran.randint(0,15), ran.randint(0,15), ran.randint(0,10)
        return x, y, z

    def dibujar(self):
        self.ax.clear()  # Limpiar los ejes en lugar de toda la figura
        self.ax.voxels(self.voxelarray, edgecolor='k', facecolors=self.colors, alpha=0.8)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        plt.draw()
        plt.pause(0.01)

    def plot_vehiculos_usuario(self, vehiculo):
        for i in range(vehiculo.cant):
            while True:
                x, y, z, numero = self.obtener_coordenadas_usuario(vehiculo.nombre, i)

                if x is None or y is None or z is None:
                    continue

                es_avion = (vehiculo.nombre == "PLANE")

                if self.verificar_limites(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                    if not self.verificar_colision(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                        if es_avion:
                            self.colors[x:x+4, y:y+1, z:z+1] = vehiculo.color
                            self.colors[x+2:x+3, y-1:y+2, z:z+1] = vehiculo.color
                            self.colors[x:x+1, y:y+1, z:z+2] = vehiculo.color
                            vehiculo.posicionar_avion(x, y, z, self.voxelarray)

                        else:
                            vehiculo.posicionar(x, y, z, self.voxelarray)
                            self.colors[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = vehiculo.color

                        self.dibujar()
                        break

                    else:
                        print("¡Colisión detectada! Por favor, ingrese nuevas coordenadas.")
                else:
                    print("Las coordenadas exceden los límites del mapa. Por favor, ingrese nuevas coordenadas.")
        
mapa = Mapa()

vehiculos = [Globo(), Avion(), Zepellin(), Elevador()]

for v in vehiculos:
    mapa.plot_vehiculos_usuario(v)

plt.show()