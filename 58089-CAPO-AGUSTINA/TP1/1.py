class Alumno():

    def __init__(self, sexo, nombre):
        self.sexo = sexo
        self.nombre = nombre
 
    def grupo(self):
        if (self.sexo == "femenino" and self.nombre <= "M") or (self.sexo == "masculino" and self.nombre >= "N"):
            print("Integra el Grupo A")
        else:
            print("Integra el Grupo B")


def main():
    nombre = input("Ingrese su nombre con la primera letra en mayuscula:\n")
    sexo = input("Ingrese su sexo:\n")
    alumno = Alumno(sexo, nombre)
    alumno.grupo()


if __name__ == "__main__":
    main()
