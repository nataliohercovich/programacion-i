from random import randint 

class Numeros():

    def __init__(self):
        self.numeros=0
        self.lista=[]
            
    def setGenerarNumeros(self):
        for i in range(0,10):
            self.numeros=randint(0,20)
            self.lista.append(self.numeros)
    
    def getGenerarNumeros(self):
        return self.lista
