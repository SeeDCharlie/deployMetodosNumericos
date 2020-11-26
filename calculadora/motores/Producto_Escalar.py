def productoEscalar(matriz, producto):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]= float(matriz[i][j])*float(producto)

    return matriz

"""
producto = float(input("Ingrese el producto escalar: "))
Matriz = productoEscalar(producto)

print("\nRESULTADO:")
for i in Matriz:
    print (i)
"""