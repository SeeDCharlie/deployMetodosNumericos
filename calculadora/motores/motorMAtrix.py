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
