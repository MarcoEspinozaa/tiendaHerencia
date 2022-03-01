from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    @abstractmethod
    def validar_opcion(self):
        pass

class Restaurante(Tienda):
    IVA = 0.19
    def __init__(self, nombre: str, costoDelivery: int):
        self.__nombre = nombre
        self.__costoDelivery = costoDelivery
        self.__listaProdcutos = []

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def costoDelivery(self):
        return self.__costoDelivery

    @property
    def listaProductos(self):
        return self.__listaProdcutos

    @listaProductos.setter
    def listaProductos(self, nuevo_producto: object):
        self.__listaProdcutos.append(nuevo_producto)


    def validar_opcion(self, opciones: list, eleccion: int):
        # Definir validación de eleccion
        while True: 
            if eleccion not in opciones:
                eleccion = int(input('Opción no válida, ingrese una de las opciones válidas: '))
            else:
                return eleccion

    def agregar_item(self, item: Producto):
        self.__listaProdcutos.append(item)

    def ingresar_producto(self):
        print('')
        opcion_ingreso = int(input("¿Desea agregar un producto?\n1. Sí\n2. No\n> "))
        self.validar_opcion([1,2] , opcion_ingreso)
        while opcion_ingreso == 1:
            nombre = input("Ingrese nombre del producto: ").lower()
            precio = int(input("Ingrese precio del producto: "))
            producto = Producto(nombre)
            self.agregar_item(producto)
            producto.precio = precio

            print(f"\n***** Datos producto {producto.nombre.capitalize()} *****")
            print(f"PRECIO: ${producto.precio}")
            print(f"\nLa tienda cuenta con {len(self.listaProductos)} productos(s)\n")

            opcion_ingreso = int(input("¿Desea agregar un producto?\n1. Sí\n2. No\n> "))

    def listar_productos(self):
        print("Lista de productos disponibles:\n")
        print("Nombre del prodcuto // Precio")
        for index, item in enumerate(self.listaProductos, 1):
            print(f'{index}. {item.nombre.capitalize()} // ${item.precio}')

    def venta(self, nombre_producto: str, cantidad_requerida: int):
        producto = Producto(nombre_producto)
        if producto in self.listaProductos:
            indice = self.listaProductos.index(producto)
            producto = self.listaProductos[indice]
            valor_total = cantidad_requerida * producto.precio
            iva = valor_total * self.IVA
            valor_final = valor_total + iva
            print(f'Se está realizando una venta.\n')
            print(f'Venta: {producto.nombre.capitalize()} tiene un precio de ${producto.precio} pesos')
            print(f'Bruto: ${producto.precio} x {cantidad_requerida} = ${valor_total}')
            print(f'IVA: ${valor_total} x {self.IVA} = ${iva}')
            print('-------------------------------')
            print(f'TOTAL: ${valor_final}')
        else:
            print('El producto no existe, no se puede realizar la venta')


class Supermercado(Tienda):
    IVA = 0.19
    def __init__(self, nombre: str, costoDelivery: int):
        self.__nombre = nombre
        self.__costoDelivery = costoDelivery
        self.__listaProdcutos = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def costoDelivery(self):
        return self.__costoDelivery

    @property
    def listaProductos(self):
        return self.__listaProdcutos

    @listaProductos.setter
    def listaProductos(self, nuevo_producto: object):
        self.__listaProdcutos.append(nuevo_producto)

    def validar_opcion(self, opciones: list, eleccion: int):
        # Definir validación de eleccion
        while True: 
            if eleccion not in opciones:
                eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
            else:
                return eleccion

    def agregar_item(self, item: Producto):
        self.__listaProdcutos.append(item)

    def ingresar_producto(self):
        opcion_ingreso = int(input("¿Desea agregar un producto?\n1. Sí\n2. No\n> "))
        self.validar_opcion([1,2], opcion_ingreso)
        while opcion_ingreso == 1:
            nombre = input("Ingrese nombre del producto: ").lower()
            stock = int(input("Ingrese stock del producto: "))

            producto = Producto(nombre, stock)
            if producto in self.listaProductos:
                indice = self.listaProductos.index(producto)
                producto.precio = self.listaProductos[indice].precio
                self.listaProductos[indice] += producto
                producto.stock = self.listaProductos[indice].stock
            else:
                self.agregar_item(producto)
                precio = int(input("Ingrese precio del prodcuto: "))
                producto.precio = precio

            print(f"\n***** Datos producto {producto.nombre.capitalize()} *****")
            print(f"PRECIO: ${producto.precio}")
            print(f"STOCK: {producto.stock}")
            print(f"\nLa tienda cuenta con {len(self.listaProductos)} prodcutos(s)\n")

            opcion_ingreso = int(input("¿Desea agregar un producto?\n1. Sí\n2. No\n> "))

    def listar_productos(self):
        print("Lista de productos disponibles:\n")
        print("Nombre del prodcuto // Precio // Stock")
        for index, item in enumerate(self.listaProductos, 1):
            if item.stock < 10:
                print(f'{index}. {item.nombre.capitalize()} // ${item.precio} // Stock: {item.stock} Pocos productos disponibles')
            else:
                print(f'{index}. {item.nombre.capitalize()} // ${item.precio} // Stock: {item.stock}')

    def venta(self, nombre_producto: str, cantidad_requerida: int):
        producto = Producto(nombre_producto)
        if producto in self.listaProductos:
            indice = self.listaProductos.index(producto)
            producto = self.listaProductos[indice]
            if producto.stock < cantidad_requerida and producto.stock > 0: 
                cantidad_requerida = producto.stock
                producto.stock = 0
            producto.stock -= cantidad_requerida
            valor_total = cantidad_requerida * producto.precio
            iva = valor_total * self.IVA
            valor_final = valor_total + iva
            producto.stock -= cantidad_requerida
            print(f'Se está realizando una venta.\n')
            print(f'Venta: {producto.nombre.capitalize()} tiene un precio de ${producto.precio} pesos')
            print(f'Bruto: ${producto.precio} x {cantidad_requerida} = ${valor_total}')
            print(f'IVA: ${valor_total} x {self.IVA} = ${iva}')
            print('-------------------------------')
            print(f'TOTAL: ${valor_final}')
        else: 
            print("No se puede realizar la venta, no se cuenta con stock disponible o el producto no existe")


