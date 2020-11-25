import sympy as sp
import numpy as np
from random import *
from matplotlib.backends.backend_agg import FigureCanvasAgg

def evalAtPointNP(f, x):
        b = sp.sympify(f).free_symbols
        var = b.pop()
        return sp.sympify(f).subs(var, x)

def montecarlo(a, b, k, n, f):
        # Areabajo la curva
        x = np.linspace(a - 1, b + 1)
        y = evalAtPointNP(f, x)

        # hace el sombreado
        ix = np.linspace(a, b)
        iy = evalAtPointNP(f, ix)
        ne = 0
        #print(random())
        for w in range(n):
                xi = a + (random() * (b - a))
                yi = random() * (k)
                f_xi = evalAtPointNP(f, xi)
                if yi <= f_xi:
                        ne += 1

        return (ne / n) * (b - a) * k

"""
x, y = sp.symbols('x y')
str_ecuacion = input("ingrese la ecuación:")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'gráfica')
sp.plot(funcion, (x, -5, 5), title = 'zoom de la gráfica')

a = float(sp.sympify(input("escriba el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("escriba el extremo superior del intervalo (b): ")))
n = int(input("escriba el número de particiones (debe ser entero): "))
k = float(sp.sympify(input("escriba el valor de k (punto 'y' mas alto de la función): ")))

print("\naproximación: ", montecarlo(a, b, k , n, str_ecuacion ))

sp.plot(funcion, (x, a-0.2, b+0.2), title = 'intervalo seleccionado: ' + str(a) + " , " + str(b))
"""