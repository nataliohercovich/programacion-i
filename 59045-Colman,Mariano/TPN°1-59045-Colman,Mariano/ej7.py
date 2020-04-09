class Count():

    def conta(self,frase,letra):
        contador = 0
        for i in frase:
            if letra.lower() == i.lower():
                contador = contador+1
        return contador

def main():
    count = Count()
    fra = str(input("Ingrese una frase: "))
    let = str(input("Ingrese la letra que quiere contar: "))
    resultado = count.conta(fra,let)
    print("La letra " +let.upper()+ " aparece %s veces" %count.conta(fra,let)) 

main()