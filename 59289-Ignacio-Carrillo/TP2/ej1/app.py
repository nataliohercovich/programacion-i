import os
from cajero_automatico import Cajero_automatico
from billete import Billete,Billete_100,Billete_200,Billete_500,Billete_1000

class Api():

    def __init__(self):
        self.cajero=Cajero_automatico()
        self.lista_billetes=[]

    def ejecutar(self):
        os.system("clear clc")
        print("CAJERO AUTOMATICO")
        flag=True
        while flag==True:
            menu=self.menu()
            if(menu==1):
                os.system("clear clc")
                self.reconocer_billetes()
            elif(menu==2):
                os.system("clear clc")
                print("\nVaciando cajero...")
                self.cajero.vaciar_cajero()
            elif(menu==3):
                os.system("clear clc")
                while True:
                    try:
                        monto=int(input("\nIngrese el monto a extraer: "))
                        if(monto%100!=0):
                            raise ValueError
                        else:
                            entrega=self.cajero.extraer_dinero(monto)
                            total=0
                            if(len(entrega)>0):
                                print("\nBilletes entregados: ")
                            for i in range(len(entrega)):
                                print(entrega[i].denominacion)
                                total+=entrega[i].denominacion
                            print("\nTotal entregado: ${}".format(total))
                            break
                    except ValueError:
                        print("\n**ERROR**Debe extraer un multiplo de 100")
            elif(menu==4):
                os.system("clear clc")
                self.cajero.contar_dinero("print")
            else:
                os.system("clear clc")
                print("\nCerrando Sesion...")
                flag=False
        print()
         
    def cargar_cajero(self):
        # while True:
        #     try:
        #         eleccion=input("""
        #         Desea cargar un nuevo billete: Y/N: """)
        #         eleccion=eleccion.upper()
        #         if(eleccion=='Y'):
        #             self.reconocer_billetes()
        #         elif(eleccion=='N'):
        #             if(len(self.lista_billetes)>0):
        #                 self.cajero.agregar_dinero(self.lista_billetes)
        #             break
        #         else:
        #             raise ValueError
        #     except ValueError:
        #         os.system("clear clc")
        #         print("\n***ERROR*** Introduzca una opcion válida")
        if(len(self.lista_billetes)>0):
            self.cajero.agregar_dinero(self.lista_billetes)
        else:
            print("\n**Error al llenar cajero** No se ha ingresado dinero")

    def reconocer_billetes(self):
        # while True:
        #     try:
        #         eleccion=int(input("""
        #         Ingrese el tipo de moneda:
        #         1- Pesos
        #         2- Dolares
        #         3- Reales
                                    
        #         Eleccion: """))
        #         if(eleccion==1):
        #             tipo="Pesos"
        #             break
        #         elif(eleccion==2):
        #             tipo="Dolares"
        #             break
        #         elif(eleccion==3):
        #             tipo="Reales"
        #             break
        #         else:
        #             raise ValueError
        #     except ValueError:
        #         print("\n***ERROR*** Introduzca una opcion válida")
        
        tipo="Pesos"
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 100: """))
        for i in range(eleccion):
            billete=Billete_100(100,tipo)
            self.lista_billetes.append(billete)
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 200: """))
        for i in range(eleccion):
            billete=Billete_200(200,tipo)
            self.lista_billetes.append(billete)
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 500: """))
        for i in range(eleccion):
            billete=Billete_500(500,tipo)
            self.lista_billetes.append(billete)
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 1000: """))
        for i in range(eleccion):
            billete=Billete_1000(1000,tipo)
            self.lista_billetes.append(billete)
        
        self.cargar_cajero()

    def menu(self):
        while True:
            try:
                eleccion=int(input("""
                Ingrese que desea hacer:
                1- Cargar cajero
                2- Vaciar cajero
                3- Extraer dinero
                4- Contar dinero cajero
                0- Salir
                                    
                Eleccion: """))
                if(eleccion!=1 and eleccion!=2 and eleccion!=3 and eleccion!=4 and eleccion!=0):
                    raise ValueError
                else:
                    break
            except ValueError:
                os.system("clear clc")
                print("\n***ERROR*** Introduzca una opcion válida")
            
        return eleccion

if __name__ == "__main__":
    api = Api()  
    api.ejecutar()