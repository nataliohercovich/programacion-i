class Numeros():
    def __init__(self):
        self.nimpares = []

    def ver_impar(self, numero):
        if numero%2 != 0:
            return True

    def lista(self, n):
        if n <= 0:
            return print("Ingrese numero valido")
        else:
            for i in range(1, n+1):
                if self.ver_impar(i) == True:
                    self.nimpares.append(i)

def main():
    numeros = Numeros()
    try:
        n = int(input("Ingrese un numero entero positivo\n>>"))
        numeros.lista(n)
        print("Numeros impares: " + str(numeros.nimpares))
    except:
        print("Ingrese un numero valido")
main()