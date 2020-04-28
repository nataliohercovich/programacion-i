class Numero():

    def __init__(self):
        self.numero = 0
    
    def setNumero(self):
        while True:
            try:
                self.numero=int(input("\nIngrese un entero mayor a cero: "))
                if self.numero<=0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nEl numero ingresado es invalido. Intente nuevamente")
        return self.numero
    
    def getNumero(self):
        return self.numero