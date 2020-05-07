class ordenamiento():

    def __init__(self):
        self.numero = 0
    
    def ingresar(self):
        self.numero = int(input("Introduce un número entero positivo: "))

    def calculo(self):
        for i in range(1, self.numero, 2):
            if self.numero > 0:
                print (i)

impares = ordenamiento()
impares.ingresar()
impares.calculo()