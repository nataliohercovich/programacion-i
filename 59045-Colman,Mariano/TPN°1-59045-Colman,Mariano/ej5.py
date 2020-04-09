class Triangulo():

    def forma (n):
        l=[]
        for i in range(1,n+1,2):
            l.append(i)
            numero = str(l)
            numero = numero.replace('[','')
            numero = numero.replace(']','')
            numero = numero.replace(',','')
            print(numero[::-1])


def main():
    triangulo = Triangulo
    n = int(input("Ingrese un numero entero: "))
    if n < 0:
        return print("Ingrese un numero positivo")

    triangulo.forma(n)
main()
