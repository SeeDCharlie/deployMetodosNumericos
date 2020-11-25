import sympy as sp


class mSimp13:

	def __init__(self):
		self.funcion = ''

	def f(self,x):
		b = self.funcion.free_symbols
		var = b.pop()
		valor = self.funcion.evalf(subs={var:x})
		return valor

	def Df(self,x):
		b = self.funcion.free_symbols
		var = b.pop()
		df = sp.diff(self.funcion,var)
		valor = df.evalf(subs = {var:x})
		return valor
	def simpson13(self,a, b):

		h = (b - a) / 6
		return h*(self.f(a) + 4* self.f((a+b)/2) + self.f(b))

	def simpsonCompuesto13(self,a, b, n):
		if(a > b):
			return -self.simpsonCompuesto13(b, a, n)
		i = a
		h = (b - a) / n
		suma = 0
		while(i <= b):
			if(i + h <= b):
				suma += self.simpson13(i, i+h)
			i += h
		return suma

	def error(self,a, b, n):
		h = (b - a) / n
		error = abs((-h ** 5 / 90) * self.Df((a + b) / 2))
		return error


"""print("Método de Simpson 1/3\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

a = float(sp.sympify(input("Dijite el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("Dijite el extremo superior del intervalo (b): ")))
n = int(input("Dijite el número de particiones (debe ser entero): "))

print("\nAproximación: ", simpsonCompuesto13(a, b, n))
print("Error absoluto: ", abs(error(a, b, n)))#8*x^2 - 8

sp.plot(funcion, (x, a-0.2, b+0.2), title = 'Intervalo seleccionado: ' + str(a) + " , " + str(b))
"""
