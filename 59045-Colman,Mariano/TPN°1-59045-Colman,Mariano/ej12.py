import operator
import random

class Aleatorios():
    def __init__(self):
        self.azar = {1:None,2:None,3:None,4:None,5:None,6:None,7:None}
        self.ordenado = {}

    def randomice(self):
        for i in range (1,8):
            self.azar[i] = random.randint(1,10)

    def diccionarioAzar(self):
        for i in range(1, 8):
            if i == 7:
                print(str(self.azar[i])+ "\n")
            else:
                print(str(self.azar[i]) + ",", end=" ")


    def diccionarioOrdenado (self):
        self.ordenado = sorted(self.azar.items(), key=operator.itemgetter(1), reverse=True)
        for numero in range (0,7):
            new = self.ordenado[numero][1]
            if numero == 6:
                print(str(new)+ "\n")
            else:
                print(str(new)+ ",", end=" ")



def main():
    aleatorios = Aleatorios()
    aleatorios.randomice()
    aleatorios.diccionarioAzar()
    aleatorios.diccionarioOrdenado()
main()
