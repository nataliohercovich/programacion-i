import os

class APP(object):

    def __init__(self):
        self.txt = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej18.txt"
        self.json = '/home/agus/Escritorio/ARCHIVO_ORIGINAL.json'

    def controlador(self, vacio):
        a = vacio.split()
        for elemento in a:
            for letra in elemento:
                if letra == ":":
                    if elemento[elemento.index(letra) + 1] == ",":
                        return False
    
    def crear_archivo(self):

        with open(self.txt, "r") as l:

            with open(self.json, 'w') as file:
                x = False
                k = False

                for i in l:

                    y = ""
                    i.replace(" ", "\"")
                    for j in i:
                        if j == ":":
                            x = True
                        if j == "," or j == ".":
                            x = False
                        if x == True and j != ":":
                            j = "x"
                        
                        y += j
 
                    z = y.split(", ")
                    n = z[0].split(":")
                    m  = z[1].split(":")
                    d = z[2].split(":")
                    f = z[3].split(":")
                    f[0] = f[0].replace(" ", "")
                    f[1] = f[1].replace(".", "")
                    f[1] = f[1].replace("\n", "")                        
                    a = n[0].lower() + "\":" + "\"" + n[1].lower() + "\"" + ",\"" + m[0].lower() + "\":" + "\"" + m[1].lower() + "\"" + ",\"" + d[0].lower() + "\":" + "\"" + d[1].lower() + "\"" + ",\"" + f[0].lower() + "\":" + "\"" + f[1].lower()

                    if self.controlador(y) == False: 
                        file.write("Error con la fuente de datos" + "\n")
                    else:
                        a = "{\"" + a + "}\""
                        file.write(a + "\n")
                        

def main():
    app = APP()
    app.crear_archivo()
main()