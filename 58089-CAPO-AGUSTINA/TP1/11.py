class Creditos:

    def __init__(self):
        self.curso = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
        self.total = 0

    def suma(self):
        self.total = self.curso["Quimica"] + self.curso["Fisica"] + self.curso["Matematicas"]
 
    def imprimir(self):
        for materia, creditos in self.curso.items():
            print("La asignatura", materia, "tiene", creditos, "creditos")
        print("Total: ", self.total)


def main():
    cred = Creditos()
    cred.suma()
    cred.imprimir()


if __name__ == "__main__":
    main()
