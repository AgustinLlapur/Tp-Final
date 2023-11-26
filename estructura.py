import tkinter as tk
import interfaz as interfaz
import objetos as obj
import bot as bot

def main(ventana_juego):
    root = tk.Tk()
    inicio_juego = interfaz.InicioBatallaNaval(root)
    root.mainloop()
    
    user_board = obj.Mapa()
    vehiculos = [obj.Globo(), obj.Avion(), obj.Zepellin(), obj.Elevador()]

    for v in vehiculos:
        user_board.plot_vehiculos_usuario(v)

    hitboard_usuario = obj.Hitboard(user_board.board)
    board_maquina = bot.get_starting_board()
    hitboard_maquina = obj.Hitboard(board_maquina)

    while True:
        ventana_juego.actualizar_mapa(hitboard_usuario.voxelarray, vehiculos)  # Actualizar la interfaz
        print("turno del usuario")
        disparo_usuario = input("ingrese coordenadas de disparo: ").split()
        dx, dy, dz = map(int, disparo_usuario)
        hitboard_usuario.take_shot(dx, dy, dz, vehiculos)
        disparo_maquina = bot.next_turn(hitboard_maquina.board)
        mx, my, mz = map(int, disparo_maquina)
        hitboard_maquina.take_shot(mx, my, mz, vehiculos)

        if len(vehiculos) == 0:
            print("el usuario ha perdido")
            break

# if __name__ == "__main__":
    # root = tk.Tk()
    # inicio_juego = interfaz.InicioBatallaNaval(root)
    # root.mainloop()
    
ventanajuego = interfaz.VentanaJuego(tk.Tk())
main(ventanajuego)