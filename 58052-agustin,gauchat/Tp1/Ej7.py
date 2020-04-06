class Contador():
    
    def cant(self, frase, letra):
        j = 0
        for i in frase:
            if letra.upper() == i.upper():
                j += 1

        return j

def main():
    contador = Contador()
    f = input("Ingrese una frase:\n>>")
    l = input("Ingrese letra a contar:\n>>")
    print("La letra aparece %s veces" % contador.cant(f, l))
main()