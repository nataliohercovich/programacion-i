import random

class Numeros():
    def __init__(self):
        self.a = []

    def lista(self):
        for i in range(0, 10):
            self.a.append(random.randint(1, 10))

    def promediarLista(self):
        sum=0.0
        for i in range(0,len(self.a)):
            sum=sum+self.a[i]
    
        return sum/len(self.a)

def main():
    numeros = Numeros()
    numeros.lista()
    print("Lista: %s" % numeros.a)
    print("El promedio es: %s" % numeros.promediarLista())
main()