class VentaIncog():
    def __init__(self):
        self.dire = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej15.txt"
        self.etiq = ["Nombre", "Monto", "Descripcion", "Formadepago"]

    def mostrar_venta(self):
        with open(self.dire, "r") as l:
            for i in l:
                j = i.split(", ")
                for k in range(0, len(self.etiq)):
                    if k == len(self.etiq) - 1:
                        print(self.etiq[k] + ": " + j[k])
                    else:
                        print(self.etiq[k] + ": " + j[k], end=", ")
                print("")



def main():
    ventaincog = VentaIncog()
    ventaincog.mostrar_venta()
main()