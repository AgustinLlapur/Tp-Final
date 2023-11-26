import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import objetos as obj
import bot as bot


def main():

    #PRIMERA PARTE(EL USUARIO ARMA SU MAPA)
    mapa = obj.Mapa()

    globo = obj.Globo()
    avion = obj.Avion()
    zepellin = obj.Zepellin()
    elevador = obj.Elevador()

    vehiculos = [globo, avion, zepellin, elevador]

    for vehiculo in vehiculos:
        mapa.plot_vehiculos_usuario(vehiculo)

    #plt.show() 

    #MAPA DE LA PC
    mapa_pc = bot.get_starting_board()

    #y ahora?????????????
    while True:
        pass


if __name__ == "__main__":
    main()