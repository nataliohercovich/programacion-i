from billete import Billete,Billete_100,Billete_200,Billete_500,Billete_1000

class Cajero_automatico():

    def __init__(self):
        self.almacen_interno={'100':[],'200':[],'500':[],'1000':[]}

    def extraer_dinero(self,monto):
        contador_dinero,dinero_total=self.contar_dinero("no imprimir")
        entrega_billete=[]
        if(dinero_total>=monto):
            while(monto!=0):
                if(monto>=1000 and len(self.almacen_interno['1000'])>0):
                    billete=self.almacen_interno['1000'].pop()
                    monto-=billete.denominacion
                    dinero_total-=billete.denominacion
                    entrega_billete.append(billete)
                elif(monto>=500 and len(self.almacen_interno['500'])>0):
                    billete=self.almacen_interno['500'].pop()
                    monto-=billete.denominacion
                    dinero_total-=billete.denominacion
                    entrega_billete.append(billete)
                elif(monto>=200 and len(self.almacen_interno['200'])>0):
                    billete=self.almacen_interno['200'].pop()
                    monto-=billete.denominacion
                    dinero_total-=billete.denominacion
                    entrega_billete.append(billete)
                elif(monto>=100 and len(self.almacen_interno['100'])>0):
                    billete=self.almacen_interno['100'].pop()
                    monto-=billete.denominacion
                    dinero_total-=billete.denominacion
                    entrega_billete.append(billete)
                else:
                    print("\nSe produjo un error")
                
        else:
            print("\n**ERROR**Cantidad de dinero insuficente en cajero")
        
        return entrega_billete

    def agregar_dinero(self,lista_billetes):
        for i in range(len(lista_billetes)):
            self.almacen_interno[str(lista_billetes[i].denominacion)].append(lista_billetes[i])

    def vaciar_cajero(self):
        for key,lista in self.almacen_interno.items():
            for j in range(len(lista)):
                lista.pop()

    def contar_dinero(self,a):
        print()
        contador_dinero=[]
        for key,lista in self.almacen_interno.items():
            aux=len(lista)*int(key)
            if a=="print":
                print("\nBilletes de ${}: {}*${}=${}".format(key,len(lista),key,str(aux)))
            contador_dinero.append(aux)

        dinero_total=0
        for i in range(len(contador_dinero)):
            dinero_total+=contador_dinero[i]
        if a=="print":
            print("\nCantidad total de dinero en cajero: ${}".format(dinero_total))
        
        return contador_dinero,dinero_total

