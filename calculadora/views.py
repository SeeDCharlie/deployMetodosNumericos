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

def calcSumaMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mDos = json.loads(request.POST.get('dats'))['mUno']
        mUno = json.loads(request.POST.get('dats'))['mDos']
        matrizResultado = SumaResta.suma(mUno, mDos).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})

def calcRestaMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mDos = json.loads(request.POST.get('dats'))['mDos']
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = SumaResta.resta(mUno, mDos).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})

# multiplicacion de matrices

def calcMultMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        mDos = json.loads(request.POST.get('dats'))['mDos']
        matrizResultado = motorMAtrix.multiMatrix(mUno, mDos).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})

# inversa de una matriz
def calcMaInver(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = motorMAtrix.matrizInver(mUno).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})

# transpuesta de una matriz
def calcMaTrans(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = motorMAtrix.matrixTran(mUno).tolist()
        return JsonResponse({'matrResult': matrizResultado, 'success': True})
    return JsonResponse({'success': False})

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

def calcMonte(request):

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



def grafica(request,funcion, a , b ):

    func = sp.sympify(funcion)
      
    xDats = [i for i in np.arange(float(a),float(b)+1.0, 0.3)]
    yDats = [ float('{:.15f}'.format(float(func.subs('x',i)))) for i in xDats]

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
