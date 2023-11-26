import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D
import vehiculos as v
import objetos as obj
import bot as bot
import tkinter as tk
import interfaz as interfaz


def main():
    #arrancar el posicionamiento

    vehiculos = [obj.Globo(), obj.Avion(), obj.Zepellin(), obj.Elevador()]

    print("Se prepara el juego")
    print("Posicionamiento de vehiculos")
    print("----------------------------")
    #usuario recibe su tablero

    user_board = obj.Mapa()

    #usuario posiciona sus vehiculos

    for v in vehiculos:
        board_usuario = user_board.plot_vehiculos_usuario(v) # ya imprime mensajes de "ingrese coordenadas ... " (las saca de obtener_cordenadas_usuario)

    #la maquina recibe hitboard del usuario
    hitboard_usuario = obj.Hitboard(board_usuario)
    #la maquina posiciona sus vehiculos
    board_maquina = bot.get_starting_board()

    #usuario recibe hitboard de la maquina
    hitboard_maquina = obj.Hitboard(board_maquina)

    # Obtener la instancia de la ventana de juego
    root = tk.Tk()
    inicio_juego = tk.InicioBatallaNaval(root)
    ventana_juego = inicio_juego.ventana_juego

    # Actualizar la ventana de juego con los tableros iniciales
    ventana_juego.actualizar_mapa(hitboard_usuario.voxelarray, hitboard_usuario.colors,)


    #ARRANCA EL JUEGO

    print("Inicia el juego")

    #uso un while loop??????????


    while True:
        print("Turno del usuario")
        #se intercambian disparos
        # usuario dispara
        print("Disparo Jugador 1")
        print("-----------------")
        disparo_usuario = input("Coordenadas: ").split()
        dx, dy, dz = map(int, disparo_usuario)
        res_usuario = hitboard_usuario.take_shot(dx, dy, dz, vehiculos)
        print(f"Resultado: {res_usuario}")   # incorporar la funcion take_shot de bot.py
        
        # maquina dispara
        print("Disparo Computadora")
        disparo_maquina = bot.next_turn(hitboard_maquina.board)
        mx, my, mz = map(int, disparo_maquina)
        print(f"Coordenadas: {mx} {my} {mz}")
        hitboard_maquina.take_shot(mx, my, mz, vehiculos)
        res_computadora = hitboard_maquina.take_shot(dx, dy, dz, vehiculos)
        print(f"Resultado: {res_computadora}")
        #se actualiza el tablero
                # Cuando realices cambios en los tableros, actualiza la interfaz
        ventana_juego.actualizar_mapa(hitboard_usuario.voxelarray, hitboard_usuario.colors,)
        #cuando alguien se queda sin vehiculos
        if len(vehiculos) == 0:
            print("el usuario ha perdido")
            break

        
        break
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
    
if __name__ == "__main__":
    main()
