import time
import math
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
        self.cambio = 0
        self.montoo = 0


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
        return self.billetes_100, self.total_billetes_100, self.billetes_200, self.total_billetes_200, self.billetes_500, self.total_billetes_500, self.billetes_1000, self.total_billetes_1000, self.dinero_disponible

        #return self.dinero_disponible
    
    def extraer_dinero(self, monto):

        #pswd = int(input("Por favor ingrese su clave: "))
        pswd = 1234
        #print("Verificando, por favor espere")
        time.sleep(1)
        if pswd != 1234:
            while pswd != 1234:
                print("Clave incorecta")
                pswd = int(input("Por favor ingrese su clave: "))
                print("Verificando, por favor espere")
                time.sleep(1)
        #else:
            #print("\nIngresando...")
            #print("Bienvenido al ATM")
            #time.sleep(1)

        #print(f"""\nDinero disponible en la cuenta: $ {self.dinero_disponible}\n""")
        #monto = int(input("Por favor ingrese el monto a extraer: $ "))
        monto = 10000
        self.montoo = monto
        #cambio = 10
        #self.cambio = 10
        #self.cambio = int(input("Por favor ingrese el cambio con cambio a extraer: $ "))
        self.cambio = 10
        while monto <= 0 or monto % 100 != 0:
            #print("Solo se pueden extraer montos multiplos de 100\n")
            #monto = int(input("Por favor ingrese el monto a extraer: $ "))
            return 'Monto no valido'
        extraidos = []
        #copia_monto2 = monto

       
        #verifico que no quiera extraer mas de lo que tiene
        if self.dinero_disponible >= monto:

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 100:
                monto = monto - 100

                #saco un billete de ese monto
                self.billetes_100 -= 1

                for billete in self.almacen:

                    if billete.valor == 100:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 200:
                monto = monto - 200

                #saco un billete de ese monto
                self.billetes_200 -= 1

                for billete in self.almacen:

                    if billete.valor == 200:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 500:
                monto = monto - 500

                #saco un billete de ese monto
                self.billetes_500 -= 1

                for billete in self.almacen:

                    if billete.valor == 500:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 1000:
                monto = monto - 1000

                #saco un billete de ese monto
                self.billetes_1000 -= 1

                for billete in self.almacen:

                    if billete.valor == 1000:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break


            print("\nExtrayendo dinero...")
            time.sleep(2)
            return self.montoo
            #print(extraidos)
            #print(f"""\nTOTAL EXTRAIDO: $ {copia_monto2}""")
            #nuevo_balance = self.dinero_disponible - copia_monto2
            #print(f"""\nNuevo balance de cuenta: $ {nuevo_balance}""")

        else:
            #print("Fondos insuficientes")
            return 'Fondos insuficientes'
    
        #return extraidos
        
    def extraer_dinero_cambio(self):
        cambio = self.cambio
        porcentaje = self.montoo * (cambio / 100)
        copia_monto = self.montoo
        nuevo_balance = self.dinero_disponible - copia_monto
        porcentaje_redondo = math.ceil(porcentaje)
        cont_100 = 0
        cont_200 = 0
        cont_500 = 0
        cont_1000 = 0


        for billete in self.almacen:

            while porcentaje_redondo != 0:

                if self.total_billetes_100 >= porcentaje_redondo:
                        #extraidos.append(billete)
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 100
                        cont_100 += 1
                        break
                
                elif self.total_billetes_200 >= porcentaje_redondo:
                        #extraidos.append(billete)
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 200
                        cont_200 += 1
                        break
                
                elif self.total_billetes_500 >= porcentaje_redondo:
                        #extraidos.append(billete)
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 500
                        cont_500 += 1
                        break
                
                elif self.total_billetes_1000 >= porcentaje_redondo:
                        #extraidos.append(billete)
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 1000
                        cont_1000 += 1
                        break
                else:
                    print("ERROR")
        #totalitario = cont_100 * 100 + cont_200 * 200 + cont_500 * 500 + cont_1000 * 1000
        #resto_extraer = copia_monto - totalitario            
        print(f"""\nExtrayendo $ {copia_monto}, de los cuales  {cont_100} billetes son de 100""")
        print(f"""\n\t\t\t\t   {cont_200} billetes son de 200""")
        #print(f"""\n\t\t\t\t  {cont_500} billetes son de 500""")
        print(f"""\nNuevo balance de cuenta: $ {nuevo_balance}""")
        return copia_monto


atm = Cajero_Automatico()
atm.agregar_billetes(money)
atm.contar_billetes()
#atm.extraer_dinero_cambio()
atm.extraer_dinero(1)
atm.extraer_dinero_cambio()
