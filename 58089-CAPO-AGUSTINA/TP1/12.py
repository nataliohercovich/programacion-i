import random


class NumeroA():

    def __init__(self):

        self.diccionario = {}
        self.lista = []

    def generar(self):
        for i in range(10):
            self.lista.append(random.randint(1, 10))
        self.lista.sort()
        self.lista.reverse()
        print(self.lista)


def main():

    na = NumeroA()
    na.generar()


if __name__ == "__main__":
    main()
