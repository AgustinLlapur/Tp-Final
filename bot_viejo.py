import numpy as np
import random as ran
import objetos_viejo as o
import matplotlib.pyplot as plt

class Bot:
    def __init__(self) -> None:
        pass

    def next_turn(hit_board: tuple) -> tuple:
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
        vehiculos = [o.Avion(), o.Elevador(), o.Globo(), o.Zepellin()]

        limites = (15,15,10)
        board = np.empty(limites, dtype=object)

        for v in vehiculos:
            es_avion = (v.name=="PLANE")
            for i in range(v.cant):
                while True:
                    x, y, z = ran.randint(0,14), ran.randint(0,14), ran.randint(0,9)
                    if o.Player().verificar_limites(x,y,z,v.largo,v.ancho,v.alto,es_avion):
                        if not o.Mapa().verificar_colision(x, y, z, v.largo, v.ancho, v.alto, es_avion):
                            if es_avion:
                                board[x:x+4,y:y + 1,z:z +1] = f"{v.name}_{i}"
                                board[x + 2:x + 3, y - 1:y + 2, z:z +1] = f"{v.name}_{i}"
                                board[x:x+1,y:y + 1,z:z +2] = f"{v.name}_{i}"
                                break
                            else:
                                board[x:x+v.largo, y:y+v.ancho, z:z+v.alto] = f"{v.name}_{i}"
                                break
                        
        board[board == None] = "EMPTY"

        return board