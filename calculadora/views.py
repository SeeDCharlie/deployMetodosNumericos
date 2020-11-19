from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
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

# Create your views here.

def index(request):
    return render(request,'calculadora/index.html')

@csrf_exempt 
def calcSumaMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mDos = json.loads(request.POST.get('dats'))['mUno']
        mUno = json.loads(request.POST.get('dats'))['mDos']
        matrizResultado = SumaResta.suma(mUno,mDos).tolist()
        return JsonResponse({'matrResult':matrizResultado, 'success':True})      
    return JsonResponse({'success':False})

@csrf_exempt
def calcRestaMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mDos = json.loads(request.POST.get('dats'))['mDos']
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = SumaResta.resta(mUno,mDos).tolist()
        return JsonResponse({'matrResult':matrizResultado, 'success':True})
    return JsonResponse({'success':False})

#multiplicacion de matrices

@csrf_exempt
def calcMultMatriz(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        mDos = json.loads(request.POST.get('dats'))['mDos']
        matrizResultado = motorMAtrix.multiMatrix(mUno,mDos).tolist()
        return JsonResponse({'matrResult':matrizResultado, 'success':True})
    return JsonResponse({'success':False})

#inversa de una matriz
@csrf_exempt
def calcMaInver(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = motorMAtrix.matrizInver(mUno).tolist()
        return JsonResponse({'matrResult':matrizResultado, 'success':True})
    return JsonResponse({'success':False})
@csrf_exempt
#transpuesta de una matriz
def calcMaTrans(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        matrizResultado = motorMAtrix.matrixTran(mUno).tolist()
        return JsonResponse({'matrResult':matrizResultado, 'success':True})
    return JsonResponse({'success':False})
@csrf_exempt
#metodo de gauss jordan a una matriz
def calcMaGauss(request):
    if request.is_ajax() and request.method == 'POST':
        mUno = json.loads(request.POST.get('dats'))['mUno']
        res = [num[-1] for num in mUno]
        mUno = [num[:-1] for num in mUno]
        matrizResultado = motorMAtrix.gaussJordan(mUno, res).tolist()
        letters = string.ascii_lowercase
        rand_letters = random.choices(letters,k=len(matrizResultado))
        matrizResultado = [(rand_letters[i] +" = "+ str(dat)) for i, dat in enumerate(matrizResultado)]
        return JsonResponse({'matrResult':[matrizResultado], 'success':True})
    return JsonResponse({'success':False})

@csrf_exempt
def calcSimp13(request):
    if request.is_ajax() and request.method == 'POST':
        a = float(sp.sympify(json.loads(request.POST.get('dats'))['a']))
        b = float(sp.sympify(json.loads(request.POST.get('dats'))['b']))
        n = int(json.loads(request.POST.get('dats'))['n'])
        resultado = Simpson13.simpsonCompuesto13(a,b,n)
        error = abs(error(a, b, n))
        return JsonResponse({'result':resultado,'error':error, 'success':True})
    return JsonResponse({'success':False})
    print("")

def primerCorte(request):
    return render(request, 'calculadora/cortes/corte1.html')

def segundoCorte(request):
    return render(request, 'calculadora/cortes/corte2.html')

def tercerCorte(request):
    return render(request, 'calculadora/cortes/corte3.html')

def trapecios(request):
    return render(request,'')

def monteCarlo(request):
    return render(request, 'calculadora/monteCarlo.html')




def grafica(request,funcion, a , b ):

    func = sp.sympify(funcion)
      
    xDats = [i for i in range(int(a),int(b)+1)]
    yDats = [ func.subs('x',i) for i in xDats]

    fig, ax = plt.subplots()
    ax.plot(xDats, yDats)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response
