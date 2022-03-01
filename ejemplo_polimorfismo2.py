
class PelotaDeDeporte():
    def __init__(self, color: str, forma: str): 
        self.__color = color
        self.__forma = forma
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def forma(self):
        return self.__forma


class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, forma: str, cantidad_hexagonos: int):
        super().__init__(color, forma) # se ejecuta constructor de PelotaDeDeporte
        #PelotaDeDeporte.__init__(self, color, forma) --> otra forma de llamar como el ejemplo 3
        self.__cantidad_hexagonos = cantidad_hexagonos

    @property
    def cantidad_hexagonos(self):
        return self.__cantidad_hexagonos

pdf = PelotaDeFutbol("Blanco y Negro", "Esferica", 15)
print(pdf.color)
print(pdf.forma)
print(pdf.cantidad_hexagonos)