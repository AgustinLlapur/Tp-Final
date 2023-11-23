import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D
import vehiculos as v
import objetos as obj

def main():

    #arrancar el posicionamiento

    vehiculos = [obj.Globo(), obj.Avion(), obj.Zepellin(), obj.Elevador()]

    print("se prepara el juego")

    #usuario recibe su tablero

    user_board = obj.Mapa()

    #usuario posiciona sus vehiculos

    for v in vehiculos:
        user_board.plot_vehiculos_usuario(v)

    #la maquina recibe hitboard del usuario

    #la maquina posiciona sus vehiculos

    #usuario recibe hitboard de la maquina

    #ARRANCA EL JUEGO

    print("inicia el juego")

    #uso un while loop??????????

    while True:
        
        #se intercambian disparos

        #cuando alguien se queda sin vehiculos
        break
    
if __name__ == "__main__":
    main()