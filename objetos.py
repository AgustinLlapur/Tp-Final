class vehiculo:
    def __init__(self, name, forma, vida):
        self.name = name 
        self.forma = forma
        self.vida = vida
  
class globo(vehiculo):
    def __init__(self, name, forma, vida):
        super().__init__(name, forma, vida)
        self.name = name
        self.forma = (3,3,3)
        self.vida = 1

class zeppelin(vehiculo):
    def __init__(self, name, forma, vida):
        super().__init__(name, forma, vida)
        self.name = name
        self.forma = (5,2,2)
        self.vida = 3

class avion:
    def __init__(self, name, forma, vida):
        super().__init__(name, forma, vida)
        pass

class elevador:
    def __init__(self, name, forma, vida):
        super().__init__(name, forma, vida)
        self.name = name
        self.forma = (1,1,10)
        self.vida = 4

class mapa:
    def __init__(self) -> None:
        self.x = 15
        self.y = 15
        self.z = 10
#definir el objeto en el codigo principal



    








            
    

    