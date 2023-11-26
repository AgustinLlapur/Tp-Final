#INTERFAZ

from typing import Any, Tuple
import tkinter as tk
from PIL import Image, ImageTk
import os 
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as tkfont
import objetos as obj


class VentanaJuego:
    """Clase que representa la ventana del juego con mapas 3D."""
    def __init__(self, root: tk.Tk) -> None:
        """
        Inicializa la ventana del juego.

        Args:
            root (tk.Tk): La ventana principal de Tkinter.
        """
        self.root = root
        self.root.title("Mapas 3D")
        
        self.fig = plt.figure(figsize=(10, 5))

        # Crear subgráficos para los dos mapas
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122, projection='3d')

        # self.ax.voxels(self.voxelarray, edgecolor='k', facecolors=self.colors, alpha=0.8)
        # self.ax.set_xlabel("X")
        # self.ax.set_ylabel("Y")
        # self.ax.set_zlabel("Z")

        self.ax1.set_title('User board')
        self.ax2.set_title('User hit board')

        self.draw_empty_grid(self.ax1)
        self.draw_empty_grid(self.ax2)

        self.canvas = self.create_canvas()
        
        self.ax1.voxelarray, self.ax1.colors = obj.Mapa().voxelarray, obj.Mapa().colors
        self.ax2.voxelarray, self.ax2.colors = obj.Hitboard().voxelarray, obj.Hitboard().colors

    def actualizar_mapa(self, nuevo_voxelarray1, nuevo_colors1, nuevo_voxelarray2, nuevo_colors2):
        """
        Actualiza la representación gráfica de los mapas en la interfaz.

        Args:
            nuevo_voxelarray1 (np.ndarray): Nuevo estado del voxelarray del primer mapa.
            nuevo_colors1 (np.ndarray): Nuevos colores del primer mapa.
            nuevo_voxelarray2 (np.ndarray): Nuevo estado del voxelarray del segundo mapa.
            nuevo_colors2 (np.ndarray): Nuevos colores del segundo mapa.
        """
        self.ax1.clear()
        self.ax2.clear()

        self.ax1.voxelarray = nuevo_voxelarray1
        self.ax1.colors = nuevo_colors1

        self.ax2.voxelarray = nuevo_voxelarray2
        self.ax2.colors = nuevo_colors2

        self.ax1.voxels(nuevo_voxelarray1, edgecolor='k', facecolors=nuevo_colors1, alpha=0.8)
        self.ax2.voxels(nuevo_voxelarray2, edgecolor='k', facecolors=nuevo_colors2, alpha=0.8)

        self.canvas.draw()
        
    def create_canvas(self) -> Any: # La función puede devolver cualquier tipo de objeto.
        """
        Crea el canvas para mostrar los mapas 3D.

        Returns:
            Any: El canvas para los gráficos 3D.
        """
        # Crear canvas y pack
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Agregar botón para volver al menú
        btn_volver = tk.Button(self.root, text="Volver al Menú", command=self.volver_al_menu)
        btn_volver.pack(side=tk.BOTTOM, pady=10)
        return canvas

    def draw_empty_grid(self, ax: Axes3D) -> None:
        """
        Dibuja la cuadrícula vacía en los mapas 3D.

        Args:
            ax (Axes3D): Subgráfico tridimensional de Matplotlib.
        """
        # Definir los límites de los ejes
        ax.set_xlim(0, 15)
        ax.set_ylim(0, 15)
        ax.set_zlim(0, 10)

        # Crear una cuadrícula vacía utilizando plot_surface con rstride y cstride en 1
        X = np.arange(0, 16)
        Y = np.arange(0, 16)
        X, Y = np.meshgrid(X, Y)
        Z = np.zeros_like(X)

        ax.plot_surface(X, Y, Z, color='none', edgecolor='none', alpha=0)

        # Establecer etiquetas de los ejes
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

    def volver_al_menu(self) -> None:
        """
        Cierra la ventana actual y vuelve al menú principal.
        """
        # Cerrar la ventana actual y volver al menú
        self.root.destroy()
        
