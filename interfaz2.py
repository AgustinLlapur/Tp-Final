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

        self.ax1.set_title('User board')
        self.ax2.set_title('Opponent hit board')

        self.draw_empty_grid(self.ax1)
        self.draw_empty_grid(self.ax2)

        self.canvas = self.create_canvas()

        self.voxelarray = np.zeros((15,15,10), dtype=bool)
        self.colors = np.empty((15,15,10), dtype=object)

    def get_user_board(self) -> Axes3D:
        """
        Devuelve el mapa 3D del usuario.

        Returns:
            Axes3D: El mapa 3D del usuario.
        """
        return self.ax1
    def get_hitboard(self) -> Axes3D:
        """
        Devuelve el mapa 3D del oponente.

        Returns:
            Axes3D: El mapa 3D del oponente.
        """
        return self.ax2

     

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

        self.voxelarray = np.zeros((15, 15, 10), dtype=bool)
        self.colors = np.empty((15, 15, 10), dtype=object) 


        mapa = obj.Mapa()

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

    def dibujar(self):
        self.ax.clear()  # Limpiar los ejes en lugar de toda la figura
        self.ax.voxels(self.voxelarray, edgecolor='k', facecolors=self.colors, alpha=0.8)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        plt.draw()
        plt.pause(0.01)

    def plot_vehiculos_usuario(self, vehiculo):

        board_usuario = np.empty((15,15,10), dtype=object)
        mapa = obj.Mapa()

        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
        for i in range(vehiculo.cant):
            while True:
                try:
                    x, y, z, numero = mapa.obtener_coordenadas_usuario(vehiculo.name, i)
                except ValueError:
                    print("Ingrese correctamente las coordenadas formato: (x y z)")
                    continue

                if x is None or y is None or z is None:
                    continue

                es_avion = (vehiculo.name == "PLANE")

                if mapa.verificar_limites(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):
                    if not mapa.verificar_colision(x, y, z, vehiculo.largo, vehiculo.ancho, vehiculo.alto, es_avion):

                        if es_avion:
                            mapa.colors[x:x+4, y:y+1, z:z+1] = vehiculo.color
                            mapa.colors[x+2:x+3, y-1:y+2, z:z+1] = vehiculo.color
                            mapa.colors[x:x+1, y:y+1, z:z+2] = vehiculo.color
                            board_usuario[x:x+4,y:y + 1,z:z +1] = f"{vehiculo.name}_{i}"
                            board_usuario[x + 2:x + 3, y - 1:y + 2, z:z +1] = f"{vehiculo.name}_{i}"
                            board_usuario[x:x+1,y:y + 1,z:z +2] = f"{vehiculo.name}_{i}"
                            vehiculo.posicionar_avion(x, y, z, mapa.voxelarray)

                        else:
                            vehiculo.posicionar(x, y, z, mapa.voxelarray)
                            mapa.colors[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = vehiculo.color
                            board_usuario[x:x+vehiculo.largo, y:y+vehiculo.ancho, z:z+vehiculo.alto] = f"{vehiculo.name}_{i}"
                        self.dibujar()
                        break

                    else:
                        print("¡Colisión detectada! Por favor, ingrese nuevas coordenadas.")
                else:
                    print("Las coordenadas exceden los límites del mapa. Por favor, ingrese nuevas coordenadas.")
        board_usuario[board_usuario == None] = "EMPTY"

        return board_usuario
        
    def iniciar_juego(self) -> None:
        """
        Inicializa la ventana de juego cuando se hace clic en 'Empezar a Jugar'.
        """
        # Crear una nueva ventana para el juego
        ventana_juego = tk.Toplevel(self.root)

        # Crear la ventana del juego y pasar la ventana principal
        juego = VentanaJuego(ventana_juego)

        # Llamar a la función plot_vehiculos_usuario de la instancia de VentanaJuego
        self.plot_vehiculos_usuario(obj.Avion())
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    inicio_juego = InicioBatallaNaval(root)
    root.mainloop()