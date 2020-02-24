import re
import math
import json
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
#BY Jhoan Sebastian Saavedra Romero & Juan Pablo Hernández Jiménez

def filterStopWords(arrayText):
    stop_words = set(stopwords.words('english'))
    newArray=[]
    for dt in arrayText:
        if dt not in stop_words:
            newArray.append(dt)
    return newArray


def vocabulary(arrayText,posRow,vocabulary):
    for obj in arrayText:
        if obj in vocabulary:
            if posRow in vocabulary[obj]:
                vocabulary[obj][posRow]+=1
            else:
                vocabulary[obj][posRow]=1
        else:
            vocabulary[obj]=dict()
            vocabulary[obj][posRow]=1

def matrizPonderacion(lengthArrayToken,vocabulary):
    matriz=[]
    for i in range(len(lengthArrayToken)):
        row=[]        
        for obj in vocabulary:
            idf=0
            tf=0
            if i in vocabulary[obj]:
                tf=vocabulary[obj][i]
                tf=tf/(len(lengthArrayToken[i]))
                idf=math.log(len(lengthArrayToken)/len(vocabulary[obj]),10)
            row.append(tf*idf)
        matriz.append(row)
    return matriz

def imprimirMatriz(matriz,textName):
    file=open(textName,"w")
    file.write(json.dumps(matriz))

def imprimirMap(mapa,textName):
    file = open(textName, "w")
    for obj in mapa:
        file.write(obj+"\n")

def convertMapToArray(mapa):
    array=[]
    for obj in mapa:
        array.append(obj)
    return array

def imprimirRelevancia(matriz,arrayWord,fileText):
    file = open(fileText, "w") 
    i=1 
    for row in matriz:
        maxV=-1
        j=0
        posicion=0
        for dat in row: 
            if dat>maxV:
                posicion=j
                maxV=dat
            j+=1        
        file.write("La palabra más revelante del documento N° {} es {} con ponderación {} ".format(i, arrayWord[posicion],maxV )+"\n")
        i=i+1     


def test_run():
    
    arrayToken1=[]
    arrayToken2=[]
    vocabulary1=dict()
    vocabulary2=dict()
     
    with open("mycorpus.txt","r") as f:  
        arrayText= re.split(r"\n",f.read())
        i=0        
        for line in arrayText: 
            arrayLine1=re.findall(r'[\w]+', line.lower())
            arrayLine2=filterStopWords(arrayLine1)
            arrayToken1.append(arrayLine1)
            arrayToken2.append(arrayLine2)
            vocabulary(arrayLine1,i,vocabulary1)
            vocabulary(arrayLine2,i,vocabulary2)
            i+=1   
     
    imprimirMap(vocabulary1,"vocabularioConStopWait.txt")
    imprimirMap(vocabulary2,"vocabularioSinStopWait.txt")

    matriz1=matrizPonderacion(arrayToken1,vocabulary1)
    matriz2=matrizPonderacion(arrayToken2,vocabulary2)

    imprimirMatriz(matriz1,"matrizConStopWait.txt")
    imprimirMatriz(matriz2,"matrizSinStopWait.txt")
    imprimirRelevancia(matriz1,convertMapToArray(vocabulary1),"relevanciaConStopWait.txt")
    imprimirRelevancia(matriz2,convertMapToArray(vocabulary2),"relevanciaSinStopWait.txt")
        
        



if __name__=="__main__":
    test_run()