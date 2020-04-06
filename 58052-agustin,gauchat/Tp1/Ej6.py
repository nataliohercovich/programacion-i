import math
 
class Primo():

    def es_primo(self, numero):
        if (numero<=1):
            return print ("\nEl numero %s NO es primo" % numero)
    
        for i in range(2, math.ceil(math.sqrt(numero))+1):
            if(numero%i==0 and i!=numero):
                return print ("\nEl numero %s NO es primo" % numero)
        return print ("\nEl numero %s es primo" % numero)

def main():
    primo = Primo()
    primo.es_primo(int(input("inserta un numero >> ")))
main()