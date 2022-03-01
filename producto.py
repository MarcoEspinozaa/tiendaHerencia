
class Producto():
    def __init__(self, nombre: str, stock: int = 0):
        self.__nombre = nombre
        self.__precio = int
        self.__stock = stock

    def validar_stock(self, stock):
        if stock < 0:
            stock = 0
        return stock
    
    def validar_precio(self, precio):
        if precio < 0:
            precio = 0
        return precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: int):
        self.__precio = self.validar_precio(nuevo_precio)

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        self.__stock = self.validar_stock(nuevo_stock)

    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self

    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()

    def __add__(self, other):
        return self.stock + other.stock