from billete import Billete,Billete_100,Billete_200,Billete_500,Billete_1000
import copy

class Cajero_automatico():

    def __init__(self):
        self.almacen_interno={'100':[],'200':[],'500':[],'1000':[]}

    def agregar_dinero(self,lista_billetes):
        for i in range(len(lista_billetes)):
            self.almacen_interno[str(lista_billetes[i].denominacion)].append(lista_billetes[i])

    def vaciar_cajero(self):
        for key,lista in self.almacen_interno.items():
            lista.clear()

    def contar_dinero(self):
        contador_dinero=[]
        for key,lista in self.almacen_interno.items():
            aux=len(lista)*int(key)
            contador_dinero.append(aux)

        dinero_total=0
        for i in range(len(contador_dinero)):
            dinero_total+=contador_dinero[i]
        
        return contador_dinero,dinero_total

    def extraer_dinero_cambio(self,monto,porcentaje):
        cambio=int(round(monto*porcentaje/100,-2))
        parcial,dinero_total=self.contar_dinero()
        copia_seguridad=copy.deepcopy(self.almacen_interno)
        entrega_billete=[]
        entrega_cambio=[]
        if(dinero_total>=monto):
            while(cambio>0):
                if(len(self.almacen_interno['100'])>0):
                    billete=self.almacen_interno['100'].pop()
                    cambio-=billete.denominacion
                    entrega_cambio.append(billete)
                elif(len(self.almacen_interno['200'])>0):
                    billete=self.almacen_interno['200'].pop()
                    cambio-=billete.denominacion
                    entrega_cambio.append(billete)
                elif(len(self.almacen_interno['500'])>0):
                    billete=self.almacen_interno['500'].pop()
                    cambio-=billete.denominacion
                    entrega_cambio.append(billete)
                elif(len(self.almacen_interno['1000'])>0):
                    billete=self.almacen_interno['1000'].pop()
                    cambio-=billete.denominacion
                    entrega_cambio.append(billete)
            cambio_total=0
            for i in range(len(entrega_cambio)):
                cambio_total+=entrega_cambio[i].denominacion
            if(cambio_total>monto):
                print("**ERROR FATAL** ")
                self.almacen_interno=copy.deepcopy(copia_seguridad)
                return 1,1
            else:
                monto-=cambio_total
                while monto>0:
                    if(monto>=1000 and len(self.almacen_interno['1000'])>0):
                        billete=self.almacen_interno['1000'].pop()
                        monto-=billete.denominacion
                        entrega_billete.append(billete)
                    elif(monto>=500 and len(self.almacen_interno['500'])>0):
                        billete=self.almacen_interno['500'].pop()
                        monto-=billete.denominacion
                        entrega_billete.append(billete)
                    elif(monto>=200 and len(self.almacen_interno['200'])>0):
                        billete=self.almacen_interno['200'].pop()
                        monto-=billete.denominacion
                        entrega_billete.append(billete)
                    elif(monto>=100 and len(self.almacen_interno['100'])>0):
                        billete=self.almacen_interno['100'].pop()
                        monto-=billete.denominacion
                        entrega_billete.append(billete)
                    else:
                        print("\n**ERROR** No se pudo satisfacer la combinacion necesaria de billetes")
                        self.almacen_interno=copy.deepcopy(copia_seguridad)
                        return 1,1
        else:
            print("\n**ERROR** Cantidad de dinero insuficente en cajero")
            return 1,1
        
        return entrega_billete,entrega_cambio

