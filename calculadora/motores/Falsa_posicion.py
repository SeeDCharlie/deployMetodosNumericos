import sympy as sp

#import numpy as np
#import matplotlib.pyplot as plt


class motorFalsaPoci :

	def __init__(self, funcion):
		self.funcion = funcion
	

	def f(self,x):
		b = self.funcion.free_symbols
		var = b.pop()
		valor = self.funcion.evalf(subs = {var:x})
		return valor

	def falsaPosicion(self,a, b, tolerancia):

		error = 10

		if (self.f(a) * self.f(b) < 0):

			contador = 1
			print("")
		
			while error > tolerancia and contador < 200:

				fa = self.f(a)
				fb = self.f(b)
				m = ((a * fb) - (b * fa)) / (fb - fa)
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
			return ['Los intervalos no contienen la raíz', 'Nan']
"""
print("Método de falsa posición\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)')
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

a = float(sp.sympify(input("Digite el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("Digite el extremo superior del intervalo (b): ")))
tolerancia = float(input("Digite el error de tolerancia: "))

falsaPosicion(a, b, tolerancia)

sp.plot(funcion, (x, a-0.5, b+0.5), title = 'Intervalo seleccionado: ' + str(a) + " , " + str(b))
"""

