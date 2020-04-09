class Curso():

    def __init__(self):
        self.materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        self.notas = []

    def ingreso(self):

        for i in range(5):
            print("Ingrese la nota de "+self.materias[i]+":")
            self.notas.append(input())
        return(self.notas)

    def imprimir(self):

        self.ingreso()
        for j in range(5):
            print(self.materias[j] + self.notas[j])


def main():
    N = Curso()
    N.imprimir()


if __name__ == "__main__":
    main()
