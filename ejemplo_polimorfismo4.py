
class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        if isinstance(self, PelotaDeTenis): #Si la instancia es de pelota de tenis hace esto, setea y manda amarillo
            self.__color = "Amarillo"
        else:                               #Si la instancia viene de otro hijo, asigna ese color
            self.__color = color

    @property
    def color(self) -> str:
        return self.__color

class PelotaDeTenis(PelotaDeDeporte):
    pass

class PelotaDePingPong(PelotaDeDeporte):
    pass

p1 = PelotaDeTenis("Rojo")
p2 = PelotaDePingPong("Blanco")
p3 = PelotaDePingPong("Naranja")

print(p1.color, p2.color)

if isinstance(p1 and p3, PelotaDePingPong):
    print('son dos pelotas del mismo tipo')
else:
    print('son dos pelotas de distinto tipo')