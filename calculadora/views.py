from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from matplotlib.figure import Figure
from random import sample
from io import StringIO
from calculadora.motores import SumaResta
from calculadora.motores import Simpson13
from calculadora.motores import Simpson38
from calculadora.motores import MonteCarlo
from calculadora.motores import Trapecios
from calculadora.motores import Rectangulos
from calculadora.motores import Biseccion
from calculadora.motores import Falsa_posicion
from calculadora.motores import Newton_Rhapson
from calculadora.motores import Polinomio

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from calculadora.motores import motorMAtrix
import random
import string
import sympy as sp
from sympy import *
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
import cmath
from sympy import log, sqrt
from sympy.abc import x, y
# Create your views here.


def index(request):
    return render(request, 'calculadora/index.html')

def polinomio(request):
    return render(request, 'calculadora/polinomio.html')

def newton_Rhapson(request):
    return render(request, 'calculadora/newton_Rhapson.html')
    
def falsa_posicion(request):
    return render(request, 'calculadora/falsa_posicion.html')

def biseccion(request):
    return render(request, 'calculadora/biseccion.html')

def IEEE(request):
    return render(request, 'calculadora/IEEE.html')

def converBases(request):
    return render(request, 'calculadora/conversionesBases.html')

def trapecios(request):
    return render(request, 'calculadora/trapecios.html')

def rectangulos(request):
    return render(request, 'calculadora/rectangulos.html')

def monteCarlo(request):
    return render(request, 'calculadora/monteCarlo.html')

def simpson13(request):
    return render(request, 'calculadora/simpson1_3.html')

def simpson38(request):
    return render(request, 'calculadora/simpson3_8.html')

def SuMaMu(request):
    return render(request, 'calculadora/Suma_Resta.html')

def inTraGau(request):
    return render(request, 'calculadora/Inversa_Trans.html')
@csrf_exempt
def calcSumaMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mDos = json.loads(request.POST.get('dats'))['mUno']
        mUno = json.loads(request.POST.get('dats'))['mDos']
        matrizResultado = SumaResta.suma(mUno, mDos).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})
@csrf_exempt
def calcRestaMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mDos = json.loads(request.POST.get('dats'))['mDos']
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = SumaResta.resta(mUno, mDos).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})
@csrf_exempt
# multiplicacion de matrices
def calcMultMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        mDos = json.loads(request.POST.get('dats'))['mDos']
        matrizResultado = motorMAtrix.multiMatrix(mUno, mDos).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})
