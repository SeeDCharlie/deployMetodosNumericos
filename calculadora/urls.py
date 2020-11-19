from django.urls import path
from .views import *

from .views import *
from .views import *

urlpatterns = [
    path('', index),
    path('home/', index,name="home"),
    path('grafica/<str:funcion>/<str:a>/<str:b>', grafica, name="grafica"),
    path('montecarlo/', monteCarlo,name="montecarlo"),

    path('primerCorte/', primerCorte, name="primerCorte"),
    path('segundoCorte/', segundoCorte, name="segundoCorte"),
    path('tercerCorte/', tercerCorte, name="tercerCorte"),

    #url para el calculo de la suma y resta de matrices
    path('restaM/', calcRestaMatriz, name = 'calcRestaMatriz'),
    path('calcSumaMatriz/', calcSumaMatriz, name ='calcSumaMatriz'),

    #url para el calculo de la multiplicacion de matrices
    path('calcMultiMatriz/', calcMultMatriz, name='calcMultiMatrix'),

    #inversa de una matriz
    path('calcMaInv/', calcMaInver, name = 'calcMaInv'),

    #transuesta de una matriz
    path('calcMaTans/', calcMaTrans, name = 'calcMaTrans'),

    #gauss Jordan en una matriz
    path('calcMaGauss/', calcMaGauss, name = 'calcMaGauss'),

    #simpson1/3
    path('calcSimpson13/' , calcSimp13 , name = 'calcSimp13'),
]
