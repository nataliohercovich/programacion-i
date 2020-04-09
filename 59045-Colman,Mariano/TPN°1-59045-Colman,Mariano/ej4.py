class Triangulo():
    def __init__(self):
        self.asterisco="*"
    
    def forma (self,n):
        for i in range (0,n):
            print(self.asterisco*(i+1))

def main():
    triangulo = Triangulo()
    n = int(input("Ingrese la altura del triangulo: "))
    if n < 1:
        return print("Ingrese una altura valida")
    triangulo.forma(n)

main()