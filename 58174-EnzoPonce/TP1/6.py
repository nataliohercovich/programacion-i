class numero_primo():

    def __init__(self):
        self.entero = 0
        

    def ingresar(self):
        self.entero = int(input("Ingrese un numero entero mayor a 2: "))

    def calculo(self):
        if self.entero < 2 :
            return False
        i = 2
        while self.entero % i != 0:
            i += 1
        if i == self.entero:
            print(str(self.entero) + " es primo ")
        else:
            print(str(self.entero) + " es par ")

numero=numero_primo()
numero.ingresar()
numero.calculo()
