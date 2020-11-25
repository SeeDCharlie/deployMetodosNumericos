def productoDeMatrices():
    print('Ingresa el orden de su Matriz A')
    filas1, columnas1 = int(input("Número de filas matriz A: ")), int(input("Número de columnas matriz A: "))
    print('\nIngresa el orden de su Matriz B')
    filas2, columnas2 = int(input("Número de filas matriz B: ")), int(input("Número de columnas matriz B: "))

    if (columnas1 == filas2):
        matriz1 = []
        for i in range(filas1):
            matriz1.append( [0] * columnas1 )

        matriz2 = []
        for i in range(filas2):
            matriz2.append( [0] * columnas2 )

        print('\nPRIMER MATRIZ')
        for i in range(filas1):
            for j in range(columnas1):
                matriz1[i][j] = float(input('Elemento[%d,%d]: ' % (i, j)))
        print('\nSEGUNDA MATRIZ')
        for i in range(filas2):
            for j in range(columnas2):
                matriz2[i][j] = float(input('Elemento[%d,%d]: ' % (i, j)))

        matriz3 = []
        for i in range(filas1):
            matriz3.append( [0] * columnas2 )

        for i in range(filas1):
            for j in range(columnas2):
                for k in range(filas2):
                    matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
        print ('\nRESULTADO')
        return (matriz3)
    else:
        return ("Recuerda la multiplicacion entre matrices debe ser mxn * nxp")


Matriz = productoDeMatrices()
for i in Matriz:
    print (i)
