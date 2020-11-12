import sympy as sp


def f(x):
	b = funcion.free_symbols
	var = b.pop()
	valor = funcion.evalf(subs={var:x})
	return valor

def Df(x):
	b = funcion.free_symbols
	var = b.pop()
	df = sp.diff(funcion,var)
	valor = df.evalf(subs = {var:x})
	return valor

def simpson13(a, b):
	h = (b - a) / 6
	return h*(f(a) + 4* f((a+b)/2) + f(b))

def simpsonCompuesto13(a, b, n):
	if(a > b):
		return -simpsonCompuesto13(b, a, n)
	i = a
	h = (b - a) / n
	suma = 0
	while(i <= b):
		if(i + h <= b):
			suma += simpson13(i, i+h)
		i += h
	return suma

def error(a, b, n):
	h = (b - a) / n
	error = abs((-h ** 5 / 90) * Df((a + b) / 2))
	return error

print("Método de Simpson 1/3\n")
x, y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)')
sp.plot(funcion, (x, -5, 5), title = '(Ampliación) Ten en cuenta la(s) raíz(es)')

a = float(sp.sympify(input("Dijite el extremo inferior del intervalo (a): ")))
b = float(sp.sympify(input("Dijite el extremo superior del intervalo (b): ")))
n = int(input("Dijite el número de particiones (debe ser entero): "))

print("\nAproximación: ", simpsonCompuesto13(a, b, n))
print("Error absoluto: ", abs(error(a, b, n)))

sp.plot(funcion, (x, a-0.2, b+0.2), title = 'Intervalo seleccionado: ' + str(a) + " , " + str(b))