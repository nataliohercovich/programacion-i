class Venta():
    def __init__(self):
        self.dire = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej15.txt"
        self.etiq = ["nombre", "monto", "descripcion", "formadepago"]

    def imprimir_txt(self):
        with open(self.dire, "r") as l:
            for i in self.etiq:
                print(i, end=", ")
            print("\n")
            for i in l:
                print(i)

def main():
    venta = Venta()
    #venta.dire = input("Ingrese direccion del txt >>")
    venta.imprimir_txt()
main()