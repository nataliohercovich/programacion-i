class Esprimo():   
    
    def primo(n):
        if n < 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True            

def main():
    esprimo = Esprimo
    n = int(input("Ingrese un numero mayor a 0: "))
    if n < 1:
        return print("Ingrese un numero valido")
    resultado = esprimo.primo(n)
    if resultado is True:
        print("El numero es primo")
    else:
        print("El numero no es primo")
main()

