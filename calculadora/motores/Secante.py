import sympy as sp

#import numpy as np
#import matplotlib.pyplot as plt


class motor_secante:

	def __init__(self, funcion):
		self.funcion = funcion

	def f(self, x):
		b = self.funcion.free_symbols
		var = b.pop()
		valor = self.funcion.evalf(subs = {var:x})
		return valor

	def secante(self,a, b, tolerancia):

		c = 0
		iteraciones = 0

		while(abs(self.f(c)) < tolerancia and iteraciones < 501):
			c = b - ((b-a) / (self.f(b)-self.f(a))) * self.f(b)
			a = b
			b = c
			iteraciones = iteraciones + 1

		if(iteraciones >= 500):
			print("\nSe ha alcanzado el numero máximo de iteraciones")
			print("Es posible que no hayan raices en el intervalo")
			print("Intenta con otro intervalo")
			return ['Se ha alcanzado el numero máximo de iteraciones(500)','Intenta con otro intervalo']
		else:
			print("\nLa raíz es: ", c)
			print("El error relativo es: ", abs(self.f(c)))
			return [c,abs(self.f(c)) ]


"""
print("Método de la secante\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)')
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

a = float(sp.sympify(input("Digite el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("Digite el extremo superior del intervalo (b): ")))
tolerancia = float(input("Digite el error de tolerancia: "))

secante(a, b, tolerancia)

sp.plot(funcion, (x, a-0.5, b+0.5), title = 'Intervalo seleccionado: ' + str(a) + " , " + str(b))
"""