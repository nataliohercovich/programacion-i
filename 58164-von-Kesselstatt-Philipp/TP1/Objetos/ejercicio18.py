import json


class EmptyValue(Exception):
    pass


class LectorDeVentas():
    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio18.py", "")
        self.texto = open(self.path + self.archivo).read()

    def listToDict(self, lista):

        if "" in lista:
            raise EmptyValue()

        result = {
                  "nombre": lista[0],
                  "monto": int(lista[1]),
                  "descripcion": lista[2],
                  "forma de pago": lista[3]
                  }
        return result

    def convertToJSON(self):
        self.archivoJSON = self.archivo[:self.archivo.find(".")] + ".json"

        textoLista = self.texto.split("\n")[:-1]
        self.lista = [self.listToDict(item.split(", ")) for item in textoLista]

        self.JSON = open(self.path + self.archivoJSON, "w")
        json.dump(self.lista, self.JSON, indent=4)
        self.JSON.close()


"""
archivo = "txt.txt"
ejercicio18 = LectorDeVentas(archivo)

ejercicio18.convertToJSON()
"""
"""
import os
os.system("cat " + ejercicio18.path + "txt.json")
"""
