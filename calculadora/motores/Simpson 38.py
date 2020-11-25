import sympy as sp

class mSimp38:
	
	def __init__(self):
		self.funcion = ''

	def f(self, x):
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

	def simpson38Simple(self,a, b):
		m1 = (2*a + b) / 3
		m2 = (a + 2*b) / 3
		f_a = self.f(a)
		f_m1 = self.f(m1)
		f_m2 = self.f(m2)
		f_b = self.f(b)
		integral = (b - a) / 8*(f_a + 3*f_m1 + 3*f_m2 + f_b)
		return integral

	def simpson38(self,a, b, n):
		h = (b - a) / n
		suma = 0
		for i in range(n):
			b = a + h
			area = self.simpson38Simple(a, b)
			suma = suma + area
			a = b
		return suma

	def error(self,a, b, n):
		h = (b - a) / n
		error = float(abs((n*h ** 5 / 80) * self.Df(((a + b) / 2))))
		return error
"""
print("Método de Simpson 3/8\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)')
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

a = float(sp.sympify(input("Dijite el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("Dijite el extremo superior del intervalo (b): ")))
n = int(input("Dijite el número de particiones (debe ser entero): "))

print("\nAproximación: ", simpson38(a, b, n))
print("Error absoluto: ", abs(error(a, b, n)))

sp.plot(funcion, (x, a-0.2, b+0.2), title = 'Intervalo seleccionado: ' + str(a) + " , " + str(b))
"""