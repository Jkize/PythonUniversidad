# Jhoan Sebastian Saavedra Romero CC: 1010238118
import pandas as pd
import numpy as np
SIZE=180
gen = ['Female', 'Male',]
genero= np.random.choice(gen, SIZE) 
tv=np.around(np.random.uniform(low=0.0, high=12.01, size=(SIZE,)), decimals=1)
pc=np.around( np.random.uniform(low=0.0, high=18.01, size=(SIZE,))  , decimals=1)
dormir=np.around( np.random.uniform(low=0.0, high=9.01, size=(SIZE,)) , decimals=1) 
A1= np.around( np.random.uniform(low=0.0, high=192.01, size=(SIZE,)), decimals=1)
A2=np.around(np.random.uniform(low=0.0, high=169.01, size=(SIZE,)), decimals=1)
A3=np.around(np.random.uniform(low=0.0, high=192.01, size=(SIZE,)), decimals=1)
Ej=np.around(np.random.uniform(low=0.0, high=9.01, size=(SIZE,)), decimals=1)
prom=np.around(np.random.uniform(low=3.0, high=5.01, size=(SIZE,)), decimals=1)

data={
    'Genero':genero,
    'TV':tv,
    'Computador':pc,
    'Dormir':dormir,
    'AlturaE':A1,
    'AlturaMama':A2,
    'AlturaPapa':A3,
    'EjercicioE':Ej,
    'Promedio':prom
}
 
df = pd.DataFrame(data, columns= ['Genero', 'TV','Computador','Dormir','AlturaE','AlturaMama','AlturaPapa','EjercicioE','Promedio'])
df.to_csv (r'data.csv', index = False, header=True) 
print (df)
