import copy
class Estado:
    estado_padre=None
    def __init__(self,estado=[[5,4,0],[6,1,8],[7,3,2]],pos={"x":0,"y":2}):
        self.estado=estado
        self.pos=pos
    
    def __str__(self):
        estadoStr=""
        for st in self.estado:
            estadoStr+="{} \n".format(st)
        return estadoStr    

    
def genEstado(estado): 
    x=estado.pos["x"]
    y=estado.pos["y"] 
    posibleX=[0,-1,0,1]
    posibleY=[-1,0,1,0]
    estados=[]
    for i in range(4):
        newX=x+posibleX[i]
        newY=y+posibleY[i] 
        if(newX>=0 and newX<3 and newY>=0 and newY<3):
            mat=copy.deepcopy(estado.estado)
            val1=mat[x][y]
            val2=mat[newX][newY]
            mat[x][y]=val2
            mat[newX][newY]=val1
            pos={"x":newX,"y":newY} 
            estados.append(Estado(mat,pos))  
    return estados

def BFS(estado):
    visitado=dict() 
    queue=[]
    queue.append(estado)
    visitado[estado.__str__()]=True
    total=0
    while queue:
        total+=1
        s=queue.pop(0)
        if(s.__str__()==estadoFinal.__str__()):
            return s
        estados=genEstado(s)
        for est in estados:
            est.estado_padre=s
            if(est.__str__() not in visitado):
                visitado[est.__str__()]=True
                queue.append(est)
    print("UN total de ",total,"Pasos")
    
estadoInicial=Estado([[5,4,0],[6,1,8],[7,3,2]],{"x":0,"y":2}) 
estadoFinal=Estado([[1,2,3],[4,5,6],[7,8,0]])  
resEstado=BFS(estadoInicial) 
print("Solución de abajo hacia arriba")
while True:
    print(resEstado)
    resEstado=resEstado.estado_padre
    if(resEstado==None):
        break