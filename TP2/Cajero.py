class billete():
   
    def __init__(self, denominacion, moneda_valor, representacion):
        self.denominacion = denominacion
        self.moneda_valor = moneda_valor
        self.representacion = representacion


class billete_100(billete):
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

class billete_200(billete):
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

class billete_500(billete):
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

class billete_1000(billete):
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

cien = billete_100(100,'pesos','$100')
doscientos = billete_200(200,'pesos','$200')
quinientos = billete_500(500,'pesos','$500')
mil = billete_1000(1000,'pesos','$1000')


class Cajero_automatico(billete_100, billete_200, billete_500, billete_1000 ):
    def __init__(self):
        self.lista=[cien,cien,cien,cien,cien,cien,cien,cien,cien,cien,doscientos,quinientos,mil]
        self.almacen=[]
        self.total = 0
        self.denominacion = []
        self.lista1 = []
        self.lista2 = []
        self.monto = 0
        self.cambio = 0

    def agregar_dinero(self):
        
        for i in self.lista:
            self.almacen.append(i)
        print(self.almacen)

    def contar_dinero(self):
            
            for item in self.lista:
                self.total += item.denominacion
            print("La cantidad de dinero disponible en el cajero es de :",self.total)
    
    def extraer_dinero(self):
        self.monto= int(input("Ingrese la cantidad de dinero que desea retirar :"))
        self.cambio= int(input("Ingrese el porcentaje que desea sacar en cambio: "))
    
        while self.monto > self.total or self.monto %100!=0 :
            print("No hay dinero suficiente o ingrese un numero multiplo de 100")
            self.monto= int(input("Ingrese la cantidad de dinero que desea retirar: "))
            self.cambio= int(input("Ingrese el porcentaje que desea sacar en cambio: "))
        
        for item in self.almacen:
            self.denominacion.append(item.denominacion)
            self.denominacion.sort()
            self.denominacion.reverse()
        
        for i in self.denominacion:
            
            
            self.lista1.append(i)
            s=sum(self.lista1)
            if s <= self.monto:
                self.lista2.append(i)
                suma=sum(self.lista2)
        r=self.monto-suma 
            
        self.lista2.append(r)
        self.lista2.sort()       
        self.lista2.reverse()
        
        for i in self.lista2:
            if i == 300: 
                self.lista2.remove(300)
                self.lista2.append(200)
                self.lista2.append(100)
            if i == 400:
                self.lista2.remove(400)
                self.lista2.append(200)
                self.lista2.append(200)
        print("su vuelto es", self.lista2)        

        billete_auxiliar.nuevo=r
        self.lista.append(billete_auxiliar)
        #print(self.lista)

        resta=self.total - self.monto
        print("Dinero disponible en el cajero: ", resta)

    def extraer_dinero_cambio(self):
        x = self.monto
        y = self.cambio
        porcentaje = y * x/100
        print(porcentaje)
        resta = self.monto - porcentaje
        print (resta)
        lista1 = []
        lista2= []
        lista3 = []
        cambio=[]
        self.denominacion.reverse()

        for i in self.denominacion:
            lista1.append(i)
            s=sum(lista1)
            if s <= round(porcentaje):
                cambio.append(i)
        print(cambio)

        self.denominacion.reverse()
        for i in self.denominacion:
            lista2.append(i)
            s=sum(lista2)
            if s <= resta:
                lista3.append(i)
        lista3.append(100)
        lista3.sort()
        lista3.reverse()
        print(lista3)

        


      


billete_auxiliar = Cajero_automatico()
c = Cajero_automatico()
c.agregar_dinero()
c.contar_dinero()
c.extraer_dinero()
c.extraer_dinero_cambio()