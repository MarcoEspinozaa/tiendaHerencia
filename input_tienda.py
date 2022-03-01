
def main():
    tipo = input('\nIngrese la tienda que desea administrar: \n'
        '1. Supermercado\n'
        '2. Farmacia\n'
        '3. Restaurant\n'
        '> ')
    while tipo not in ['1','2','3']:
        tipo = input('Opción no válida, ingrese una de las opciones válidas: ')

    return tipo

def main2():
    eleccion = input('\nIndique la opción de lo que desea realizar: \n'
        '1. Listar los productos existentes\n'
        '2. Realizar una venta\n'
        '3. Volver a agregar un producto\n'
        '4. Empezar de nuevo (desde 0)\n'
        '5. Salir del programa\n'
        '> ')
    while eleccion not in ['1','2','3','4','5']:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')

    return eleccion