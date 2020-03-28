def impar(numero):
    if numero%2 != 0:
        return True

numeros = []
try:
    n = int(input("Ingrese un numero entero positivo\n>>"))
    if n >= 0:

        for i in range(1, (n + 1)):
            if impar(i) == True:
                numeros.append(i)

        print("Numeros impares: " + str(numeros))

    else:
        print("Ingrese un numero valido")


except:
    print("Ingrese un numero valido")