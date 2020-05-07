from io import open

class lectura():
    
    def leer(self):
        archivo = open("15.txt", "r")
        texto = archivo.read()
        archivo.close()
        print(texto)

tex = lectura()
tex.leer()

