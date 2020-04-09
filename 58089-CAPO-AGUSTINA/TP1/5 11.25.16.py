class Triangulo():

    def __init__(self):
        self.num = 1
        self.lista = []

    def ingreso(self):
        self.num = int(input("Ingrese un numero: "))

    def proceso(self):
        for i in range(1, self.num, 2):
            self.lista.append(i)
            self.lista.sort()
            self.lista.reverse()
            print(self.lista)


def main():
    tr = Triangulo()
    tr.ingreso()
    tr.proceso()


if __name__ == "__main__":
    main()
