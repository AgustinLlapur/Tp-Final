import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D
import mapa as m


class Player:
    def __init__(self, mapa, vehiculos: dict) -> None:
        self.mapa = mapa
        self.vehiculos = vehiculos

    def dispara_usuario(self):
            while True:
                try:
                    x, y, z = ran.randint(0, 14), ran.randint(0, 14), ran.randint(0, 9)

                    #x, y, z, = map(int, input("Ingrese las coordenadas para disparar: ").split())
                    
                    if x < 0 or x > 14 or y < 0 or y > 14 or z < 0 or z > 9:
                        print("Las coordenadas exceden los límites del mapa.")
                        continue
                except ValueError:
                    print("Ingrese correctamente las coordenadas formato: (x y z)")
                    continue
                return x, y, z
            
    def verificar_limites(self, x, y, z, largo, ancho, alto, es_avion=False):
        if es_avion:
            alas = (y - 1 >= 0 and y + 1 <= self.mapa.y_size)
            return (x + 4 <= self.mapa.x_size and y + 2 <= self.mapa.y_size and z + 2 <= self.mapa.z_size) and alas
        return x + largo <= self.mapa.x_size and y + ancho <= self.mapa.y_size and z + alto <= self.mapa.z_size
    
    def verificar_colision(self, x, y, z, largo, ancho, alto, es_avion=False):
        if not self.verificar_limites(x, y, z, largo, ancho, alto, es_avion):
            print("Las coordenadas exceden los límites del mapa.")
            return True
        if es_avion:
            return np.any(self.mapa.voxelarray[x:x+4, y:y+1, z:z+1]) or \
                   np.any(self.mapa.voxelarray[x+2:x+3, y-1:y+2, z:z+1]) or \
                   np.any(self.mapa.voxelarray[x:x+1, y:y+1, z:z+2])
        else:
            return np.any(self.mapa.voxelarray[x:x+largo, y:y+ancho, z:z+alto])
    
    def obtener_coordenadas(self, nombre, vehiculo):
        try:
            if vehiculo.name == "ELEVATOR":
                x, y = map(int, input(f"Ingrese la posición para {nombre}: ").split())
                
                return x, y, 0
            else:
                x, y, z =  map(int, input(f"Ingrese la posición para {nombre}: ").split())

                return x, y, z
        except ValueError:
            print("Error: Ingrese números enteros para las coordenadas.")
            return None, None, None

    def colocar_vehiculo(self, nombre, vehiculo):
        while True:
            try:
                # x, y, z = self.obtener_coordenadas(nombre, vehiculo)
                x, y, z = ran.randint(0,14), ran.randint(0,14), ran.randint(0,9)
            except ValueError:
                print("Ingrese correctamente las coordenadas formato: (x y z)")
                continue

            if x is None or y is None or z is None:
                continue

            es_avion = (vehiculo.name == "PLANE")

            if self.verificar_limites(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                if not self.verificar_colision(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                    if es_avion:
                        self.mapa.colors[x:x+4, y:y+1, z:z+1] = vehiculo.color
                        self.mapa.colors[x+2:x+3, y-1:y+2, z:z+1] = vehiculo.color
                        self.mapa.colors[x:x+1, y:y+1, z:z+2] = vehiculo.color
                        self.mapa.array_board[x:x+4,y:y + 1,z:z +1] = f"{nombre}"
                        self.mapa.array_board[x + 2:x + 3, y - 1:y + 2, z:z +1] = f"{nombre}"
                        self.mapa.array_board[x:x+1,y:y + 1,z:z +2] = f"{nombre}"
                        self.mapa.voxelarray[x:x+4,y:y + 1,z:z +1] = True
                        self.mapa.voxelarray[x + 2:x + 3, y - 1:y + 2, z:z +1] = True
                        self.mapa.voxelarray[x:x+1,y:y + 1,z:z +2] = True
                    else:
                        self.mapa.voxelarray[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = True
                        self.mapa.colors[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = vehiculo.color
                        self.mapa.array_board[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = f"{nombre}"
                    break

                else:
                        print("¡Colisión detectada! Por favor, ingrese nuevas coordenadas.")
            else:
                    print("Las coordenadas exceden los límites del mapa. Por favor, ingrese nuevas coordenadas.")

    def get_starting_board(self):
        """
        Gives the board with the airships placed on it. The board is a 3D iterable of 
        strings. 

        Each cell has 12 possible values: 'EMPTY', 'BALLOON_0', 'BALLOON_1',
        'BALLOON_2', 'BALLOON_3' 'BALLOON_4', 'ZEPPELIN_0', 'ZEPPELIN_1', 'PLANE_0',
        'PLANE_1', 'PLANE_2', 'ELEVATOR'.

        Returns:
            tuple: A tuple of tuples of tuples of strings representing the board.
            Each cell can be accessed by board[x][y][z].
        """

        for nombre, vehiculo in self.vehiculos.items():
            es_avion = (vehiculo.name=="PLANE")
            
            while True:
                x, y, z = ran.randint(0,14), ran.randint(0,14), ran.randint(0,9)
                if self.verificar_limites(x,y,z,vehiculo.largo,vehiculo.ancho,vehiculo.alto,es_avion):
                    if not self.verificar_colision(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                        if es_avion:
                            self.mapa.array_board[x:x+4,y:y + 1,z:z +1] = f"{nombre}"
                            self.mapa.array_board[x + 2:x + 3, y - 1:y + 2, z:z +1] = f"{nombre}"
                            self.mapa.array_board[x:x+1,y:y + 1,z:z +2] = f"{nombre}"
                            break
                        else:
                            self.mapa.array_board[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = f"{vehiculo}"
                            break
                        
        return self.mapa.array_board

    def next_turn(self, hit_board: tuple) -> tuple:
        """Returns the coordinates to shoot next.

        Args:
            hit_board (tuple): A 3D iterable of strings representing the hit board.
            Each cell can be accessed by hit_board[x][y][z].

            Each cell has 4 possible values:
            - '?': No shot has been done there.
            - 'HIT': An airship has been hit there before.
            - 'MISS': A shot has been done there but did not hit any airship.
            - 'SUNK': An airship was there but has already been shot down entirely.

        Returns:
            tuple: (x,y,z) to shoot at.
        """

        while True:
            x, y, z = ran.randint(0, 14), ran.randint(0, 14), ran.randint(0, 9)

            if hit_board[x][y][z] != '?':
                
                if hit_board[x][y][z] == 'HIT':
                    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
                    for dx, dy, dz in directions:
                        new_x, new_y, new_z = x + dx, y + dy, z + dz
                        if 0 <= new_x <= 14 and 0 <= new_y <= 14 and 0 <= new_z <= 9:
                            return new_x, new_y, new_z
                else: 
                    continue
            else:
                return x, y, z


class Hitboard:
    def __init__(self, opponent_board) -> None:
        self.size = (15,15,10)
        self.board = np.empty(self.size, dtype=object)
        self.board[self.board == None] = '?' 
        self.opponent_board = opponent_board  
        self.plot_board = np.zeros((15,15,10), dtype=bool)
        self.colors = np.empty((15, 15, 10), dtype=object)

    def take_shot(self, x, y, z, vehiculos: dict):
            """
            Realiza un disparo en las coordenadas especificadas (x, y, z) en el tablero del oponente.

            Args:
                x (int): La coordenada x del disparo.
                y (int): La coordenada y del disparo.
                z (int): La coordenada z del disparo.
                vehiculos (dict): Un diccionario que contiene los vehículos del oponente.

            Returns:
                str: El resultado del disparo, que puede ser uno de los siguientes:
                    - 'REPETIDO' si el disparo ya se ha realizado en las coordenadas especificadas.
                    - 'HIT <nombre_vehiculo>' si el disparo impacta en un vehículo pero no lo hunde.
                    - 'SUNK <nombre_vehiculo>' si el disparo hunde un vehículo.
                    - 'MISS' si el disparo no impacta en ningún vehículo.
            """
            shot = self.opponent_board[x][y][z]
            
            if self.board[x][y][z] != '?':
                return 'REPETIDO'

            shot = self.opponent_board[x][y][z]
            
            for nombre, objeto in vehiculos.items():
                if shot == nombre:
                    objeto.recibir_disparo()
                    if not (objeto.is_sunken):
                        self.board[x][y][z] = 'HIT'
                        self.colors[x][y][z] = 'green'
                        self.plot_board[x][y][z] = True
                        return f'HIT {nombre}'

                    else:
                        if objeto.name == 'PLANE':
                            self.board[x:x+4,y:y + 1,z:z +1] = 'SUNK'
                            self.board[x + 2:x + 3, y - 1:y + 2, z:z +1] = 'SUNK'
                            self.board[x:x+1,y:y + 1,z:z +2] = 'SUNK'
                            
                            self.plot_board[x:x+4,y:y + 1,z:z +1] = True
                            self.plot_board[x + 2:x + 3, y - 1:y + 2, z:z +1] = True
                            self.plot_board[x:x+1,y:y + 1,z:z +2] = True

                            self.colors[x:x+4,y:y + 1,z:z +1] = 'black'
                            self.colors[x + 2:x + 3, y - 1:y + 2, z:z +1] = 'black'
                            self.colors[x:x+1,y:y + 1,z:z +2] = 'black'
                            
                        else:
                            self.board[x:x+objeto.largo, y:y+objeto.ancho, z:z+objeto.alto] = 'SUNK'
                            self.colors[x:x+objeto.largo, y:y+objeto.ancho, z:z+objeto.alto] = 'black'
                            self.plot_board[x:x+objeto.largo, y:y+objeto.ancho, z:z+objeto.alto] = True

                        return f'SUNK {nombre}'
    
                elif shot == 'EMPTY':
                    self.board[x][y][z] = 'MISS'
                    self.plot_board[x][y][z] = True
                    self.colors[x][y][z] = 'red'
                    return 'MISS'                
                 
            return 'xd'
        

class Vehiculo:
    def __init__(self, name, largo, ancho, alto, vida, cant, color):
        self.name = name
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.vida = vida
        self.cant = cant
        self.color = color  
        self.is_sunken = False

    def get_name(self):
        return self.name

    def get_self_coords(self):
        return self.coords
    
    def get_size(self):
        return self.largo, self.ancho, self.alto
    
    def get_color(self):
        return self.color
        
    def recibir_disparo(self):
        self.vida -= 1
        if self.vida == 0:
            self.sink()

    def sink(self):
        self.is_sunken = True
    
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
        self.colors = np.empty((self.x_size, self.y_size, self.z_size), dtype=object) 
        self.array_board = np.empty((self.x_size, self.y_size, self.z_size), dtype=object)
        self.array_board[self.array_board == None] = 'EMPTY'
    

        
class Dibujar:
    def __init__(self,mapa,hitboard):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1,2,subplot_kw={"projection": "3d"})
        self.mapa = mapa
        self.hitboard= hitboard


    def dibujar(self):
        """
        Dibuja el objeto en un gráfico 3D.

        Limpia los ejes en lugar de toda la figura.
        Utiliza el método voxels para dibujar los voxels del objeto.
        Establece las etiquetas de los ejes X, Y y Z.
        Actualiza el gráfico y pausa por 0.01 segundos.

        Args:
            None

        Returns:
            None
        """
        
        self.ax1.clear()  # Limpiar los ejes en lugar de toda la figura
        self.ax1.set_title('Mapa del Jugador')
        self.ax1.voxels(self.mapa.voxelarray, edgecolor='gray', facecolors=self.mapa.colors, alpha=0.4)
        self.ax1.set_xlabel("X")
        self.ax1.set_ylabel("Y")
        self.ax1.set_zlabel("Z")
                
        self.ax2.clear()  # Limpiar los ejes en lugar de toda la figura
        self.ax2.set_title('Hitboard del jugador')
        self.ax2.voxels(self.hitboard.plot_board, edgecolor='gray', facecolors=self.hitboard.colors, alpha=0.4)
        self.ax2.set_xlabel("X")
        self.ax2.set_ylabel("Y")
        self.ax2.set_zlabel("Z")
        
        plt.draw()
        plt.pause(0.1)



                
