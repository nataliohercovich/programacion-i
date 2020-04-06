class VentaIncog():
    def __init__(self):
        self.dire = "/home/agus/Programacion1/um-programacion-i-2020/58052-agustin,gauchat/Tp1/Ej15.txt"

    def mostrar_venta(self):
        with open(self.dire, "r") as l:

            x = False

            for i in l:
                for j in i:
                    if j == ":":
                        x = True
                    if j == "," or j == ".":
                        x = False
                    if x == True and j != " " and j != ":":
                        j = "x"
                    print(j, end="")
                print("")

def main():
    ventaincog = VentaIncog()
    ventaincog.mostrar_venta()
main()