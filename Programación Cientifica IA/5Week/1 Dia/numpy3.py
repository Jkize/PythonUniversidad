import numpy as np
import os

print(np.full((3,3),True,dtype=bool))
print(np.ones((3,3),dtype=bool))

arr=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[arr%2==1],"\n")

a=np.arange(15)
#-1 Decide automaticamente los numeros de columnas
# El 3 lo parte en 15 en 3 filas
print(a.reshape(3,-1))

a=np.array([2,6,1,9,10,3,27])
print(a[ (a>=5)&(a<=10) ])

arr=np.arange(1,10)
arr[arr%2==1] = -1 
print(arr,"\n")

a=np.array([1,2,3])
print(np.r_[np.repeat(1,3),np.tile(a,3)])
print("\n")

a=np.arange(10).reshape(2,-1) 
b=np.repeat(1,10).reshape(2,-1)
print("Estoo ",a,"\n",b)

#Conjuntos
#np.intersect1d(a,b)
#np.setdiff1d(a,b) lo que esta en a pero no en b
a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
print("Prueba",np.where(a==b)) 

