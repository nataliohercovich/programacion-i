import random
import operator

class Dicc():
    def __init__(self):
        self.A = {1 : None, 2 : None, 3 : None, 4 : None, 5 : None}
        self.Aord = []

    def generar_numeros(self):
        for i in range (1, 6):
            self.A[i] = random.randint(1, 10)

    def dicc_inicial(self):
        for i in range(1, 6):
            if i == 5:
                print(str(self.A[i])+ "\n")
            else:
                print(str(self.A[i]) + ", ", end="")

    def dicc_ordenado(self):
        self.Aord = sorted(self.A.items(), key=operator.itemgetter(1), reverse=True)

        for j in range(0, 5):
            a = self.Aord[j][1]
            if j == 4:
                print(str(a)+ "\n")
            else:
                print(str(a) + ", ", end="")

def main():
    dicc = Dicc()
    dicc.generar_numeros()
    print("Diccionario inicial:")
    dicc.dicc_inicial()
    print("Diccionario ordenado:")
    dicc.dicc_ordenado()
main()