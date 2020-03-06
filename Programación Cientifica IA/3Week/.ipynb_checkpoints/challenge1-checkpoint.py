
import math

#Jhoan Sebastian Saavedra Romero

def factorial(num):
    if(num==0):
        return 1
    return num*factorial(num-1)

def ecuacion_cuadratica(a,b,c):
    val= b*b - 4*a*c
    if(val>=0):
        r1=(-b + math.sqrt(val))/(2*a)
        r2=(-b - math.sqrt(val))/(2*a)
        return {"r1":r1,"r2":r2}
    else:         
        r1="{} + √({})i/{}".format( (-b/2*a), val,2*a)
        r2="{} - √({})i/{}".format( (-b/2*a), val,2*a) 
        return {"r1":r1,"r2":r2}


#Factorial
n=5
print(factorial(n))

#Funciòn cuadràtica valida
a=1
b=6
c=8
print(ecuacion_cuadratica(a,b,c))
#Funciòn cuadràtica con resultados imaginarios
a1=1
b1=1
c1=1
print(ecuacion_cuadratica(a1,b1,c1))
