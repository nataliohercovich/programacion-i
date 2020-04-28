from texto import Texto
from excepcion import miError
import json

class App():

    def __init__(self):
        self.lista_diccionarios=[]
        self.lista_etiquetas=["Nombre","Monto","Descripcion","Forma de pago"]

    def main(self):
        texto=Texto()
        texto.setTexto()
        self.convertir(texto.getTexto())
        self.archivar()

    def convertir(self,lista):
        for i in range(len(lista)):
            a=0 
            self.lista_diccionarios.append({})
            for j in range(len(lista[i])):
                self.lista_diccionarios[i].setdefault(self.lista_etiquetas[j],lista[i][j])
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
