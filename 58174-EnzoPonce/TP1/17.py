from io import open

class intercambio():

    def leer(self):
        self.fichero = open('15.txt','r')
        self.lineas = self.fichero.readlines()
        self.filas = self.texto.split("\n") 
        #fichero.close()

    def convertir(self):
        self.datos= {}
        self.datos['ventas'] = []

        for linea in self.lineas:
            r = linea.replace("\n", "").split(";")  
            self.datos['ventas'].append = ({"nombre":r[0], "monto":r[1], "descripcion":r[2], "forma de pago":r[3]})
           

        


t = intercambio()
t.leer()
t.convertir()