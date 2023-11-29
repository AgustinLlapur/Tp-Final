import numpy as np
import objetos_viejo as obj
import bot_viejo as pc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  


dicc_vehicle_usuario = {
    f"{obj.Globo().name}_{i}": obj.Globo() for i in range(5)
}
dicc_vehicle_usuario.update({
    f"{obj.Zepellin().name}_{i}": obj.Zepellin() for i in range(2)
})
dicc_vehicle_usuario.update({
    f"{obj.Avion().name}_{i}": obj.Avion() for i in range(3)
})
dicc_vehicle_usuario.update({
    f"{obj.Elevador().name}_{i}": obj.Elevador()for i in range(1)
})

dicc_vehicle_pc = {
    f"{obj.Globo().name}_{i}": obj.Globo() for i in range(5)
}
dicc_vehicle_pc.update({
    f"{obj.Zepellin().name}_{i}": obj.Zepellin() for i in range(2)
})
dicc_vehicle_pc.update({
    f"{obj.Avion().name}_{i}": obj.Avion() for i in range(3)
})
dicc_vehicle_pc.update({
    f"{obj.Elevador().name}_{i}": obj.Elevador()for i in range(1)
})

lista_vehiculos =[obj.Globo(), obj.Zepellin(), obj.Avion(), obj.Elevador()] # solo para el ploteo 



def main(): 

    #POSICIONAMIENTO

    #instancia de mapa bot
    mapa_bot = obj.Mapa()

    #instancia del bot
    bot = obj.Player(mapa_bot, dicc_vehicle_pc)

    #mapa con vehiculos maquina
    bot_main_board = bot.get_starting_board()

    #hitboard jugador
    player_hitboard = obj.Hitboard(bot_main_board)

    #instancia de mapa para jugador
    mapa_player = obj.Mapa()  

    #hitboard maquina
    bot_hitboard = obj.Hitboard(mapa_player.array_board)

    dibujo_player = obj.Dibujar(mapa_player,player_hitboard)

    #instancia de jugador
    usuario = obj.Player(mapa_player, dicc_vehicle_usuario)


    #mapa con vehiculos del jugador
    for nombre, vehiculo in usuario.vehiculos.items():
        usuario.colocar_vehiculo(nombre, vehiculo)
        dibujo_player.dibujar()      #cada vez que quiero actualizar la parte visual/para que se agreguen cosas nuevas


    while True:
        # Turno del usuario
        print("\nTurno del Usuario:")
        user_shot_coords = usuario.dispara_usuario()
        result = player_hitboard.take_shot(user_shot_coords[0], user_shot_coords[1], user_shot_coords[2], dicc_vehicle_pc)
        print(f"¡Disparo {result}!")
        

        # Verificar si la máquina ha perdido
        if all(v.is_sunken for v in dicc_vehicle_pc.values()):
            print("¡Has ganado! La máquina ha perdido todas sus naves.")
            print(f'hundidos: {[v.is_sunken for v in dicc_vehicle_pc.values()]}')
            plt.show(block=False)
            break

        # Turno de la máquina
        print("\nTurno de la Máquina:")
        machine_shot_coords = bot.next_turn(bot_hitboard.board)  
        result = bot_hitboard.take_shot(machine_shot_coords[0], machine_shot_coords[1], machine_shot_coords[2], dicc_vehicle_usuario)
        print(f"¡Disparo {result}!")
        
        # print(f'hundidos: {[v.is_sunken for v in dicc_vehicle_pc.values()]}')
        
        # Verificar si el usuario ha perdido una vez que todos los vehículos de la máquina han sido hundidos
        if all(v.is_sunken for v in dicc_vehicle_usuario.values()):
            print("¡Has perdido! Todas tus naves han sido hundidas.")
            # print(f'hundidos: {[v.is_sunken for v in dicc_vehicle_pc.values()]}')
            plt.show(block=False)
            break

 
if __name__ == "__main__":
    main()