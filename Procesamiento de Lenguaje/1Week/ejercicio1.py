import re
import math
import json
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def createVocabulary(text,mapWord,linea):    
    i=0
     
    for ln in linea:
        txt=ln.lower()        
        matchObj=re.findall(r'[\w]+', txt)
        for obj in matchObj:
            if obj in mapWord:
                if i in  mapWord[obj]:
                    mapWord[obj][i]+=1
                else:
                     mapWord[obj][i]=1                
            else:
                mapWord[obj]=dict()
                mapWord[obj][i]=1                
        i=i+1

def createVocabularyStopWords(text,mapWord,linea,stopwords):    
    i=0
     
    for ln in linea:
        txt=ln.lower()        
        matchObj=re.findall(r'[\w]+', txt)
        for obj in matchObj:
            if obj not in stopwords:            
                if obj in mapWord:
                    if i in  mapWord[obj]:
                        mapWord[obj][i]+=1
                    else:
                         mapWord[obj][i]=1                
                else:
                    mapWord[obj]=dict()
                    mapWord[obj][i]=1                
        i=i+1



def vocabulario(mapWord,textName):
    file = open(textName, "w")
    for obj in mapWord:
        file.write(obj+"\n")


def matrix(mapWord,arrayLinea):
    matrix=[] 
    for i in range( len(arrayLinea)-1): 
        row=[]
        j=0
        for obj in mapWord:
            idf=0
            tf=0 
            if i in mapWord[obj]:
                tf=mapWord[obj][i]                           
                tf=tf/len(arrayLinea[i])
                idf=math.log(len(arrayLinea)/len(mapWord[obj]),10)
                print(obj," tf ",tf," DF: ",len(mapWord[obj])," IDF ",idf," Tamaño del documento ",len(arrayLinea[i])) 
              
            row.append(tf*idf)
        j+=1
        matrix.append(row)
    return matrix

def imprimirMatrix(matrix,textName):
    file = open(textName, "w") 
    file.write(json.dumps(matrix) +"\n")

def convertMapToArray(mapWord):
    array=[]
    for obj in mapWord:
        array.append(obj)
    return array

def relevancia(matrix,arrayWord,fileText):
    file = open(fileText, "w") 
    i=0
    for row in matrix:
        minV=-9999
        j=0
        posicion=0
        for dat in row: 
            if dat>minV:
                posicion=j
                minV=dat
            j+=1
        file.write("La palabra más revelante del documento N° {} es {} ".format(i, arrayWord[posicion] )+"\n")
        i=i+1     




def test_run():
    with open("mycorpus.txt","r") as f:
        text=f.read()
        lineas=re.split(r"\n",text)
        mapWord=dict()
        createVocabulary(text,mapWord,lineas) 
        mat=matrix(mapWord,lineas)  
        imprimirMatrix(mat,"matrix1.txt")       
        vocabulario(mapWord,"vocabulario1.txt")
        print(mapWord)

        #Sin stop WOrds
        stop_words = set(stopwords.words('english')) 
        mapWordNotStopWord=dict()
        createVocabularyStopWords(text,mapWordNotStopWord,lineas,stop_words) 
        mat2=matrix(mapWordNotStopWord,lineas) 
        imprimirMatrix(mat2,"matrix2.txt")   
        vocabulario(mapWordNotStopWord,"vocabulario2.txt")        


        #Imprimir el más revelante     
        arrayWord1=convertMapToArray(mapWord)
        relevancia(mat,arrayWord1,"relevancia1.txt") 
        arrayWord2=convertMapToArray(mapWordNotStopWord)
        relevancia(mat,arrayWord2,"relevancia2.txt") 




       

        


if __name__=="__main__":
    test_run()