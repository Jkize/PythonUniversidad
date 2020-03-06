import numpy as np
data=np.arange(10)
SIZE=20
gen = ['Female', 'Male',]
genero= np.random.choice(gen, SIZE)
horas=np.random.uniform(low=0.0, high=24.0, size=(SIZE,))
computador=np.random.uniform(low=0.0, high=24.0, size=(SIZE,))
dormir=np.random.uniform(low=0.0, high=24.0, size=(SIZE,))
alturaEPulgada=np.random.uniform(low=50.0, high=90.0, size=(SIZE,))
alturaMPulgada=np.random.uniform(low=50.0, high=90.0, size=(SIZE,))
alturaPPulgada=np.random.uniform(low=50.0, high=90.0, size=(SIZE,))
ejercicio=np.random.uniform(low=0.0, high=24.0, size=(SIZE,)) 
data=[genero,horas,computador,dormir,alturaEPulgada,alturaMPulgada,alturaPPulgada,ejercicio]
 
f=open('newData3.csv','a')
n=1
for dt in data:
    if(n==1):
        np.savetxt(f,dt,'%s',delimiter=", ")
    else:
        np.savetxt(f,dt,'%.2f',delimiter=", ")
    n+=1
    f.write("\n")