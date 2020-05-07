import json
import os

class Venta:
    def __init__(self,archivo):
        self.archivo = archivo 
        self.lista = []
        self.dic = {}
        self.ventas = {}

    def read_line(self):
        i = 1
        for line in self.archivo.readlines():
            self.lista = line.split(",")
            self.ventas = {
               "nombre": str(self.lista[0]),
               "monto": str(self.lista[1]),
               "descripcion": str(self.lista[2]),
               "formapago": str(self.lista[3].replace("\n", ""))}
            self.dic["venta numero " + str(i)] = self.ventas
            i += 1
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