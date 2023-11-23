def get_starting_board():
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

    limites = (15, 15, 10)
    board = np.empty(limites, dtype=object)

    for v in vehiculos:
        es_avion = (v.nombre == "PLANE")
        for i in range(v.cant):
            while True:
                x, y, z = ran.randint(0, 15), ran.randint(0, 15), ran.randint(0, 10)
                if o.Mapa().verificar_limites(x, y, z, v.largo, v.ancho, v.alto, es_avion):
                    if not o.Mapa().verificar_colision(x, y, z, v.largo, v.ancho, v.alto, es_avion):
                        if es_avion:
                            board[x:x+4, y:y+1, z:z+1] = f"{v.nombre}_{i}"
                            board[x+2:x+3, y-1:y+2, z:z+1] = f"{v.nombre}_{i}"
                            board[x:x+1, y:y+1, z:z+2] = f"{v.nombre}_{i}" * 2
                            break
                        else:
                            board[x:x+v.largo, y:y+v.ancho, z:z+v.alto] = f"{v.nombre}_{i}"
                            break
    board[board == None] = "EMPTY"
    return board

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
    x, y, z = ran.randint(0, 15), ran.randint(0, 15), ran.randint(0, 10)
    return x, y, z
