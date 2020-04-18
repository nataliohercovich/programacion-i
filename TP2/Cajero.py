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
        self.lista=[cien, doscientos, quinientos, mil]
        self.almacen=[]
        self.total = 0
        self.denominacion = []

    def agregar_dinero(self):
        
        for i in self.lista:
            self.almacen.append(i)
        print(self.almacen)

    def contar_dinero(self):
            
            for item in self.lista:
                self.total += item.denominacion
            print("La cantidad de dinero disponible en el cajero es de :",self.total)
    
    def extraer_dinero(self):
        monto= int(input("Ingrese la cantidad de dinero que desea retirar :"))
    
        while monto > self.total or monto %100!=0 :
            print("No hay dinero suficiente o ingrese un numero multiplo de 100")
            monto= int(input("Ingrese la cantidad de dinero que desea retirar: "))

        
        for item in self.almacen:
            self.denominacion.append(item.denominacion)
            self.denominacion.sort()
        

        suma=0
        lista=[]
        for i in self.denominacion:
            
            lista.append(i)
            s=sum(lista)
            
            if s == monto:
                lista.reverse()
                print(lista)


        resta=self.total - monto
        print("Dinero disponible en el cajero: ", resta)
      



c = Cajero_automatico()
c.agregar_dinero()
c.contar_dinero()
c.extraer_dinero()