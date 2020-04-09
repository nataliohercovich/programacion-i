class Primo:
    def es_primo(self, num):
        i = 2
        if num != 2:
            while num % i != 0:
                i += 1
        if i == num:
            return("El numero es primo")
        else:
            return("El numero no es primo")


def main():
    num = int(input("Ingrese un numero\n"))
    info = Primo()
    print(info.es_primo(num))


if __name__ == "__main__":
    main()
