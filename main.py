import matplotlib as plt
import objetos as obj

def mensaje():
    print('Posicionamiento de vehículos')
    print('----------------------------')
    print('Jugador 1, ingrese las coordenadas de los vehículos: ')
    


def crear_vehiculo(nombre_p, tipo, cantidad):
    """
    Crea instancias de vehículos y solicita al usuario la posición de cada uno.

    Parameters:
    - nombre_p (str): Prefijo para el nombre del vehículo (por ejemplo, "Globo").
    - tipo (str): Tipo de vehículo (por ejemplo, "globo").
    - cantidad (int): Cantidad de vehículos a crear.

    Returns:
    - List: Lista de instancias de vehículos creados.
    """
    vehiculos = []
    for i in range(1, cantidad + 1):
        while True:
            try:
                posicion = tuple(map(int, input(f'Ingrese la posición del {nombre_p}_{i}: ').split()))
                vehiculo = None
                if tipo == 'globo':
                    vehiculo = obj.globo(f"{nombre_p}_{i}", posicion, 1)
                elif tipo == 'zeppelin':
                    vehiculo = obj.zeppelin(f"{nombre_p}_{i}", posicion, 3)
                elif tipo == 'avion':
                    vehiculo = obj.avion(f"{nombre_p}_{i}", posicion, 2)
                elif tipo == 'elevador':
                    vehiculo = obj.elevador(f"{nombre_p}_{i}", posicion, 4)
                vehiculos.append(vehiculo)
                break
            except ValueError:
                print("Error: Ingrese números válidos para la posición.")

    return vehiculos

def main():
    """
    Función principal que crea instancias de varios tipos de vehículos y almacena las instancias en listas.
    """
    globos = crear_vehiculo("Globo", "globo", 5)
    zeppelins = crear_vehiculo("Zeppelin", "zeppelin",   2)
    aviones = crear_vehiculo("Avion", "avion", 3)
    elevadores = crear_vehiculo("Elevador", "elevador", 1)


if __name__ == "__main__":
    main()
