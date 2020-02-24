import numpy as np

#Escriba un programa NumPy para crear una matriz de 3x3 con valores que oscilen entre 2 y 10 

array=np.arange(2,11).reshape(3,3)  #reshape 3 x 3
print(array,"\n")
arr = np.flip(array) #Invierte la matriz
print(arr)

NumPy=np.random.rand(90)
print(NumPy)
fa=(NumPy*9/5) + 32
print(fa)
np.savez("centigrado.npz",c=NumPy)
np.savez("fahrenheit.npz",f=fa)