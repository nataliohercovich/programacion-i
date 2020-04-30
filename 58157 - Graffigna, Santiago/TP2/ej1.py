import time
from plata import money
from billetes import Billete_100, Billete_1000, Billete_200, Billete_500

class Cajero_Automatico():
    
    def __init__(self):

        self.billetes_100 = 0
        self.billetes_200 = 0
        self.billetes_500 = 0
        self.billetes_1000 = 0
        self.total_100 = 0
        self.total_200 = 0
        self.total_500 = 0
        self.total_1000 = 0
        self.dinero_disponible = 0
        self.almacen = []

    
    
    def agregar_billetes(self, mas_billetes):

        for billete in mas_billetes:
            self.almacen.append(billete)


    def contar_billetes(self):

        #la cuenta en si
        for billete in self.almacen:

            if billete.valor == 100:
                self.billetes_100 += 1
            if billete.valor == 200:
                self.billetes_200 += 1
            if billete.valor == 500:
                self.billetes_500 += 1 
            if billete.valor == 1000:
                self.billetes_1000 += 1

        #cantidad de billetes por su valor
        self.total_billetes_100 = self.billetes_100 * 100
        self.total_billetes_200 = self.billetes_200 * 200
        self.total_billetes_500 = self.billetes_500 * 500
        self.total_billetes_1000 = self.billetes_1000 * 1000

        #total de plata en la cuenta
        self.dinero_disponible = self.total_billetes_100 + self.total_billetes_200 + self.total_billetes_500 + self.total_billetes_1000

    
    def extraer_dinero(self, monto):

        pswd = int(input("Por favor ingrese su clave: "))
        print("Verificando, por favor espere")
        time.sleep(1)
        if pswd != 1234:
            while pswd != 1234:
                print("Clave incorecta")
                pswd = int(input("Por favor ingrese su clave: "))
                print("Verificando, por favor espere")
                time.sleep(1)
        else:
            print("Ingresando...")
            print("Bienvenido al ATM")
            time.sleep(1)

        print(f"""\nDinero disponible en la cuenta: $ {self.dinero_disponible}\n""")
        monto = int(input('Por favor ingrese el monto a extraer: $ '))
        while monto <= 0 or monto % 100 != 0:
            print("Solo se pueden extraer montos multiplos de 100\n")
            monto = int(input('Por favor ingrese el monto a extraer: $ '))
        copia_monto2 = monto

       
        #verifico que no quiera extraer mas de lo que tiene
        if self.dinero_disponible > monto:

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 100:
                monto = monto - 100

                #saco un billete de ese monto
                self.billetes_100 -= 1


            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 200:
                monto = monto - 200

                #saco un billete de ese monto
                self.billetes_200 -= 1


            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 500:
                monto = monto - 500

                #saco un billete de ese monto
                self.billetes_500 -= 1



            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 1000:
                monto = monto - 1000

                #saco un billete de ese monto
                self.billetes_1000 -= 1


            print("Extrayendo dinero...")
            time.sleep(2)
            print(f"""\nTOTAL EXTRAIDO: $ {copia_monto2}""")
            nuevo_balance = self.dinero_disponible - copia_monto2
            print(f"""\nNuevo balance de cuenta: $ {nuevo_balance}""")

        else:
            print("Fondos insuficientes")

        
atm = Cajero_Automatico()
atm.agregar_billetes(money)
atm.contar_billetes()
atm.extraer_dinero(1)
