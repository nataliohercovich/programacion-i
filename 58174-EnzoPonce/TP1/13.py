import random

class promedio():

    def __init__(self):
        self.lista = []
       
    def ingresar(self):
        self.lista = random.sample(range(100), 10)
        print("La lista contiene estos elementos: ", self.lista)
        suma = 0
        for elementos in self.lista:
            suma += elementos
            prom = suma / 10 
        print("Su promedio es: ", prom)

numero = promedio()
numero.ingresar()
