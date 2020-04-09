class triangulo():
    def __init__(self):
        self.numero = 1
        self.lista = []

    def ingresar(self):
        self.numero = int(input("Introduce la altura del triángulo (entero positivo): "))
    
    def calculo(self):
        for i in range(1, self.numero +1, 2):
            self.lista.append(i)
            self.lista.sort()
            self.lista.reverse()
            print(self.lista)


X = triangulo()
X.ingresar()
X.calculo()