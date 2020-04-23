from billetes import Billete_100,Billete_1000,Billete_200,Billete_500

class Cajero():
    
    def __init__(self):

        self.total = 0
        self.lista_billetes = []
       
        self.cant_b100 = 0
        self.cant_b200 = 0
        self.cant_b500 = 0
        self.cant_b1000 = 0

        self.suma_100 = 0
        self.suma_200 = 0
        self.suma_500 = 0
        self.suma_1000 = 0

    
    
    def agregar_billetes(self,lista):

        for billete in lista:
            self.lista_billetes.append(billete)

    def contar(self):

        cant_b100 = 0
        cant_b200 = 0
        cant_b500 = 0
        cant_b1000 = 0

        for billete in self.lista_billetes:

            if billete.valor == 100:
                cant_b100 +=1
                
            if billete.valor == 200:
                cant_b200 +=1
               
            if billete.valor == 500:
                cant_b500 +=1
                
            if billete.valor == 1000:
                cant_b1000 +=1

       
             
        self.cant_b100 = cant_b100
        self.cant_b200 = cant_b200
        self.cant_b500 = cant_b500
        self.cant_b1000 = cant_b1000

        self.suma_100 = cant_b100 * 100
        self.suma_200 = cant_b200 *200
        self.suma_500 = cant_b500 *500
        self.suma_1000 = cant_b1000 *1000

        self.total = self.suma_100 + self.suma_200 + self.suma_500 + self.suma_1000
      

        return self.cant_b100,self.suma_100,self.cant_b200,self.suma_200,self.cant_b500,self.suma_500,self.cant_b1000,self.suma_1000, self.total

    
    def extraer_dinero(self,monto):

        lista_extraidos = []

        if monto%100 ==0:

            if self.total > monto :

                while self.cant_b1000 > 0 and monto >= 1000:
                    monto = monto - 1000

                    self.cant_b1000 -= 1

                    for billete in self.lista_billetes:
                        if billete.valor == 1000:
                            lista_extraidos.append(billete)
                            self.lista_billetes.remove(billete)
                            break

                while self.cant_b500 > 0 and monto >= 500:
                    monto = monto - 500

                    self.cant_b500 -= 1

                    for billete in self.lista_billetes:
                        if billete.valor == 500:
                            lista_extraidos.append(billete)
                            self.lista_billetes.remove(billete)
                            break

                while self.cant_b200 > 0 and monto >= 200:
                    monto = monto - 200

                    self.cant_b200 -= 1

                    for billete in self.lista_billetes:
                        if billete.valor == 200:
                            lista_extraidos.append(billete)
                            self.lista_billetes.remove(billete)
                            break

                while self.cant_b100 > 0 and monto >= 100:
                    monto = monto - 100

                    self.cant_b100 -= 1

                    for billete in self.lista_billetes:
                        if billete.valor == 100:
                            lista_extraidos.append(billete)
                            self.lista_billetes.remove(billete)
                            break

                print("Billetes extraidos : ")

                for i in lista_extraidos:
                    print(i.representacion)

                print("No se pudo entregar por falta de cambio: $" , monto)

            else:
                print("No hay dinero suficiente en el cajero")

        else:
            print("Solo puede ingresar multiplos de 100")
       

""" pruebas
a = Billete_500()
b = Billete_500()
c = Billete_100()
d = Billete_1000()
e = Billete_500()
f = Billete_1000()
j = Billete_200()

lista = [a,b,d,e,f]


cajero = Cajero()

cajero.agregar_billetes(lista)

print(cajero.contar())

lista2 = [d]

cajero.agregar_billetes(lista2)

print(cajero.contar())

lista3 = [j]

cajero.agregar_billetes(lista3)

print(cajero.contar())

cajero.extraer_dinero(1700)

print(cajero.contar()) 

"""
