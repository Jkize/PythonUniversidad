#Importar las librerias necesarias
import sys
from datetime import datetime
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import pandas as pd

#Función para crear la matriz (size,size) con números randoms de 0 a 50 hecho manualmente
def crearMatriz(size):
    mat=[]
    for i in range(size): 
        mat.append([])
        for j in range(size): 
            mat[i].append(random.randint(0, 50))
    return mat

#Funcion de coseno por seno de la matriz mat y retorna una nueva matriz
def cosenoPorSeno(mat):
    n=len(mat)
    newMat=[]
    for i in range(n):
        newMat.append([])
        for j in range(n):
            newMat[i].append(math.sin(mat[i][j]) * math.cos(mat[i][j]))
    return newMat


#Función para sacar el promedio al hacerlo por python
def promedioPython(iteraciones,size):
    suma=0
    for a in range(iteraciones):    
        start=datetime.now().second
        matrizPython=crearMatriz(size)
        matrizPythonOperacion=cosenoPorSeno(matrizPython) 
        suma+=datetime.now().second - start
        
    promedio=(suma/iteraciones)    
    return promedio

#Función para sacar el promedio al hacerlo por numpy
def promedioNumpy(iteraciones,size):
    suma=0
    for a in range(iteraciones):
        start=datetime.now().second
        matrizNumpy=np.random.randint(50, size=(size, size))
        matrizNumpyOperacion=np.cos(matrizNumpy)*np.sin(matrizNumpy)
        suma+=datetime.now().second - start        
        
    promedio=(suma/iteraciones)    
    return promedio

iteraciones=10
sizes=[800,1200,1700,200]
arrayPromPython=[]
arrayPromNumpy=[]
for i in range(len(sizes)):
    arrayPromPython.append(promedioPython(iteraciones,sizes[i]))
    arrayPromNumpy.append(promedioNumpy(iteraciones,sizes[i]))

matPintar=[]
for i in range(4):
    matPintar.append([])
    matPintar[i].append(arrayPromPython[i])
    matPintar[i].append(arrayPromNumpy[i])

#Pintar

df=pd.DataFrame(matPintar , index=['800','1200',"1700","2000"],
               columns=pd.Index(['Python','Numpy'],name="Ejecución"))
df.plot.bar() 
plt.suptitle('Python vs Numpy',fontsize=14)
plt.ylabel('Tiempo en segundos',fontsize=12)
plt.xlabel('tamaño del arreglo sizexsize',fontsize=12)
