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
    
    def calcular_impares(self,limite):        
        self.impares=[]     
        for i in range(limite):
            j=0
            k=0
            self.impares.append([])
            while k<=i:
                if(j%2!=0):
                    self.impares[i].append(int(j))
                    k+=1
                j+=1    
        return self.impares

