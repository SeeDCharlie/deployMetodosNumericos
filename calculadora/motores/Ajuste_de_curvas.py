import numpy as np
import matplotlib.pyplot as plt

def getGrados(x):
	grados = 0
	tam = []

	for i in x:
		if i not in tam:
			tam.append(i)

	grados = len(tam)
	if grados > 7:
		grados = 7

	return grados

def graficar(x, y, grados):
	sols = {}

	for grado in range(1, grados-1):
		z = np.polyfit(x, y, grado, full=True)
		sols[grado] = z

	# Pintar datos
	plt.plot(x, y, 'o')

	mayor = 10
	for i in x:
		if i > mayor:
			mayor = i

	menor = 10000
	for i in x:
		if i < menor:
			menor = i

	# Pintar curvas de ajuste
	xp = np.linspace(menor - menor*0.05, mayor + mayor*0.05, 100)
	for grado, sol in sols.items():
		coefs, error, *_ = sol
		p = np.poly1d(coefs)
		plt.plot(xp, p(xp), "-", label="Gr: %s. Error %.3f" % (grado, error) )

	plt.legend()
	plt.show()

def curveFit(n, x, y):
	nCopy = n
	sol = []

	A = x**nCopy
	nCopy -= 1
	while(nCopy >= 1):
		A = np.append(A,x**nCopy, axis=0)
		nCopy -= 1

	A = np.append(A,np.asmatrix(np.ones(A.shape[1])), axis=0)
	A = np.flip(np.rot90(A,3),1)
	y = np.rot90(np.asmatrix(y),3)
	ATras = np.transpose(A)
	S = np.dot(ATras,A)
	z = np.dot(ATras,y)
	SInv = np.linalg.inv(S)
	sol = np.dot(SInv,ATras)
	sol = np.dot(sol,y)

	return sol

def crearEcuacion(cohe):
	n = cohe.shape[0]-1
	k = 0
	funcStr = ''
	while(k != cohe.shape[0]):
		num = np.ndarray.item(cohe[k])
		funcStr += (str(num) if num < 0 else ' + ' + str(num)) + (("*x**" + str(n)) if n > 0 else '')
		k += 1
		n -= 1

	return funcStr


def ajuste(listOne, listTow):
	x = np.array(listOne)
	y = np.array(listTow)
	x1 = np.array([x])
	grados = getGrados(x)
	#graficar(x, y, grados)
	k = curveFit(grados, x1, y)
	return crearEcuacion(k)
	
