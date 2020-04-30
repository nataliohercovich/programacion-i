from Cajero import billete,billete_100,billete_200,billete_500,billete_1000


class Cajero_automatico(billete_100, billete_200, billete_500, billete_1000 ):
    def __init__(self):
        self.lista=[]
        self.almacen=[]
        self.total = 0
        self.denominacion = []
        self.lista1 = []
        self.lista2 = []
        self.monto = 0
        self.cambio = 0
        self.lista3 = []
        self.lista4 = []
        self.r = 0
        self.completo = []
        self.muestra = ""

    def agregar_dinero(self, lista):
        for i in lista:
            self.almacen.append(i)
        for item in self.almacen:
                self.total += item.denominacion
                self.denominacion.append(item.denominacion)
    def contar_dinero(self):
            
            self.denominacion.sort()
            self.denominacion.reverse() 
            billete1=str(self.denominacion).count('100')
            billete2=str(self.denominacion).count('200')
            billete3=str(self.denominacion).count('500')
            billete4=str(self.denominacion).count('1000')


            for i in self.denominacion:
                if i==1000 and billete4 != 0:
                    self.muestra += "\nbilletes de $1000: {}".format(billete4)
                    billete4=0
                if i==500 and billete3 != 0:
                    self.muestra += "\nbilletes de $500: {}".format(billete3)
                    billete3=0
                if i==200 and billete2 != 0:
                    self.muestra += "\nbilletes de $200: {}".format(billete2)
                    billete2=0
                if i==100 and billete1 != 0:
                    self.muestra += "\nbilletes de $100: {}".format(billete1)
                    billete1=0
            self.muestra += "\nLa cantidad de dinero disponible en el cajero es de: ${}".format(self.total)               
            return self.muestra 
       
             
    def extraer_dinero(self, monto, cambio):
        self.monto= monto
        self.cambio= cambio
    
        while self.monto > self.total:
            return("Error.Debe retirar un monto menor al que hay en el cajero")
        while self.monto %100!=0:
            return("Error.El monto es incorrecto")
        while self.cambio > 100:
            return("Error.El porcentaje no debe ser mayor al 100%")
        
        self.resto=self.total - self.monto
            
        x = self.monto
        y = self.cambio
        self.porcentaje = y * x/100
        round(self.porcentaje)

        self.resta = self.monto - self.porcentaje
        self.r = self.resta

        self.denominacion.sort()
        self.denominacion.reverse()
        for i in self.denominacion:
            if self.resta / i >= 1:
                self.resta -= i
                self.lista2.append(i)
        while sum(self.lista2) < self.r:
            return "Error. No hay una combinación de billetes que nos permita extraer ese monto"


        print("Usted quiere retirar: ${}\n".format(self.monto))
        billete4=str(self.lista2).count('1000')
        billete3=str(self.lista2).count('500')
        billete2=str(self.lista2).count('200')
        billete1=str(self.lista2).count('100')
        
        muestra=''
        
        for i in self.lista2:
            if i==1000 and billete4 != 0:
                muestra += "{} billetes de $1000\n".format(billete4)
                billete4=0
            if i==500 and billete3 != 0:
                muestra += "{} billetes de $500\n".format(billete3)
                billete3=0
            if i==200 and billete2 != 0:
                muestra += "{} billetes de $200\n".format(billete2)
                billete2=0
            if i==100 and billete1 != 0:
                muestra += "{} billetes de $100\n".format(billete1)
                billete1=0
                     
        return muestra    
  
    def extraer_dinero_cambio(self):
        self.function = self.porcentaje + self.resta

       
        self.denominacion.reverse()
        for i in self.denominacion:
            if self.function / i >= 1:
                self.function -= i
                self.lista3.append(i)

        for i in self.lista2:
            self.lista3.append(i)
        
        billete4=str(self.lista3).count('1000')
        billete3=str(self.lista3).count('500')
        billete2=str(self.lista3).count('200')
        billete1=str(self.lista3).count('100')
        
        muestra=''
        
        for i in self.lista3:
            if i==1000 and billete4 != 0:
                muestra += "{} billetes de $1000\n".format(billete4)
                billete4=0
            if i==500 and billete3 != 0:
                muestra += "{} billetes de $500\n".format(billete3)
                billete3=0
            if i==200 and billete2 != 0:
                muestra += "{} billetes de $200\n".format(billete2)
                billete2=0
            if i==100 and billete1 != 0:
                muestra += "{} billetes de $100\n".format(billete1-billete4)
                billete1=0
                     
        return muestra         

        
    def imprimir(self):
        print("\nstock:\n", self.muestra)
        print("\nEl monto del dinero en cambio es:\n", self.porcentaje)
        print ("\nEl resto del dinero solicitado es:\n",self.r)
        print("\nLos billetes en cambio son:", self.lista3)
        #print("\nEl resto de billetes son:", self.lista4)
        print("\nDinero restante en el cajero:\n", self.resto)

