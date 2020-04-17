class Escuela():
    def __init__(self):
        self.materias = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
        self.notas = []

    def agregar_notas(self, n):
        self.notas.append(n)
    
    def mostrar_notas(self):
        for i in range(0, 5):
            print("En " + self.materias[i] + " te has sacado " + self.notas[i])

def main():
    escuela = Escuela()

    for i in range(0, 5):
        escuela.agregar_notas(input("Ingrese nota de " + escuela.materias[i] + ">>"))

    print("")
    escuela.mostrar_notas()
main()