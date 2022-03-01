from tienda import Farmacia, Restaurante, Supermercado
from input_tienda import main, main2
import sys
import os
import time
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

while True:
    tipo = main()

    #Ingresa al tipo de tienda deseada
    if tipo == '1':
        nombre = 'Supermercado'
        print('')
        costoDelivery = int(input(f"Ingrese el costo del delivery para {nombre}: "))
        #Limpia pantalla
        os.system(op_sys)
        #Instancia la clase e inicia para agregar producto
        tienda = Supermercado(nombre, costoDelivery)
        tienda.ingresar_producto()
    elif tipo == '2':
        nombre = 'Farmacia'
        print('')
        costoDelivery = int(input(f"Ingrese el costo del delivery para {nombre}: "))
        #Limpia pantalla
        os.system(op_sys)
        #Instancia la clase e inicia para agregar producto
        tienda = Farmacia(nombre, costoDelivery)
        tienda.ingresar_producto()
    elif tipo == '3':
        nombre = 'Restaurant'
        print('')
        costoDelivery = int(input(f"Ingrese el costo del delivery para {nombre}: "))
        #Limpia pantalla
        os.system(op_sys)
        #Instancia la clase e inicia para agregar producto
        tienda = Restaurante(nombre, costoDelivery)
        tienda.ingresar_producto()

    while True:
        eleccion = main2()

        if eleccion == '1':
            os.system(op_sys)
            tienda.listar_productos()
            print('')
        elif eleccion == '2':
            os.system(op_sys)
            nombre_producto = input("Ingrese el nombre del producto que desea vender: ").lower()
            cantidad_requerida = int(input("Ingrese la cantidad requerida: "))
            print('')
            tienda.venta(nombre_producto, cantidad_requerida)
        elif eleccion == '3':
            os.system(op_sys)
            tienda.ingresar_producto()
        #Para que no se tenga que ejecutar el programa una vez por cada tienda
        elif eleccion == '4':
            os.system(op_sys)
            break
        elif eleccion == '5':
            print("Finalizando programa ..")
            time.sleep(2)
            os.system(op_sys)
            # finalizar programa
            exit()


