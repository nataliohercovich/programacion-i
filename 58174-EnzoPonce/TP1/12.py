import random

class aleatoria():

    def __init__(self):
        self.lista = []
        

    def valores(self):
        self.lista = random.sample(range(10), 10)
        print("Lista original: ", self.lista)
        for i in range(1, len(self.lista)):
            for j in range(0, len(self.lista) - i):
                if self.lista[j] > self.lista[j + 1]:
                    temp = self.lista[j]
                    self.lista[j] = self.lista[j + 1]
                    self.lista[j + 1] = temp
        print ("\nLista ordenada: ", self.lista)




valor = aleatoria()
valor.valores()
