class Numero():

    def __init__(self):
        self.numero = 0
    
    def setNumero(self):
        while True:
            try:
                self.numero= int(input("Ingrese un numero positivo:  "))
                if self.numero<=0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nEl numero ingresado es invalido. Intente nuevamente")
        return self.numero

    def getNumero(self):
        return self.numero

    def calculo(self,limite):        
        self.impares=[]
        for i in range(0,limite+1):
            if(i%2!=0):
                self.impares.append(i)
        return self.impares

