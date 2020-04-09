class triangulo():

    def __init__(self):
        self.numero = []

    def ingresar(self):
        self.numero = int(input("Introduce la altura del triángulo (entero positivo): "))
    
    def calculo(self):
        for i in range(self.numero):
            print("*"*(i+1))

X = triangulo()
X.ingresar()
X.calculo()

