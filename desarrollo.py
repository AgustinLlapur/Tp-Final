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



import numpy as np
import random as ran
import objetos as o

def get_starting_board():
    """
    Generates the initial board with airships placed on it.

    Returns:
        np.ndarray: A 3D NumPy array representing the board.
    """
    # Definir las dimensiones del tablero
    x_size, y_size, z_size = 15, 15, 10

    # Crear un tablero vacío
    board = np.full((x_size, y_size, z_size), 'EMPTY', dtype=object)

    # Crear instancias de vehículos
    vehicles = [o.Avion(), o.Elevador(), o.Globo(), o.Zepellin()]

    for vehicle in vehicles:
        is_plane = (vehicle.nombre == "PLANE")
        for i in range(vehicle.cant):
            while True:
                x, y, z = ran.randint(0, x_size - 1), ran.randint(0, y_size - 1), ran.randint(0, z_size - 1)
                if o.Mapa().verificar_limites(x, y, z, vehicle.largo, vehicle.ancho, vehicle.alto, is_plane):
                    if not o.Mapa().verificar_colision(x, y, z, vehicle.largo, vehicle.ancho, vehicle.alto, is_plane):
                        if is_plane:
                            board[x:x + 4, y:y + 1, z:z + 1] = f"{vehicle.nombre}_{i}"
                            board[x + 2:x + 3, y - 1:y + 2, z:z + 1] = f"{vehicle.nombre}_{i}"
                            board[x:x + 1, y:y + 1, z:z + 2] = f"{vehicle.nombre}_{i}" f"{vehicle.nombre}_{i}"
                            break
                        else:
                            board[x:x + vehicle.largo, y:y + vehicle.ancho, z:z + vehicle.alto] = f"{vehicle.nombre}_{i}"
                            break

    return board

# Ejemplo de uso
starting_board = get_starting_board()
print(starting_board)

def next_turn(hit_board: tuple) -> tuple:
    """
    Returns the coordinates to shoot next based on the hit_board.

    Args:
        hit_board (tuple): A 3D iterable of strings representing the hit board.
        Each cell can be accessed by hit_board[x][y][z].

        Each cell has 4 possible values:
        - '?': No shot has been done there.
        - 'HIT': An airship has been hit there before.
        - 'MISS': A shot has been done there but did not hit any airship.
        - 'SUNK': An airship was there but has already been shot down entirely.

    Returns:
        tuple: (x, y, z) to shoot at.
    """
    # Iterate through the hit_board to find the next valid shot position
    for x in range(len(hit_board)):
        for y in range(len(hit_board[x])):
            for z in range(len(hit_board[x][y])):
                if hit_board[x][y][z] == '?':
                    return x, y, z  # Return the first '?' position found
    # If no '?' position found, return a default position or handle accordingly
    return -1, -1, -1  # Or handle the case where there are no more positions to shoot


def check_valid_placement(board, x, y, z, airship_type): # Verificar si la colocación de un vehículo en las coordenadas dadas (x, y, z) es válida.
    # Verificar si las coordenadas están dentro de los límites del tablero
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or z < 0 or z >= len(board[0][0]):
        return False  # Está fuera de los límites del tablero

    # Verificar si la ubicación está ocupada por otro vehículo
    if board[x][y][z] != 'EMPTY':
        return False  # Hay un vehículo en esta ubicación

    return True  # La colocación es válida

def place_airship(board, x, y, z, airship_type): # Colocar un vehículo del tipo dado en las coordenadas especificadas del tablero.
    if check_valid_placement(board, x, y, z, airship_type):
        # Si la colocación es válida, actualiza el tablero con el nuevo vehículo
        board[x][y][z] = airship_type

def check_ship_sunk(hit_board, ship_type): # Verifica si un tipo específico de nave ha sido completamente hundido en el tablero de impactos.
    # Lógica para verificar si un tipo específico de nave ha sido hundida
    # Esto se basa en la cantidad de 'HIT' en el hit_board correspondiente al tipo de nave

    ship_size = 3  # Supongamos que 'PLANE_0' es un barco de tamaño 3
    hit_count = sum(hit == 'HIT' for row in hit_board for col in row for hit in col if hit == ship_type)

    if hit_count >= ship_size:
        return True  # La nave ha sido completamente hundida
    else:
        return False  # La nave no ha sido completamente hundida


