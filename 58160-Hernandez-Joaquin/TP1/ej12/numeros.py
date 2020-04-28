from random import randint

class Numeros():

    def __init__(self):
        self.numeros=0
        self.diccionario={}
    
    def setGenerar_numeros(self):
        repeticiones=randint(0,20)
        for i in range(repeticiones):
            self.numeros=randint(0,10)
            self.diccionario.setdefault(str(i),self.numeros)
        
    def getGenerar_numeros(self):
        return self.diccionario
  
   
    