class InicioBatallaNaval:
    """Clase que representa la pantalla de inicio del juego Batalla Aeronaval."""
    def __init__(self, root: tk.Tk) -> None:
        """
        Inicializa la pantalla de inicio.

        Args:
            root (tk.Tk): La ventana principal de Tkinter.
        """
        self.root = root
        self.root.title("Batalla Aeronaval")
        self.root.attributes('-fullscreen', True)
        self.fuente_personalizada1: Tuple[str, int, str] = ("Times New Roman", 22, "bold")

        # Carga la fuente personalizada
        self.fuente_personalizada = tkfont.Font(family="Square Pixel7", size=130, weight="bold")

        # Obtén la ruta completa del script y construye la ruta completa de la imagen
        script_dir = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(script_dir, "fondo_inicio.jpg")

        # Cargar la imagen de fondo y almacenarla como un atributo de la instancia
        imagen_original = Image.open(imagen_path)
        imagen_redimensionada = imagen_original.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.imagen_fondo = ImageTk.PhotoImage(imagen_redimensionada)

        self.crear_interfaz_inicio()

    def crear_interfaz_inicio(self) -> None:
        """
        Crea la interfaz de inicio con la imagen de fondo y botones.
        """
        # Configurar el fondo
        lbl_fondo = tk.Label(self.root, image=self.imagen_fondo)
        lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Crear un canvas sobre la imagen de fondo
        canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        canvas.pack()

        # Mostrar la imagen de fondo
        canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen_fondo)

        # Mostrar el texto "Batalla Aeronaval" en el centro de la pantalla
        texto = "Batalla Aeronaval"
        canvas.create_text(
            self.root.winfo_screenwidth() / 2,  # Posición x del texto
            self.root.winfo_screenheight() / 4,  # Posición y del texto
            text=texto,
            font=self.fuente_personalizada,
            fill="white" # Color del texto
        )

        # Agregar un borde alrededor del texto
        canvas.create_text(
            self.root.winfo_screenwidth() / 2 + 2,  # Desplazar el texto en x para simular el borde
            self.root.winfo_screenheight() / 4 + 2,  # Desplazar el texto en y para simular el borde
            text=texto,
            font=self.fuente_personalizada,
            fill="black",  # Color del borde
        )

        # Botón para empezar a jugar
        btn_empezar = tk.Button(self.root, text="Empezar a Jugar", font=self.fuente_personalizada1, command=self.iniciar_juego)
        btn_empezar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Botón para salir
        btn_salir = tk.Button(self.root, text="Salir", font=self.fuente_personalizada1, command=self.root.destroy)
        btn_salir.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        
    def iniciar_juego(self) -> None:
        """
        Inicializa la ventana de juego cuando se hace clic en 'Empezar a Jugar'.
        """
        # Crear una nueva ventana para el juego
        ventana_juego = tk.Toplevel(self.root)

        # Crear la ventana del juego
        juego = VentanaJuego(ventana_juego)

if __name__ == "__main__":
    root = tk.Tk()
    inicio_juego = InicioBatallaNaval(root)
    root.mainloop()

#OBJETOS

import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D


