import json
import os

class ErrorDataInvalida(Exception):
    pass

class Venta:
    def __init__(self,archivo):
        self.archivo = archivo 
        self.dic = {}


    def read_line(self):
        i = 1
        for line in self.archivo.readlines():
            try:
                lista = line.replace("\n", "").split(", ")
                if "" in lista:
                    raise ErrorDataInvalida
                ventas = {"nombre": lista[0],
                    "monto": lista[1],
                    "descripcion": lista[2],
                    "formapago": lista[3].replace("\n", "")}
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


