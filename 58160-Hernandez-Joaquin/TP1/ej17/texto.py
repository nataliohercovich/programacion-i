class Texto():

    def __init__(self):
        self.lista=[]
        
    def setTexto(self):
        self.archivo=open("/home/joaquin/Progamacion1/um-programacion-i-2020/58160-Hernandez-Joaquin/Trabajo Practico 1/ej17/archivo_original","r")
        for linea in self.archivo.readlines():
            if linea!="" and linea!="\n":
                linea=linea.replace("\n","")
                self.lista.append(linea.split(", "))
    
    def getTexto(self):
        return self.lista
