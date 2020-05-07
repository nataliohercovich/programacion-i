import json
import os

class ErrorDataInvalida(Exception):
    pass

class TarjetaCredito:
    def __init__(self, nombre, ncard, codver, tipo):
        self.nombre = nombre
        self.ncard = ncard
        self.codver = codver
        self.tipo = tipo
    
    def getNombre(self):
        return self.nombre
    def getNcard(self):
        return self.ncard
    def getCodver(self):
        return self.codver
    def getTipo(self):
        return self.tipo

class Venta:
    def __init__(self,archivo):
        self.archivo = archivo 
        self.dic = {}

    def getMonto(self):
        return self.monto
    def setMonto(self, monto):
        self.monto = monto
    
    def getDescripcion(self):
        return self.desc
    def setDescripcion(self, desc):
        self.desc = desc


    def read_line(self):
        i = 1
        for line in self.archivo.readlines():
            try:
                lista = line.replace("\n", "").split(", ")
                if "" in lista:
                    raise ErrorDataInvalida
                tarjeta = TarjetaCredito (lista[0], lista[1],
                        lista[2], lista[3])
                self.setMonto(lista[4])
                self.setDescripcion(lista[5].replace('\n', ''))
                ventas = {"Nombre y Apellido": tarjeta.getNombre(),
                               "Numeor de Tarjeta de "
                               "Credito": tarjeta.getNcard(),
                               "Codigo de verificacion": tarjeta.getCodver(),
                               "Tipo de tarjeta de credito": tarjeta.getTipo(),
                               "Monto de la venta": self.getMonto(),
                               "Descripcion de la venta": self.getDescripcion()}
                self.dic["venta numero " + str(i)] = ventas
                i += 1
            except ErrorDataInvalida:
                print("\n\nOcurrió un problema con la fuente de datos\n\n")
                continue
        return self.dic
        


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    nombre = input("Ingrese el nombre del archivo:\n")
    print("\nLas ventas producidas son:\n")
    archivo = open(path + "/" + nombre + ".txt", "r")
    info = Venta(archivo)
    dic = info.read_line()
    for key in dic:
        print(key, "\n")
        print(dic[key], "\n")
    doc_json = open(path + "/ARCHIVO_ORIGINAL.json", "w")
    json.dump(dic, doc_json, indent=4)
    archivo.close()
    doc_json.close()



if __name__ == "__main__":
    main()


