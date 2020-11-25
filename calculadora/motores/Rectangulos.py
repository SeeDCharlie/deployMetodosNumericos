from sympy import*
from math import*
from math import pi
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
    ##_________________________Evaluar lafuncion
def OperarFuncion(f,x): ##_____________(3)
    #print ("Se evaluca la funcion "+ str(f))
    #y=eval(str(f))
    #resultado="{}".format(y)
    #print ("Se evaluca la funcion "+ str(f) +" ="+str(resultado))
    #return (resultado) 
    return eval(str(f)) 

def Ordenar_Funcion(Val,funcion):##_____________(1)  
    ## Evaluar lafuncion    tipo String 
    #salida=Ev_funcion(Val, funcion)
    ##obtendra el valor de la funcion tipo long
    valor=OperarFuncion(funcion,Val)
    #print("-Valor al evaluar con el punto medio= "+ str(valor))
    return ( float(valor) )


##________________________________________________ Implementación
def Izquierda(f,a,b,n,Delta,valores):
    ##___ sumatoria
    suma=0
    c=0
    while(c<=n-1):
        ##print("ñl"+str(valores[c] ))
        suma=suma+(Ordenar_Funcion(valores[c],f) )
        c+=1
    suma=suma*Delta
    print ("Suma totalmente loca izquierdo= "+str(suma))
    return suma
    
def Derecha(f,a,b,n,Delta,valores):
    ##___ sumatoria
    suma=0
    c=1
    while(c<=n):
        ##print("ñl"+str(valores[c] ))
        suma=suma+(Ordenar_Funcion(valores[c],f) )
        c+=1
    suma=suma*Delta
    print ("Suma totalmente loca Derecho= "+str(suma))
    return suma

def PuntoMedio(f,a,b,n,Delta,valores):
    total=SacarValorMedio(valores,n,f)
    total= total*Delta
    print  ("Suma totalmente loca punto Medio= "+str(total))
    return total
##_________________________________________________
def SacarValorMedio(valores,n,f):##______________________________________(5)
    c=0
    aux=0
    suma=0
    while(c<n):
        aux= ((valores[c]+valores[c+1] )/2)
        ##print ("puntos medios ="+str(aux) )
        suma= suma+(Ordenar_Funcion(aux,f))
        c+=1
    
    return suma
def Valores(a,b,Delta,n):##__________________________________(4)
    #Salida= array(n)
    print("MétodoValores ")
    listta= []
    c=0
    listta.append(a)
    aux=a
    while(c<n):        
        aux=aux+Delta
        listta.append(aux)    
        c+=1  
    return listta

def EncontrarDelta(a,b,n):##_________________________________(3)
    return ((b-a)/n)

def ComprobarN(n):##_________________________________________(2)
    print ("Método Comprobar ")
    if(n>0):
        return True
    else:
        return False

def MetodoRentangulos(f,a,b,n):##____________________________(1)
    print ("Metodo Rentangulos")
    if ComprobarN(n):
        print("El valor de los rectangulos si es entero positivo "+str(n))
        Delta=EncontrarDelta(a,b,n)
        
        valores=Valores(a,b,Delta,n)
        print("ValoreDelta "+str(Delta)+"nuemero n="+str(n))  
        
        return [abs(Izquierda(f,a,b,n,Delta,valores)), abs(Derecha(f,a,b,n,Delta,valores)), abs(PuntoMedio(f,a,b,n,Delta,valores)) ]
    else:
        print ("El valor de los rectangulos no es entero positivo")
        return ["Nan","Nan", "Nan"]
##________________________________________________LLamadas


#"(x-(1/2))*exp((-1/2)*x**2)+cos(x)"
#"(sin((1/2)+x**2))/((1/2)+x**2)"
#"exp(-0.75*x)+sin(x)-0.5*(x**2)+1.25*x" - (-0.65) (2.81)
#"atan(x)"   [0,2] 
#"(1)/(1+x**2)" [0,1]
"""
Funcion ="exp(x/2)+(cos(1/2+x))/(1/2+x)"
ValorA  = 0
ValorB  = 3.1416
NRectangulos= int (1000)
#print ("inicio")
MetodoRentangulos(Funcion,ValorA, ValorB,NRectangulos)
"""