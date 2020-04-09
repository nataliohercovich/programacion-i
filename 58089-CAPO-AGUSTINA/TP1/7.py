class FyL():

    def __init__(self, frase, letra):
        self.frase = frase
        self.letra = letra

    def cantidad(self):
        self.cant = self.frase.count(self.letra)
        cant = self.cant
        print("La cantidad de repeticiones de la letra es: ", cant)


def main():
    frase = input("Ingrese la frase: \n")
    letra = input("Ingrese la letra\n")
    cant = FyL(frase, letra)
    cant.cantidad()


if __name__ == "__main__":
    main()