class Hitboard:

    def __init__(self, opponent_board) -> None:
        self.size = (15,15,10)
        self.board = np.empty(self.size, dtype=object)
        self.board[self.board == None] = '?' 
        self.opponent_board = opponent_board  
        self.voxelarray = np.zeros((self.x_size, self.y_size, self.z_size), dtype=bool)
        self.colors = np.empty((self.x_size, self.y_size, self.z_size), dtype=object)

    def take_shot(self, x, y, z, vehiculos):
        vecs = ['BALLOON_0', 'BALLOON_1',
        'BALLOON_2', 'BALLOON_3' 'BALLOON_4', 'ZEPPELIN_0', 'ZEPPELIN_1', 'PLANE_0',
        'PLANE_1', 'PLANE_2', 'ELEVATOR']

        shot = self.opponent_board[x][y][z]
        
        for v in vehiculos:
            if shot == v.get_name():
                v.recibir_disparo()
                if v.is_sunken:
                    self.board[x][y][z] = 'SUNK'
                    return True
                else:
                    self.board[x][y][z] = 'HIT'
                    return True
        if shot == 'EMPTY':
            self.board[x][y][z] = 'MISS'
            return False

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

    def starting_board_user(self):
        vehiculos = [Avion(), Elevador(), Globo(), Zepellin()]

        board = np.empty((self.x_size, self.y_size, self.z_size), dtype=object)

        

    def plot_vehiculos_usuario(self, vehiculo):

        board_usuario = np.empty((15,15,10), dtype=object)

        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
        for i in range(vehiculo.cant):
            while True:
                try:
                    x, y, z, numero = self.obtener_coordenadas_usuario(vehiculo.name, i)
                except ValueError:
                    print("Ingrese correctamente las coordenadas formato: (x y z)")
                    continue

                if x is None or y is None or z is None:
                    continue

                es_avion = (vehiculo.name == "PLANE")

                if self.verificar_limites(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                    if not self.verificar_colision(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):

                        

                        if es_avion:
                            self.colors[x:x+4, y:y+1, z:z+1] = vehiculo.color
                            self.colors[x+2:x+3, y-1:y+2, z:z+1] = vehiculo.color
                            self.colors[x:x+1, y:y+1, z:z+2] = vehiculo.color
                            board_usuario[x:x+4,y:y + 1,z:z +1] = f"{vehiculo.name}_{i}"
                            board_usuario[x + 2:x + 3, y - 1:y + 2, z:z +1] = f"{vehiculo.name}_{i}"
                            board_usuario[x:x+1,y:y + 1,z:z +2] = f"{vehiculo.name}_{i}"
                            vehiculo.posicionar_avion(x, y, z, self.voxelarray)

                        else:
                            vehiculo.posicionar(x, y, z, self.voxelarray)
                            self.colors[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = vehiculo.color
                            board_usuario[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = f"{vehiculo.name}_{i}"
                        self.dibujar()
                        break

                    else:
                        print("¡Colisión detectada! Por favor, ingrese nuevas coordenadas.")
                else:
                    print("Las coordenadas exceden los límites del mapa. Por favor, ingrese nuevas coordenadas.")
        board_usuario[board_usuario == None] = "EMPTY"

        return board_usuario  # Devolver el tablero de salida


#ESTRUCTURA

import numpy as np
import matplotlib.pyplot as plt
import random as ran
from mpl_toolkits.mplot3d import Axes3D
import vehiculos as v
import objetos as obj
import bot as bot
import interfaz as tk

def main():
   
    
    #arrancar el posicionamiento

    vehiculos = [obj.Globo(), obj.Avion(), obj.Zepellin(), obj.Elevador()]

    print("se prepara el juego")

    #usuario recibe su tablero

    user_board = obj.Mapa()

    #usuario posiciona sus vehiculos

    for v in vehiculos:
        board_usuario = user_board.plot_vehiculos_usuario(v) 

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

    print("inicia el juego")

    #uso un while loop??????????


    while True:
        
        print("turno del usuario")
        #se intercambian disparos
        # usuario dispara
        disparo_usuario = input("ingrese coordenadas de disparo: ").split()
        dx, dy, dz = map(int, disparo_usuario)
        hitboard_usuario.take_shot(dx, dy, dz, vehiculos)
        # maquina dispara
        disparo_maquina = bot.next_turn(hitboard_maquina.board)
        mx, my, mz = map(int, disparo_maquina)
        hitboard_maquina.take_shot(mx, my, mz, vehiculos)
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