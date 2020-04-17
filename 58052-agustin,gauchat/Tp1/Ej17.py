import os
import json

class APP():

    def __init__(self):
        self.txt = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej15.txt"
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
                        dic.update({self.etiq[j]: i[j]})
                    json.dump(dic, file)
                    file.write("\n")

def main():
    app = APP()
    app.crear_archivo()
main()


# z = y.split(", ")
# n = z[0].split(":")
# m  = z[1].split(":")
# d = z[2].split(":")
# f = z[3].split(":")
# f[0] = f[0].replace(" ", "")
# f[1] = f[1].replace(".", "")
# f[1] = f[1].replace("\n", "")
# a = "{\"" + n[0].lower() + "\":" + "\"" + n[1].lower() + "\"" + ",\"" + m[0].lower() + "\":" + "\"" + m[1].lower() + "\"" + ",\"" + d[0].lower() + "\":" + "\"" + d[1].lower() + "\"" + ",\"" + f[0].lower() + "\":" + "\"" + f[1].lower() + "\"}"
