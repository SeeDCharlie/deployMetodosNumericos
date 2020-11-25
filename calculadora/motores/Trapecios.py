from sympy import*
from math import*
from math import pi
from random import*
import numpy as np
from numpy import array
import matplotlib.pyplot as plt


##_________________________Evaluar lafuncion
def OperarFuncion(f,x): ##_____________(3)
    #print ("Se evaluca la funcion "+ str(f))
    #y=eval(str(f))
    #resultado="{}".format(y)
    #print ("Se evaluca la funcion "+ str(f) +" ="+str(resultado))
    return eval(str(f)) 

def Ordenar_Funcion(Val,funcion):##_____________(1)  
    ## Evaluar lafuncion    tipo String 
    #salida=Ev_funcion(Val, funcion)
    ##obtendra el valor de la funcion tipo long
    #valor=OperarFuncion(salida)
    valor =OperarFuncion(funcion,Val)
    #print("-Valor al evaluar con el punto medio= "+ str(valor))
    return ( float(valor) )
##________________________________________________________

def EncontrarDelta(a,b,n):##_________________________________(1)
    return ((b-a)/n)
def Valores(a,b,Delta,n):##__________________________________(3)
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
def ComprobarN(n):##_________________________________________(2)
    print ("Método Comprobar ")
    if(n>0):
        return True
    else:
        return False

def trapecios(f,a,b,n):##___________________________(1)    
    print ("Metodo Trapecios Locos")
    if ComprobarN(n):
        print("El valor de los rectangulos si es entero positivo ="+str(n))
        Delta=EncontrarDelta(a,b,n)
        print("Delta o altura es = "+str(Delta))
        valores=Valores(a,b,Delta,n)
        #print("ValoreDelta "+str(Delta)+"nuemero n="+str(n))  
        aumento=a
        suma=Ordenar_Funcion(a,f)
       # print("Valor aumento = "+str(a ))
        #print("f(a) con aumento = "+str(Ordenar_Funcion(a,f)))
        if(n!=1):
            #print ("******************+Se evalua con ["+str(n)+"] trapecio")
           # c=2
           # while(c<=n):
               # aumento=aumento+Delta
                #print("Valor aumento = "+str(aumento))
               # suma=suma+(2*Ordenar_Funcion(aumento,f))
               # print("f("+str(c)+") con aumento = "+str(Ordenar_Funcion(aumento,f)))
                #c+=1
            print("Valor aumento = "+str(b))
            suma=suma+(Ordenar_Funcion(b,f))
            print("f(b) con aumento = "+str(Ordenar_Funcion(b,f)))
            suma=(suma*(Delta/2))
            print("area es = "+str(suma))
            Err=ErroTruncamiento(f,a,b)
            print("El Error de truncamiento es = "+str(Err))
            
            return [suma, Err]
        else:
            print ("Solo se evalua con un trapecio")
            suma=suma+(  Ordenar_Funcion(a,f))
            print ("con a="+str(suma))
            suma=suma+(  Ordenar_Funcion(b,f))
            print ("con b="+str(suma))
            suma= suma*Delta*(0.5)#0.5 es el unmedio de la formula
            print("area es = "+str(suma))
            Err=ErroTruncamiento(f,a,b)
            print("El Error de truncamiento es = "+str(Err))
            return [suma, Err]
        #**

    else:
        print ("El valor de los rectangulos no es entero positivo")
##_______________________________________________________-

def numerosAletorios(a,b):
    return uniform(a,b)


def derivadasLocas(f):
    f=diff(f)
    f=diff(f)
    return f

def ErroTruncamiento(f,a,b):
    derivadaF=derivadasLocas(f)
    Epsilon =numerosAletorios(a,b)
    return (-1/12)*(Ordenar_Funcion(Epsilon,derivadaF))*((b-a)**3)


##____________________________________________________________________Error



##________________________________________________________
#"(x-(1/2) )*exp((-1/2)* x^2})+cos(x)"
#"(x**3)/(1+(x**(1/2)))"
#"(sin((1/2)+x**2))/((1/2)+x**2)"  -pi/2
#"((1)/(sqrt(2*pi)))*exp((-x**2)/(2))"
"""
Funcion = "exp(x/2)+(cos(1/2+x))/(1/2+x)"
ValorA  = 0
ValorB  = 3.1416
Trapecios= int(1000)
print ("inicio")
print(trapecios(Funcion,ValorA,ValorB,Trapecios) )
"""