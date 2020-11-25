import sympy as sp

import numpy as np
import matplotlib.pyplot as plt


class motorBisec :

	def __init__(self, func):
		self.funcion = func

	def f(self,x):
		b = self.funcion.free_symbols
		var = b.pop()
		valor = self.funcion.evalf(subs={var:x})
		return valor

	def biseccion(self, a, b, tolerancia):

		error = 10

		if (self.f(a) * self.f(b) < 0):

			contador = 1
			print("")
	

			while error > tolerancia and contador < 200:

				m = (a + b) / 2
				fa = self.f(a)
				fm = self.f(m)
			
				if fm == 0:
					raiz = m
					break
				elif fa * fm < 0:
					b = m
				else:
					a = m
				raiz = m
				error = abs(fm)
				contador = contador + 1
	
	
			print("\nLa raíz es: ", raiz)
			print("El error relativo es: ", error)
			return [raiz, error]
		else:
			print("\nLos intervalos no contienen la raíz")
			return ['Los intervalos no contienen la raíz','Nan']
"""
print("Método de Bisección\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)')
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

a = float(sp.sympify(input("Digite el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("Digite el extremo superior del intervalo (b): ")))
tolerancia = float(input("Digite el error de tolerancia: "))

biseccion(a, b, tolerancia)

sp.plot(funcion, (x, a-0.5, b+0.5), title = 'Intervalo seleccionado: ' + str(a) + " , " + str(b))
"""