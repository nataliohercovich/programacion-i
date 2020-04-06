class Piramide():
    
    def hacer_piramide(n):
        l = []
        for i in range(1, int(n)+1):
            if (i % 2 != 0):
                l.append(i)
                num = str(l)
                num = num.replace(',', '')
                num = num.replace('[', '')
                num = num.replace(']', '')
                print(num[::-1])

def main():
    piramide = Piramide
    piramide.hacer_piramide(input('Ingrese un numero entero >>'))
main()