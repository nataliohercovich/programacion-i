from texto import Texto
import json

class App():

    def __init__(self):
        self.lista_diccionarios=[]
        self.lista_etiquetas=["Nombre","Monto","Descripcion","Forma de pago"]

    def main(self):
        texto=Texto()
        texto.setTexto()
        self.convertir(texto.getTexto())
        self.imprimir()
        self.archivar()

    def convertir(self,lista):
        for i in range(len(lista)):
            self.lista_diccionarios.append({})
            for j in range(len(lista[i])):
                self.lista_diccionarios[i].setdefault(self.lista_etiquetas[j],lista[i][j])
    

    def imprimir(self):
        for i in range(len(self.lista_diccionarios)):
            print(self.lista_diccionarios[i], end="\n")
        print()

    def archivar(self):
        with open("archivo_original.json", "w") as file:
            json.dump(self.lista_diccionarios, file, indent=4)

if __name__ == "__main__":
    app=App()
    app.main()
