from Billetes2 import Billete_1000,Billete_500,Billete_200,Billete_100
import math

class Atm:

    def __init__(self):
        self.billetes100 = []
        self.billetes200 = []
        self.billetes500 = []
        self.billetes1k = []
        self.total = 0

    def agregar_dinero(self, lista_de_billetes):
        for i in lista_de_billetes:
            if i.denom == 100:
                self.billetes100.append(i)
            elif i.denom == 200:
                self.billetes200.append(i)
            elif i.denom == 500:
                self.billetes500.append(i)
            else:
                self.billetes1k.append(i)

        
    def contar_dinero(self):
        billete =[len(self.billetes100), len(self.billetes200),
                    len(self.billetes500), len(self.billetes1k)]
        count_bills=[]
        for x in range(len(billete)):
            if x == 0:
                valor = 100
            if x == 1:
                valor = 200
            if x == 2:
                valor = 500
            if x == 3:
                valor = 1000
            string = (str(billete[x]), " billetes de $", str(valor))
            count_bills.append(string)
        self.total = (billete[0]*100 + billete[1]*200 + billete[2]*500 + billete[3]*1000)
        return(count_bills)
    
    def extraer_dinero(self, monto):
        disponible =[len(self.billetes1k), len(self.billetes500),
                    len(self.billetes200), len(self.billetes100)]
        '''if percentage < 100 or percentage > 0:
            percentage = math.trunc(monto * percentage / 100)
            monto = monto - percentage'''
        retiro = 0
        cant = 0
        i = 0
        if monto <= self.total:
            if monto % 100 == 0:
                cant = monto//1000
                if cant <= disponible[0]:
                    for i in range(cant):
                        disponible[0] -= 1
                    retiro = cant * 1000         
                    monto -= cant * 1000
                
                cant = monto//500           
                if cant <= disponible[1]:
                    i = 0
                    for i in range(cant):
                        disponible[1] -= 1
                    retiro += cant * 500
                    monto -= cant * 500
                
                cant = monto//200
                if cant <= disponible[2]:
                    i = 0
                    for i in range(cant):
                        disponible[2] -= 1
                    retiro += cant * 200
                    monto -= cant * 200
                
                cant = monto//100
                if cant <= disponible[3]:
                    i = 0
                    for i in range(cant):
                        disponible[3] -= 1
                    retiro += cant * 100
                print("Dinero extraidos ", retiro)       
            else:
                print("Monto no válido, ingrese un monto multiplo de 100")
        else:
            print("Monto no válido, ingrese un monto menor")

    def extraer_dinero_cambio(self, monto, percentage):
        disponible =[len(self.billetes1k), len(self.billetes500),
                    len(self.billetes200), len(self.billetes100)]
        monto_cambio = 0
        retiro = 0
        retirocam = 0
        if monto <= self.total:
            if percentage < 100 or percentage > 0:
                if monto % 100 == 0:
                    percentage = math.trunc(monto * percentage / 100)
                    while percentage % 100 != 0:
                        percentage += 10
                    monto_cambio = percentage
                    monto -= monto_cambio
                    cant = monto//1000
                    if cant <= disponible[0]:
                        for i in range(cant):
                            disponible[0] -= 1
                        retiro = cant * 1000         
                        monto -= cant * 1000
                    
                    cant = monto//500           
                    if cant <= disponible[1]:
                        i = 0
                        for i in range(cant):
                            disponible[1] -= 1
                        retiro += cant * 500
                        monto -= cant * 500
                    
                    cant = monto//200
                    if cant <= disponible[2]:
                        i = 0
                        for i in range(cant):
                            disponible[2] -= 1
                        retiro += cant * 200
                        monto -= cant * 200
                    
                    cant = monto//100
                    if cant <= disponible[3]:
                        i = 0
                        for i in range(cant):
                            disponible[3] -= 1
                        retiro += cant * 100
                    print("Dinero extraidos ", retiro)  

                    while monto_cambio != 0:
                        cant = monto_cambio//100
                        cant1 = cant
                        while cant1 != 0 or disponible[3] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[3] -= 1
                                cant1 -= 1
                            retirocam += cant * 100
                            monto_cambio -= cant * 100
                            break

                        cant = monto_cambio//200
                        cant1 = cant
                        while cant1 != 0 or disponible[2] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[2] -= 1
                                cant1 -= 1
                            retirocam += cant * 200
                            monto_cambio -= cant * 200
                            break
                        
                        cant = monto_cambio//500           
                        cant1 = cant
                        while cant1 != 0 or disponible[1] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[1] -= 1
                                cant1 -= 1
                            retirocam += cant * 500
                            monto_cambio -= cant * 500
                            break
                        
                        cant = monto_cambio//1000
                        cant1 = cant
                        while cant1 != 0 or disponible[0] != 0:
                            i=0
                            for i in range(cant):
                                disponible[0] -= 1
                                cant1 -= 1
                            retirocam += cant * 1000         
                            monto_cambio -= cant * 1000
                            break
                        break
                    print("Dinero extraidos con cambio", retirocam)
                else:
                    print("Monto no válido, ingrese un monto multiplo de 100")
            else:
                print("El porcentaje ingresado es incorrecto")
        else:
            print("Monto no válido, ingrese un monto menor")