def shoot_at_coordinates(board, hit_board, x, y, z): # Dispara a las coordenadas especificadas en el tablero, actualizando el tablero de impactos y verificando si un vehículo ha sido hundido.
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or z < 0 or z >= len(board[0][0]):
        return  # Está fuera de los límites del tablero, no se hace ningún cambio

    if hit_board[x][y][z] == 'HIT' or hit_board[x][y][z] == 'SUNK':
        return  # Ya se ha disparado allí, no se hace ningún cambio adicional

    if board[x][y][z] != 'EMPTY':
        # Es un impacto
        hit_board[x][y][z] = 'HIT'
        # Verificar si el vehículo ha sido hundido
        if check_ship_sunk(hit_board, board[x][y][z]):
            # Si el barco ha sido hundido, marcarlo como 'SUNK' en el tablero de impactos
            for i in range(len(hit_board)):
                for j in range(len(hit_board[0])):
                    for k in range(len(hit_board[0][0])):
                        if board[i][j][k] == board[x][y][z]:
                            hit_board[i][j][k] = 'SUNK'
    else:
        # No hay ningún vehículo, es un fallo
        hit_board[x][y][z] = 'MISS'

def check_shot_result(hit_board, x, y, z): # Verifica el resultado de un disparo en las coordenadas especificadas en el tablero de impactos.
    if hit_board[x][y][z] == 'HIT':
        return 'HIT'
    elif hit_board[x][y][z] == 'MISS':
        return 'MISS'
    elif hit_board[x][y][z] == 'SUNK':
        return 'SUNK'
    else:
        return 'UNKNOWN'  # O podrías manejar otra condición en caso de un valor desconocido

def display_board(board): # Mostrar en pantalla el tablero del juego (board).
    """
    Displays the game board.

    Args:
        board (tuple): The game board.
    """
    for level, level_content in enumerate(board):
        print(f"Level {level + 1}:")
        for row in level_content:
            print(" ".join(row))
        print("\n")  # Separador entre niveles

def display_hit_board(hit_board): # Muestra en pantalla el tablero de impactos (hit_board) que registra los resultados de los disparos realizados. 
    """
    Displays the hit board showing shot results.

    Args:
        hit_board (tuple): The hit board.
    """
    for level, level_content in enumerate(hit_board):
        print(f"Hit Board - Level {level + 1}:")
        for row in level_content:
            print(" ".join(row))
        print("\n")  # Separador entre niveles

def check_game_over(hit_board, airship_types): # Verifica si todos los barcos han sido completamente hundidos en el juego.
    """
    Checks if all airships have been sunk.

    Args:
        hit_board (tuple): The hit board.
        airship_types (list): List of airship types.

    Returns:
        bool: True if all airships are sunk, False otherwise.
    """
    return all(check_ship_sunk(hit_board, ship_type) for ship_type in airship_types)

# Esta versión utiliza la función all junto con una comprensión de lista para verificar si check_ship_sunk devuelve True para todos los tipos de barcos en la lista. 
# Si todos los barcos están hundidos, la función devuelve True; de lo contrario, devuelve False.

def check_game_over(hit_board, airship_types): # Verifica si todos los barcos han sido completamente hundidos en el juego.
    """
    Checks if all airships have been sunk.

    Args:
        hit_board (tuple): The hit board.
        airship_types (list): List of airship types.

    Returns:
        bool: True if all airships are sunk, False otherwise.
    """
    for airship_type in airship_types:
        if not check_ship_sunk(hit_board, airship_type):
            return False  # Al menos un barco no ha sido completamente hundido
    return True  # Todos los barcos han sido hundidos

# Funciones de interacción con el usuario
def get_user_coordinates():
    x = int(input("Ingresa la coordenada X: "))
    y = int(input("Ingresa la coordenada Y: "))
    z = int(input("Ingresa la coordenada Z: "))
    return x, y, z

def display_shot_feedback(result):
    if result == 'HIT':
        print("¡Has acertado en un vehículo!")
    elif result == 'MISS':
        print("El disparo fue un fallo.")
    elif result == 'SUNK':
        print("¡Has hundido un vehículo!")

def display_game_statistics(score, shots_taken):
    print(f"Puntuación: {score}")
    print(f"Disparos realizados: {shots_taken}")

def display_menu():
    print("----- Menú -----")
    print("1. Jugar")
    print("2. Ver estadísticas")
    print("3. Salir")

# Funciones de persistencia de datos
import pickle

def save_game(game_data):
    with open('saved_game.pickle', 'wb') as file:
        pickle.dump(game_data, file)

