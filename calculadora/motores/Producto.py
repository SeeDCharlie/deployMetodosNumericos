def productoDeMatrices(matriz1, matriz2):

    matriz3 = []
    for i in range(len(matriz1)):
        matriz3.append([0] * len(matriz2[0]))

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
    print('\nRESULTADO')
    return (matriz3)

    # return ("Recuerda la multiplicacion entre matrices debe ser mxn * nxp")

"""
Matriz = productoDeMatrices()
for i in Matriz:
    print(i)
"""