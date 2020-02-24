import re
import array

def count_words(text):
	"""Cuenta cuantas veces una palabra occure en el texto"""
	counts = dict()  # diccionario de pares { <word>: <count> } 
	
	# Conversion a minuscula
	text2 = text.lower()
    
	
	# Dividir el texto en tokens (palabras), quitando la puntuacion.
	# Usar expresiones regulares para dividr segun caracteres no-alfanumericos '\w'
	matchObjs = re.findall(r'[\w]+', text2)
	print("Lenght {}".format(len(matchObjs)))  
	print(matchObjs)
	# Conteo usando el diccionario.
	for obj in matchObjs:
		if obj in counts:
			counts[obj] += 1 #Adiciona 1 a una entrada existente
		else:
			counts[obj] = 1 #Crea un nuevo indice/palabra en el diccionario.
	
	return counts

def count_words2(text,wordDict,nText):
	text2=text.lower()
	matchObjs=re.findall(r'[\w]+', text2)
	for obj in matchObjs:
		if obj in wordDict:
			#revisar Rango
			wordDict[obj][nText]+=1
		else:
			wordDict[obj]=dict()
			wordDict[obj][nText]=1
	
def createMatrix(nTotalText,wordDict):
	matrix=[]
	for i in range(nTotalText):
		row=[]
		for obj in wordDict:
			print(wordDict[obj],i)
			
			if i+1 in wordDict[obj]:
				row.append(wordDict[obj][i+1]  )
				print("esta y pues concateno y le saco lo que se necesite")
			else:
				row.append(0)
				print("lo lleno con cero xD")
		matrix.append(row)
	return matrix



def test_run():
	with open("input.txt", "r") as f:
		text = f.read()
		wordDict=dict()
		#Leo todos los libros, hago un diccionario --> "palabra1": [1,0,3] En donde la palabra 
		#se refiere a cualquier de los textos y la posición del array y número indica cuanto se repite
		#en aquel libro
		#
		nTotalText=3
		for i in range(nTotalText):
			print("")
			#Aquí llamo count_words2(textLeido,wordDict,i)
		count_words2(text,wordDict,1) 
		count_words2("Jhoan jhoan jhoan jhoan",wordDict,2)
		matrix=createMatrix(2,wordDict)
		print(matrix) 
	

if __name__ == "__main__":
	test_run()