@csrf_exempt
# inversa de una matriz
def calcMaInver(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = motorMAtrix.matrizInver(mUno).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})
@csrf_exempt
# transpuesta de una matriz
def calcMaTrans(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = motorMAtrix.matrixTran(mUno).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})
@csrf_exempt
# metodo de gauss jordan a una matriz
def calcMaGauss(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        res = [num[-1] for num in mUno]
        mUno = [num[:-1] for num in mUno]
        matrizResultado = motorMAtrix.gaussJordan(mUno, res).tolist()
        letters = string.ascii_lowercase
        rand_letters = random.choices(letters, k=len(matrizResultado))
        matrizResultado = [(rand_letters[i] + " = " + str(dat))
                            for i, dat in enumerate(matrizResultado)]
        return JsonResponse({'matrResult': [matrizResultado], 'success': True})
    return JsonResponse({'success': False})
@csrf_exempt
def calcSimp13(request):
    if request.is_ajax() and request.method == 'POST':
        m = Simpson13.mSimp13()
        m.funcion = sp.sympify(json.loads(request.POST.get('dats'))['funcion'])
        a = float(sp.sympify(json.loads(request.POST.get('dats'))['a']))
        b = float(sp.sympify(json.loads(request.POST.get('dats'))['b']))
        n = int(json.loads(request.POST.get('dats'))['n'])
        resultado = m.simpsonCompuesto13(a, b, n)
        error = abs(m.error(a, b, n))
        print("r simpson 1/3 : ", resultado , "  error : ", error)
        return JsonResponse({'uno': str(resultado), "dos": str(error),"tres":'', 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcSimp38(request):
    if request.is_ajax() and request.method == 'POST':
        m = Simpson38.mSimp38()
        m.funcion = sp.sympify(json.loads(request.POST.get('dats'))['funcion'])
        a = float(sp.sympify(json.loads(request.POST.get('dats'))['a']))
        b = float(sp.sympify(json.loads(request.POST.get('dats'))['b']))
        n = int(json.loads(request.POST.get('dats'))['n'])
        resultado = m.simpson38(a, b, n)
        error = abs(m.error(a, b, n))
        print("r simpson 1/3 : ", resultado , "  error : ", error)
        return JsonResponse({'uno': str(resultado), "dos": str(error),"tres":'', 'success': True})
    return JsonResponse({'success':False})
@csrf_exempt
def calcMonte(request):
    if request.is_ajax() and request.method == 'POST':
        funcion = json.loads(request.POST.get('dats'))['funcion']
        a = float(sp.sympify(json.loads(request.POST.get('dats'))['a']))
        b = float(sp.sympify(json.loads(request.POST.get('dats'))['b']))
        k = float(sp.sympify(json.loads(request.POST.get('dats'))['k']))
        n = int(json.loads(request.POST.get('dats'))['n'])
        resultado = MonteCarlo.montecarlo(a, b, k, n, funcion)
        print("r monte carlo : ", resultado )
        return JsonResponse({'uno': str(resultado), "dos": '',"tres":'', 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcTrapecios(request):
    if request.is_ajax() and request.method == 'POST':
        funcion = json.loads(request.POST.get('dats'))['funcion']
        a = float(json.loads(request.POST.get('dats'))['a'])
        b = float(json.loads(request.POST.get('dats'))['b'])
        n = int(json.loads(request.POST.get('dats'))['n'])
        resultado = Trapecios.trapecios(funcion, a, b, n)
        print("r trapecios : ", resultado )
        return JsonResponse({'uno': str(resultado[0]), "dos": str(resultado[1]),"tres":'', 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcRectangulos(request):
    if request.is_ajax() and request.method == 'POST':
        funcion = json.loads(request.POST.get('dats'))['funcion']
        a = float(json.loads(request.POST.get('dats'))['a'])
        b = float(json.loads(request.POST.get('dats'))['b'])
        n = int(json.loads(request.POST.get('dats'))['n'])
        resultado = Rectangulos.MetodoRentangulos(funcion, a, b, n)
        print("r trapecios : ", resultado )
        return JsonResponse({'uno': str(resultado[0]), "dos": str(resultado[1]),"tres":str(resultado[2]), 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcBiseccion(request):
    if request.is_ajax() and request.method == 'POST':
        funcion = sp.sympify(json.loads(request.POST.get('dats'))['funcion'])
        mot = Biseccion.motorBisec(funcion)
        a = float(sp.sympify(json.loads(request.POST.get('dats'))['a']))
        b = float(sp.sympify(json.loads(request.POST.get('dats'))['b']))
        error = float(json.loads(request.POST.get('dats'))['error'])
        resultado = mot.biseccion(a, b, error)
        print("r biseccion : ", resultado )
        return JsonResponse({'uno': str(resultado[0]), "dos": str(resultado[1]),"tres":'', 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcFalsaPoci(request):
    if request.is_ajax() and request.method == 'POST':
        funcion = sp.sympify(json.loads(request.POST.get('dats'))['funcion'])
        mot = Falsa_posicion.motorFalsaPoci(funcion)
        a = float(sp.sympify(json.loads(request.POST.get('dats'))['a']))
        b = float(sp.sympify(json.loads(request.POST.get('dats'))['b']))
        error = float(json.loads(request.POST.get('dats'))['error'])
        resultado = mot.falsaPosicion(a, b, error)
        print("r biseccion : ", resultado )
        return JsonResponse({'uno': str(resultado[0]), "dos": str(resultado[1]),"tres":'', 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcNewton(request):
    if request.is_ajax() and request.method == 'POST':
        funcion = sp.sympify(json.loads(request.POST.get('dats'))['funcion'])
        mot = Newton_Rhapson.motorNewton(funcion)
        valor_x = float(sp.sympify(json.loads(request.POST.get('dats'))['valor_x']))
        error = float(json.loads(request.POST.get('dats'))['error'])
        resultado = mot.newtonRhapson(valor_x, error)
        print("r newton rhapson : ", resultado )
        return JsonResponse({'uno': str(resultado[0]), "dos": str(resultado[1]),"tres":'', 'success': True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcPolinomio(request):
    if request.is_ajax() and request.method == 'POST':
        coeficientes = list(sp.sympify(json.loads(request.POST.get('dats'))['coeficientes']))
        grado = int(sp.sympify(json.loads(request.POST.get('dats'))['grado']))
        print("coeficientes : ", coeficientes)
        resultado = Polinomio.polinomio(grado, coeficientes)
        print("r polinomios : ", resultado )
        return JsonResponse({'uno': str(resultado), "dos": '',"tres":'', 'success': True})
    return JsonResponse({'success':False})

def grafica(request,funcion, a , b ):


    U, D = sp.symbols('U D')
    div = lambda U,D: U/D
    func = sp.sympify(funcion, locals = {'div': div})
      
    xDats = [i for i in np.arange(float(a),float(b)+1.0, 0.3)]
    yDats = [ float('{:.15f}'.format(float(func.subs(x,i)))) for i in xDats]

    fig = Figure()
    canvas = FigureCanvasAgg(fig)
    ax = fig.add_subplot(111)
    ax.plot(xDats, yDats)

    ax.set(xlabel='eje x', ylabel='eje y',
           title='Grafica de la Funcion')
    ax.grid()

    response = HttpResponse(content_type = 'image/jpg')
    
    canvas.print_jpg(response)
    return response
