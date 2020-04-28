from texto import Texto
from venta import  Venta
from excepcion import miError
import json

class App():

    def __init__(self):
        self.lista_diccionarios=[]
        self.lista_etiquetas=["Nombre","Numero de Tarjeta","Codigo de Verificacion","Tipo","Monto Venta","Descripcion"]

    def main(self):
        texto=Texto()
        texto.setTexto()
        self.convertir(texto.getTexto())
        self.archivar()

    def convertir(self,lista):
        for i in range(len(lista)):
            self.lista_diccionarios.append({})
            objeto=Venta(lista[i])
            objeto.setValores()
            a=0
            for j in range(len(lista[i])):
                self.lista_diccionarios[i].setdefault(self.lista_etiquetas[j],objeto.getValores()[j])
                if lista[i][j]=="":
                    a=1
            try:
                if(a==1):
                    raise miError
                else:
                    self.imprimir(i)
            except miError:
                print("\nError!!! Ocurrio un problema con la fuente de datos de la Operacion {}".format(i+1))

    
    def imprimir(self,i):
        print(self.lista_diccionarios[i], end="\n\n")
        
    def archivar(self):
        with open("archivo_original.json", "w") as file:
            json.dump(self.lista_diccionarios, file, indent=4)

if __name__ == "__main__":
    app=App()
    app.main()
