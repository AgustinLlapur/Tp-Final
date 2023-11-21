class Vehiculo:
    def __init__(self, nombre, largo, ancho, alto, vida, cant, color):
        self.nombre = nombre
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.vida = vida
        self.cant = cant
        self.color = color  # Añadimos el atributo de color

    def rotar(self):
        self.ancho, self.largo = self.largo, self.ancho
        return self.ancho, self.largo

    def recibir_disparo(self):
        self.vida -= 1
        return self
    
    def crear_vehiculo(self, nombre_p):
        try:
            cantidad = self.cant  
            for i in range(1, cantidad + 1):
                while True:
                    try:
                        posicion = tuple(map(int, input(f'Ingrese la posición del {nombre_p}: ').split())) 
                        break
                    except ValueError:
                        print("Error: Ingrese números válidos para la posición.")

                return posicion
        except AttributeError:
            raise NotImplementedError("Cantidad no definida para este tipo de vehículo")


class Globo(Vehiculo):
    def __init__(self, nombre):
        super().__init__("Globo", 3, 3, 3, 1, 5, "blue")
        

class Zepellin(Vehiculo):
    def __init__(self, nombre):
        super().__init__("Zepellin", 5, 2, 2, 3, 2, "green")
        

class Avion(Vehiculo):
    def __init__(self, nombre):
        super().__init__("Avion", 4, 3, 2, 2, 3, "red")
        

class Elevador(Vehiculo):
    def __init__(self, nombre):
        super().__init__("Elevador", 1, 1, 10, 4, 1, "purple")
        

    

