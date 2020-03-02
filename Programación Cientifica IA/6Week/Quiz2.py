#Jhoan Sebastian Saavedra Romero
import matplotlib.pyplot as plt 
 
labels=['Lenguaje Extranjera','Ciencias Computacionales','Ingeniería','Matemáticas','Biologia','Física','Humanidades','Educación','Quimica Analítica']
values=[4,21,19,15,10,9,8,7,7]  
explode=[0,0,0.2,0,0,0,0,0,0] 
plt.title('Carreras')
plt.pie(values,labels=labels,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
plt.axis("equal")
plt.show() 
