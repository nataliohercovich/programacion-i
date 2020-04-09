class Impar():
    def __init__(self):
        self.num = 0

    def ingreso(self):
        self.num = int(input("Ingrese un numero entero positivo: "))

    def buscar(self):
        for i in range(1, self.num, 2):
            if self.num > 0:
                print(i)


def main():
    lista = Impar()
    lista.ingresar()
    lista.buscar()


if __name__ == "__main__":
    main()
