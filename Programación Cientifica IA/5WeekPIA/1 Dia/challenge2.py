import numpy as np
import random
num=random.randrange(100)
print("Numero random creado: {} ".format(num))
array=np.arange(0,num)
print("El tamaño del arreglo es {} ".format(array.size))
print("El tamaño de un elemento en bytes es {} ".format(array.itemsize))
print("Los bytes consumidos totales del arreglo es: {} ".format(array.size*array.itemsize))