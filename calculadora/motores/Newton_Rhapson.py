import sympy as sp

#import numpy as np
#import matplotlib.pyplot as plt

class motorNewton:

	def __init__(self, funcion):
		self.funcion = funcion

	def f(self,x):
		b = self.funcion.free_symbols
		var = b.pop()
		valor = self.funcion.evalf(subs = {var:x})
		return valor

	def Df(self,x):
		b = self.funcion.free_symbols
		var = b.pop()
		df = sp.diff(self.funcion,var)
		valor = df.evalf(subs = {var:x})
		return valor

	def newtonRhapson(self,x0, tolerancia):

		contador = 1
		print("")
	

		while (abs(self.f(x0)) > tolerancia and contador < 400):

			x1 = x0 - self.f(x0) / self.Df(x0)
			x0 = x1
			contador = contador + 1
        
		if(contador == 700):
			print("\nSe ha alcanzado el numero máximo de iteraciones")
			print("Es posible que no hayan raices")
			print("Intenta con otro punto inicial o un error menor")
			return ["máximo de iteraciones(700) alcanzado",'es posible que no hayan raices']
        
		else:

			print("\nLa raíz es: ", x0)
			print("El error relativo es: ", abs(self.f(x0)))
			return [x0, abs(self.f(x0)) ]
"""
print("Método de Newton Rhapson\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)')
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

inicio = float(sp.sympify(input("Digite el punto de inicio: ")))
tolerancia = float(input("Digite el error de tolerancia: "))

newtonRhapson(inicio, tolerancia)

sp.plot(funcion, (x, inicio - 2, inicio + 2), title = 'Punto de inicio: ' + str(inicio))
"""