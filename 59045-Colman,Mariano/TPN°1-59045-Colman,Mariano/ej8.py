class Escuela():
    def __init__(self):
        self.l = ["Matematica", "Fisica", "Literatura", "Quimica"]
        self.n = []

    def agregarNota (self,j):
        self.n.append(j)

    def verNotas (self):
        for i in range (0,4):
            print("En la materia "+self.l[i]+" te has sacado las notas: "+self.n[i])


def main():
    escuela = Escuela()
    for i in range (0,4):
        escuela.agregarNota(input("Ingrese las notas de la materia "+escuela.l[i]+": "))
    print(escuela.verNotas())
main()