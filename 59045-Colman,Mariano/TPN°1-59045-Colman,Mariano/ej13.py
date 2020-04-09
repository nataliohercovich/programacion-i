import random

class Promedio():
    def __init__(self):
        self.l = []

    def randomice(self):
        for i in range (0,10):
            self.l.append(random.randint(1,100))

    def promedios(self):
        suma = 0.0
        for i in range(0,len(self.l)):
            suma=suma+self.l[i]
        return suma/len(self.l)

def main():
    promedio = Promedio()
    promedio.randomice()
    promedio.l
    print("Los numeros aleatorios son: %s" %promedio.l)
    print("El promedio es: %s" %promedio.promedios())
main()