from django.urls import path
from .views import *

from .views import *
from .views import *


urlpatterns = [
    path('', index),
    path('home/', index,name="home"),

    path('grafica/<str:funcion>/<str:a>/<str:b>', grafica, name="grafica"),
    path('graficap/<str:funcion>/<str:px>/<str:py>', graficaP, name="graficaP"),

    path('ajuste_de_curvas/', ajuste_de_curvas,name="ajuste_de_curvas"),

    path('secante/', secante,name="secante"),

    path('polinomio/', polinomio,name="polinomio"),

    path('newton_Rhapson/', newton_Rhapson,name="newton_Rhapson"),

    path('falsa_posicion/', falsa_posicion,name="falsa_posicion"),
    
    path('biseccion/', biseccion,name="biseccion"),

    path('IEEE/', IEEE,name="IEEE"),
    
    path('converBases/', converBases,name="converBases"),

    path('montecarlo/', monteCarlo,name="montecarlo"),

    path('trapecios/', trapecios,name="trapecios"),

    path('rectangulos/', rectangulos,name="rectangulos"),

    #suma resta y multiplicacion
    path('SuReMu/',SuMaMu , name = 'SuMaMu'),

    #inversa transpuesta y gauss jordan
    path('inTraGau/',inTraGau , name = 'inTraGau'),

    #simpson 1/3
    path('simpson13/', simpson13, name = 'simpson13'),

    #simpson 3/8
    path('simpson38/', simpson38, name = 'simpson38'),

    #url para el calculo de la suma y resta de matrices
    path('restaM/', calcRestaMatriz, name = 'calcRestaMatriz'),
    path('calcSumaMatriz/', calcSumaMatriz, name ='calcSumaMatriz'),

    #url para el calculo de la multiplicacion de matrices
    path('calcMultiMatriz/', calcMultMatriz, name='calcMultiMatrix'),

    #inversa de una matriz
    path('calcMaInv/', calcMaInver, name = 'calcMaInv'),

    #transuesta de una matriz
    path('calcMaTans/', calcMaTrans, name = 'calcMaTrans'),

    path('calcEscalar', calcEscalar, name = 'calcEscalar'),

    path('calcAjusteC', calcAjusteC, name = 'calcAjusteC'),

    #gauss Jordan en una matriz
    path('calcMaGauss/', calcMaGauss, name = 'calcMaGauss'),

    #simpson1/3
    path('calcSimpson13/' , calcSimp13 , name = 'calcSimp13'),

    path('calcMonte/', calcMonte, name = 'calcMonte'),

    path('calcSimp38/', calcSimp38, name = 'calcSimp38'),

    path('calcTrapecios/', calcTrapecios, name = 'calcTrapecios'),

    path('calcRectangulos/', calcRectangulos, name = 'calcRectangulos'),
    
    path('calcBiseccion/', calcBiseccion, name = 'calcBiseccion'),

    path('calcFalsaPoci/', calcFalsaPoci, name = 'calcFalsaPoci'),

    path('calcNewton/', calcNewton, name = 'calcNewton'),

    path('calcPolinomio/', calcPolinomio, name = 'calcPolinomio'),

    path('calcSecante', calcSecante, name = 'calcSecante'),
]
