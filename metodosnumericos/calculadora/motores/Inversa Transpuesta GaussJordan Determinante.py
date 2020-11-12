from numpy.linalg import inv
import numpy as np
import scipy
import scipy.linalg  # SciPy Linear Algebra Library
import sympy as sp

def matrizInver(matrix):
    matrixx = np.array(matrix)
    return inv(matrixx)

def matrixTran(matrix):
    matrixx = np.array(matrix)
    return matrixx.transpose()

def sumaMatrix(matrixA, matrixB):
    matrixx = np.array(matrixA)
    matrixxx = np.array(matrixB)
    return matrixx + matrixxx

def restaMatrix(matrixA, matrixB):
    matrixx = np.array(matrixA)
    matrixxx = np.array(matrixB)
    return matrixx - matrixxx

def multiMatrix(matrixA, matrixB):
    matrixx = np.array(matrixA)
    matrixxx = np.array(matrixB)
    return matrixx * matrixxx

def facL(matrix):
    a = scipy.array(matrix)
    P, L, U = scipy.linalg.lu(a)
    return L

def gaussJordan(mat, res):
    return np.linalg.solve(mat, res)

def determinante(matrix):
    return np.linalg.det(matrix)

matriz1 = [[1, -3, 2],[5,6,-1],[4,-1,3]]
matriz2 = [-3,13,8]

#matriz2 = sp.sympify(Array(input("Matriz 2: ")))

print("Matriz Inversa\n", matrizInver(matriz1))
print("\nMatriz Transpuesta\n", matrixTran(matriz1))
print("\nMultiplicaion de matriz\n", multiMatrix(matriz1, matriz2))
print("\nGauss Jordan\n", gaussJordan(matriz1, matriz2))
print("\nDeterminante\n", determinante(matriz1))
