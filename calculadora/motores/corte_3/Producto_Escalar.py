def productoEscalar(producto):

    col = int(input("Número de filas: "))
    row = int(input("Número de columnas: "))
    matriz = [[0 for x in range(row)] for y in range(col)]
    print("\nMATRIZ:")

    for i in range(col):
        for j in range(row):
            matriz[i][j] = float(input("Elemento["+str(i)+"]["+str(j)+"]: "))

    for i in range(col):
        for j in range(row):
            matriz[i][j]= matriz[i][j]*producto

    return matriz

producto = float(input("Ingrese el producto escalar: "))
Matriz = productoEscalar(producto)

print("\nRESULTADO:")
for i in Matriz:
    print (i)