class Farmacia(Tienda):
    IVA = 0.19
    def __init__(self, nombre: str, costoDelivery: int):
        self.__nombre = nombre
        self.__costoDelivery = costoDelivery
        self.__listaProdcutos = []

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def costoDelivery(self):
        return self.__costoDelivery

    @property
    def listaProductos(self):
        return self.__listaProdcutos

    @listaProductos.setter
    def listaProductos(self, nuevo_producto: object):
        self.__listaProdcutos.append(nuevo_producto)

    def validar_opcion(self, opciones: list, eleccion: int):
        # Definir validación de eleccion
        while True: 
            if eleccion not in opciones:
                eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
            else:
                return eleccion

    def agregar_item(self, item: Producto):
        self.__listaProdcutos.append(item)

    def realizar_venta(self, cantidad_requerida: int, producto: Producto):
        iva = self.IVA
        valor_total = cantidad_requerida * producto.precio
        iva = valor_total * self.IVA
        valor_final = valor_total + iva
        print(f'Se está realizando una venta.\n')
        print(f'Venta: {producto.nombre.capitalize()} tiene un precio de ${producto.precio} pesos')
        print(f'Bruto: ${producto.precio} x {cantidad_requerida} = ${valor_total}')
        print(f'IVA: ${valor_total} x {self.IVA} = ${iva}')
        print('-------------------------------')
        print(f'TOTAL: ${valor_final}')

    def ingresar_producto(self):
        opcion_ingreso = int(input("¿Desea agregar un producto?\n1. Sí\n2. No\n> "))
        self.validar_opcion([1,2], opcion_ingreso)
        while opcion_ingreso == 1:
            nombre = input("Ingrese nombre del producto: ").lower()
            stock = int(input("Ingrese stock del producto: "))

            producto = Producto(nombre, stock)
            if producto in self.listaProductos:
                indice = self.listaProductos.index(producto)
                producto.precio = self.listaProductos[indice].precio
                self.listaProductos[indice] += producto
                producto.stock = self.listaProductos[indice].stock
            else:
                self.agregar_item(producto)
                precio = int(input("Ingrese precio del prodcuto: "))
                producto.precio = precio

            print(f"\n***** Datos producto {producto.nombre.capitalize()} *****")
            print(f"PRECIO: ${producto.precio}")
            print(f"STOCK: {producto.stock}")
            print(f"\nLa tienda cuenta con {len(self.listaProductos)} prodcutos(s)\n")

            opcion_ingreso = int(input("¿Desea agregar un producto?\n1. Sí\n2. No\n> "))

    def listar_productos(self):
        print("Lista de productos disponibles:\n")
        print("Nombre del prodcuto // Precio")
        for index, item in enumerate(self.listaProductos, 1):
            if item.precio > 15000:
                print(f'{index}. {item.nombre.capitalize()} // ${item.precio} Envío gratis al solicitar este producto')
            else:
                print(f'{index}. {item.nombre.capitalize()} // ${item.precio}')

    def venta(self, nombre_producto: str, cantidad_requerida: int):
        producto = Producto(nombre_producto)
        if producto in self.listaProductos:
            indice = self.listaProductos.index(producto)
            producto = self.listaProductos[indice]
            #Si hay stock y la cantidad no supera los 3 items.
            if cantidad_requerida <= producto.stock and cantidad_requerida <= 3:
                producto.stock -= cantidad_requerida
                self.realizar_venta(cantidad_requerida, producto)
            #Si el stock es menor a la cantidad requerida
            elif producto.stock < cantidad_requerida and producto.stock > 0: 
                cantidad_requerida = producto.stock
                producto.stock = 0     
                self.realizar_venta(cantidad_requerida, producto)
            #Sin stock
            elif producto.stock == 0 and cantidad_requerida <= 3:
                print('\033[1m' + "No se puede realizar la venta, no se cuenta con stock disponible" + '\033[0m')
            #La cantidad requerida es mayor a 3
            elif cantidad_requerida > 3:
                print('\033[1m' +  "La cantidad requerida excede los 3 prodcutos permitidos" + '\033[0m')
        else: 
            print('\033[1m' + "No se puede realizar la venta, el producto no existe" + '\033[0m')


    




