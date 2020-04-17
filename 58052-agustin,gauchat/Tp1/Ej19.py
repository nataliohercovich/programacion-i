import json
class TarjetaCredito():
    def __init__(self):
        self.nombre: ""
        self.ntarjeta = ""
        self.codver = ""
        self.ttarjeta = ""

        self.dire = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej19.txt"

    

class Venta():
    def __init__(self):
        self.tarjcredito = TarjetaCredito()
        self.monto = ""
        self.desc = ""

    def remito(self):
        diccionario = {}
        with open(self.tarjcredito.dire, "r") as l:
            with open('/home/agus/Escritorio/ej19.json', "w") as file:
                for linea in l:
                    lin = linea.split(", ")
                    self.tarjcredito.nombre = self.quitarSalto(lin[0])
                    self.tarjcredito.ntarjeta = self.quitarSalto(lin[1])
                    self.tarjcredito.codver = self.quitarSalto(lin[2])
                    self.tarjcredito.ttarjeta = self.quitarSalto(lin[3])
                    self.monto = self.quitarSalto(lin[4])
                    self.desc = self.quitarSalto(lin[5])

                    diccionario.update({"monto": self.monto})
                    diccionario.update({"descripcion": self.desc})
                    diccionario.update({"numtarjeta": self.tarjcredito.ntarjeta})
                    json.dump(diccionario, file)
                    file.write("\n")

                    
                    
        
    def quitarSalto(self, palabras):
        palabras = palabras.split()
        texto = ""
        for i in palabras:
            if i == "":
                raise Exception("Problema con la fuente de datos")
            else:
                texto += i + " "
        return texto


def main():
    venta = Venta()
    venta.remito()
main()