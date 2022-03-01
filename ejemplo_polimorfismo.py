
class PelotaDePlastico():
    def __init__(self):
        self.rebotes = []
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            #self.rebotes.append(altura)
            #self.rebotes.append(0)
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 2

pdj = PelotaDeJuguete()
pdj.rebotar(5)

print(pdj.rebotes)

super(type(pdj), pdj).rebotar(5)
print(pdj.rebotes)

