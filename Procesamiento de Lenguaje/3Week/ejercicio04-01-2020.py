#By JHOAN SEBASTIAN SAAVEDRA ROMERO
import xml.etree.ElementTree as ET
import re
from os import walk
from os import listdir
from os.path import isfile, join

from gensim.parsing.porter import PorterStemmer
from gensim.parsing.preprocessing import remove_stopwords
from gensim import corpora
from gensim import models
from gensim import similarities
from smart_open import smart_open

 

#Procesamiento de un texto utilizando las funciones de Gensim
#Y quitando simbolos
def process(text): 
    p = PorterStemmer()
    doc_nor=text.lower()
    doc_sw=remove_stopwords(doc_nor)
    doc_stem= p.stem_sentence(doc_sw)
    stem=re.findall(r'[\w]+', doc_stem)
    return doc_stem.split()

#Guarda  el dictionario
def saveDic(docDict):
    dictionary=corpora.Dictionary(docDict)
    dictionary.save('dict.dict')
     


#Dicionario de id y document del XML
def processXML(root): 
    xml=dict()
    _nafHeader=list(root.iterfind('nafHeader'))[0]
    content=list(root.iterfind('raw'))[0].text
    #title=list(_nafHeader.iterfind('fileDesc'))[0].attrib['title']
    _id=list(_nafHeader.iterfind('public'))[0].attrib['publicId']    
    document=content
    xml["document"]=document
    xml["id"]=_id

    return xml    


class MyCorpus(object):
     
    def __iter__(self):
        mypath='./doc'
        dictionary=corpora.Dictionary.load('dict.dict','r')
        for f in listdir(mypath):
            if isfile(join(mypath,f)):
                root=ET.parse('{}/{}'.format(mypath,f))
                xml=processXML(root)
                yield dictionary.doc2bow(process(xml["document"]))


def matrixSimilarity():
    tfidf=models.TfidfModel.load("tfidfCorpus.mm")
    corpus=corpora.MmCorpus('corpus.mm')
    index=similarities.MatrixSimilarity(tfidf[corpus])
    index.save('tfidfSimilarity.index')

def queries(idList):
    #cargar diccionario
    #cargar tfidf
    #cargar index
    mypath="./query"
    dictionary=corpora.Dictionary.load('dict.dict','r')    
    tfidf=models.TfidfModel.load("tfidfCorpus.mm")
    index=similarities.MatrixSimilarity.load("tfidfSimilarity.index")

    file = open("TopTenQueries.txt", "w") 
    for f in listdir(mypath):
     if isfile(join(mypath, f)):
        root=ET.parse('{}/{}'.format(mypath,f))
        xml=processXML(root) 
        query_doc=xml["document"]
        query_doc_bow=dictionary.doc2bow(process(query_doc))
        #print(query_doc_bow)
        #print(tfidf[query_doc_bow])
        sims=index[tfidf[query_doc_bow]]
        listSims=list((enumerate(sims)))
        sortSims=sorted(listSims,key=lambda pair: pair[1],reverse=True)
        
        #imp="Para la query {} su top 10 (mayor a menor): ".format(xml["id"])
        imp="{}:".format(xml["id"])
        n=1
        for dat in sortSims:
            if(n==1):
                imp+="{}".format(idList[dat[0]])
            else:
                imp+=";{}".format(idList[dat[0]])            
            n+=1
        print(imp)
        file.write(imp+"\n")


def test_run():
    #Leer los archivos de la carperta ./doc para crear el vocabulario
    mypath='./doc'
    idList=[]
    docDict=[]
    #Lee todos los archivos de la carperta doc
    for f in listdir(mypath):
     if isfile(join(mypath, f)):
        root=ET.parse('{}/{}'.format(mypath,f))
        xml=processXML(root) 
        idList.append(xml["id"]) 
        docDict.append(process(xml["document"]))
    
    saveDic(docDict)
    corpus_memory=MyCorpus()

    #Guardar Corpus
    corpora.MmCorpus.serialize('corpus.mm',corpus_memory)
    #Cargar Corpus
    corpus=corpora.MmCorpus('corpus.mm')
    #Crear tfidf del corpus
    tfidf=models.TfidfModel(corpus)
    #Guardar tfidf
    tfidf.save("tfidfCorpus.mm")
    #guardar index Similarities
    matrixSimilarity() 
    #Ejecutar queries y ver similitudes
    queries(idList)
    
     

 
if __name__=="__main__":
    test_run()