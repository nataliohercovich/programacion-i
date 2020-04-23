from io import open


class lectura():

    def leer_texto(self):
        f = open('ArchivoVentas.txt', 'r')
        texto = f.read()
        f.close()
        print(texto)


if __name__ == "__main__":
    read = lectura()
    read.leer_texto()
