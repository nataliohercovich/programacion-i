import random


class Promedios:
    def __init__(self):
        self.numeros = []
        self.num = 0

    def promedio(self):
        for i in range(10):
            self.numeros.append(random.randrange(1,11))
            self.num += self.numeros[i]
        self.num = self.num/10
        return str(self.num)


def main():
    info = Promedios()
    prom = info.promedio()
    print(info.numeros)
    print("Promedio:", prom)


if __name__ == "__main__":
    main()