def load_game():
    with open('saved_game.pickle', 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data

def special_rules_for_ships(ship_type):
    special_rules = {
        'ZEPPELIN_0': {
            'required_hits': 2  # Número de disparos requeridos para hundir un 'ZEPPELIN_0'
        },
        # Puedes agregar más reglas especiales para otros tipos de vehículos aquí
    }

    if ship_type in special_rules:
        return special_rules[ship_type]['required_hits']
    else:
        return 1  # Si no hay regla especial, se necesita un solo disparo para hundir el vehículo

def computer_AI(board, hit_board):
    # Recorre el tablero de impactos para identificar áreas donde se ha acertado
    target_list = []
    for x in range(len(hit_board)):
        for y in range(len(hit_board[0])):
            for z in range(len(hit_board[0][0])):
                if hit_board[x][y][z] == 'HIT':
                    # Agrega las coordenadas vecinas para intentar encontrar la ubicación del vehículo
                    neighbors = [
                        (x + 1, y, z),
                        (x - 1, y, z),
                        (x, y + 1, z),
                        (x, y - 1, z),
                        (x, y, z + 1),
                        (x, y, z - 1)
                    ]
                    # Filtra las coordenadas válidas dentro de los límites del tablero
                    valid_targets = [(i, j, k) for i, j, k in neighbors if 0 <= i < len(hit_board)
                                     and 0 <= j < len(hit_board[0]) and 0 <= k < len(hit_board[0][0])]
                    # Agrega estas coordenadas a la lista de posibles objetivos
                    target_list.extend(valid_targets)

    # Elimina duplicados y mezcla para hacer el disparo más aleatorio
    import random
    target_list = list(set(target_list))
    random.shuffle(target_list)

    # Ejemplo: Selecciona la primera coordenada de la lista como objetivo (puedes mejorar esta lógica)
    if target_list:
        return target_list[0]
    else:
        # Si no se encontraron HITs, dispara aleatoriamente en el tablero
        return (random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1), random.randint(0, len(board[0][0]) - 1))

import pygame

def advanced_graphics(): # Implementar mejoras visuales utilizando Pygame u otra biblioteca gráfica
    pygame.init()

    # Configuración de la ventana y otros ajustes
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Batalla Naval - Gráficos Avanzados')

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Lógica de dibujo y gráficos avanzados aquí
        screen.fill((255, 255, 255))  # Ejemplo: fondo blanco

        pygame.display.flip()

    pygame.quit()

import pygame

def graphical_user_interface(): # Crear una interfaz de usuario más interactiva y amigable con Pygame
    pygame.init()

    # Configuración de la ventana y otros ajustes
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Batalla Naval - Interfaz de Usuario')

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Lógica de la interfaz de usuario y eventos aquí
        screen.fill((255, 255, 255))  # Ejemplo: fondo blanco

        pygame.display.flip()

    pygame.quit()

import pygame

def animations(): # Agregar animaciones para mostrar disparos, hundimientos, etc. con Pygame
    pygame.init()

    # Configuración de la ventana y otros ajustes
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Batalla Naval - Animaciones')

    # Ejemplo: Imágenes para la animación
    explosion_image = pygame.image.load('explosion.png')
    # ... (cargar otras imágenes necesarias)

    # Ejemplo: Coordenadas de la animación
    explosion_x = 100
    explosion_y = 100

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Lógica de animación aquí
        screen.fill((255, 255, 255))  # Ejemplo: fondo blanco
        screen.blit(explosion_image, (explosion_x, explosion_y))  # Dibuja la explosión en las coordenadas

        pygame.display.flip()

    pygame.quit()

def show_help():
    print("¡Bienvenido al juego de Batalla Naval!")
    print("Objetivo: Hundir todos los barcos enemigos en el tablero.")
    print("\nReglas:")
    print("- Los barcos se colocan en un tablero y los jugadores se turnan para disparar a las coordenadas.")
    print("- Si un disparo alcanza un barco, se marca como 'HIT'. Si no alcanza ningún barco, se marca como 'MISS'.")
    print("- Un barco se considera hundido si todas sus partes han sido alcanzadas.")
    print("\nControles:")
    print("- Durante tu turno, ingresa las coordenadas donde quieras disparar.")
    print("- Las coordenadas se componen de números, por ejemplo, '10', '5', '3'.")
    print("\nEstrategia:")
    print("- Intenta identificar patrones y posiciones probables de los barcos enemigos para optimizar tus disparos.")
    print("- Sigue un enfoque estratégico para hundir los barcos enemigos lo más rápido posible.")
