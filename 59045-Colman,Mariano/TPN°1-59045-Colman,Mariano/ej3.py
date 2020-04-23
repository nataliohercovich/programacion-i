class Impares():
    def __init__(self):
        self.l=[]

    def lista (self,n):
        if n < 1:
            return print("Ingrese un numero entero positivo")
        else:
            for a in range(1,n+1,2):
                self.l.append(a)
    
def main():
    impares = Impares()
    n=int(input("Ingrese un numero entero positivo:"))
    impares.lista(n)
    print(impares.l)

main()