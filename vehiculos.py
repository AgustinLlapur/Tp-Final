import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D

class Player:
    def __init__(self, board, hitboard, vehicles) -> None:
        self.board = board
        self.hitboard = hitboard
        self.vehicles = vehicles

    def turn(self):
        pass

class Vehiculo:

    def __init__(self, name, largo, ancho, alto, vida, cant, color):
        self.name = name
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.vida = vida
        self.cant = cant
        self.color = color  # Añadimos el atributo de color
        self.is_sunken = False

    def get_name(self):
        return self.name

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
        return self.is_sunken
    
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

    def posicionar_avion(self, x, y, z, voxelarray):
        voxelarray[x:x+4,y:y + 1,z:z +1] = True
        voxelarray[x + 2:x + 3, y - 1:y + 2, z:z +1] = True
        voxelarray[x:x+1,y:y + 1,z:z +2] = True

class Elevador(Vehiculo):
    def __init__(self):
        super().__init__("ELEVATOR", 1, 1, 10, 4, 1, "purple")

class Hitboard:
    def __init__(self) -> None:
        self.size = (15,15,10)
        self.board = np.empty(self.size, dtype=object)
        self.board[self.board == None] = '?'

    def get_size(self):
        return self.size
    
    def get_board(self):
        return self.board
    
class Startingboard:
    def __init__(self) -> None:
        self.size = (15,15,10)
        self.board = np.empty(self.size, dtype=object)
        self.board[self.board == None] = "EMPTY"

    def get_starting_board(self):
        #funciona para la maquina, pero lo quiero generalizar 
        #cambiando la forma de llamar a las coordenadas
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
        vehiculos = [Avion(), Elevador(), Globo(), Zepellin()]

        for v in vehiculos:
            es_avion = (v.nombre=="PLANE")
            for i in range(v.cant):
                while True:
                    x, y, z = ran.randint(0,15), ran.randint(0,15), ran.randint(0,10)
                    if self.verificar_limites(x,y,z,v.largo,v.ancho,v.alto,es_avion):
                        if not self.verificar_colision(x, y, z, v.largo, v.ancho, v.alto, es_avion):
                            if es_avion:
                                self.board[x:x+4,y:y + 1,z:z +1] = f"{v.nombre}_{i}"
                                self.board[x + 2:x + 3, y - 1:y + 2, z:z +1] = f"{v.nombre}_{i}"
                                self.board[x:x+1,y:y + 1,z:z +2] = f"{v.nombre}_{i}"f"{v.nombre}_{i}"
                                break

                            else:
                                self.board[x:x+v.largo, y:y+v.ancho, z:z+v.alto] = f"{v.nombre}_{i}"
                                break

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



    