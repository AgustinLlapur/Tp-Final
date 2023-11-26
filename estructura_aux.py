import tkinter as tk
import interfaz as interfaz
import objetos as obj
import bot as bot

def main():
    root = tk.Tk()
    ventana_juego = interfaz.InicioBatallaNaval(root)
    user_board = obj.Mapa()
    vehiculos = [obj.Globo(), obj.Avion(), obj.Zepellin(), obj.Elevador()]

    for vehiculo in vehiculos:
        user_board.plot_vehiculos_usuario(vehiculo)

    hitboard_usuario = obj.Hitboard(user_board.board)
    board_maquina = bot.get_starting_board()
    hitboard_maquina = obj.Hitboard(board_maquina)

    def turno_de_juego():
        ventana_juego.actualizar_mapa(hitboard_usuario.voxelarray, vehiculos)  # Actualizar la interfaz
        print("Turno del jugador")
        manejar_entrada_usuario()  # Obtener entrada del usuario usando Tkinter
        bot.next_turn(hitboard_maquina.board)  # Realizar el turno de la IA

        if len(vehiculos) == 0:
            print("El jugador ha perdido")
        else:
            root.after(1000, turno_de_juego)  # Repetir el turno después de 1 segundo

    def manejar_entrada_usuario():
        # Lógica para manejar la entrada del usuario usando widgets de Tkinter
        # Por ejemplo, usar widgets de Entry para la entrada y un botón para confirmar el movimiento
        # Obtener la entrada del usuario y procesarla
        disparo_usuario = input("ingrese coordenadas de disparo: ").split()
        dx, dy, dz = map(int, disparo_usuario)
        hitboard_usuario.take_shot(dx, dy, dz, vehiculos)

    def realizar_turno_maquina():
        disparo_maquina = bot.next_turn(hitboard_maquina.board)
        mx, my, mz = map(int, disparo_maquina)
        hitboard_maquina.take_shot(mx, my, mz, vehiculos)

    manejar_entrada_usuario()  # Obtener el movimiento del usuario inicialmente
    root.after(1000, turno_de_juego)  # Comenzar el turno del juego después de 1 segundo
    root.mainloop()

if __name__ == "__main__":
    main()
