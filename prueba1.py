
flag = 0
stock = 10
while flag == 0:
    requerido = int(input("ingrese cantidad requerida: "))

    if requerido <= stock and requerido <= 3:
        stock -= requerido
        print(requerido, stock)
    elif stock < requerido and stock > 0: 
        requerido = stock
        stock = 0
        print(requerido, stock)
    elif stock == 0:
        print("no hay stock")
        flag = 1
    else: 
        print('excede pedido maximo')
        flag = 1
        print(requerido, stock)
