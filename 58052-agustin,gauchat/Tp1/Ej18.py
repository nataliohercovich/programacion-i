import os
import json

class APP(object):

    def __init__(self):
        self.txt = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej18.txt"
        self.json = '/home/agus/Escritorio/ventas.json'
        self.etiq = ["nombre", "monto", "descripcion", "formadepago"]
    
    def crear_archivo(self):
            dic = {}

            with open(self.txt, "r") as l:
                with open(self.json, 'w') as file:
                    for i in l:
                        i = i.split(", ")
                        for j in range(0, 4):
                            if i[j].find("\n") != -1:
                                i[j] = i[j].rstrip("\n")
                            if i[j] == "":
                                raise Exception("Problema con la fuente de datos")
                            dic.update({self.etiq[j]: i[j]})
                        json.dump(dic, file)
                        file.write("\n")

                        

def main():
    app = APP()
    app.crear_archivo()
main()