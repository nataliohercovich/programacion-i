class Triangulo():

    def __init__(self, num):
        self.num = num


def main():
    while True:
        try:
            num = int(input("Ingrese un numero entero:\n"))
            if num <= 0:
                break
            for i in range(num): 
                print("*" * (i+1))
        except:
            print("Ingrese un numero valido")


if __name__ == "__main__":
    main()
