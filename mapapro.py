import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import objetos as m

def main():

    mapa = m.Mapa()

    globo = m.Globo()
    avion = m.Avion()
    zepellin = m.Zepellin()
    elevador = m.Elevador()

    vehiculos = [globo, avion, zepellin, elevador]

    for vehiculo in vehiculos:
        mapa.plot_vehiculos_usuario(vehiculo)

    plt.show()

if __name__ == "__main__":
    main()