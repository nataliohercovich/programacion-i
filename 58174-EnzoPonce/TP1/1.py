class conjunto():

    def __init__(self):

        self.nombre = input("Ingrese su nombre: ")
        self.genero = input ("Ingrese su Genero (M o F): ")

    def imprimir(self):
        print("Su nombre es: ", self.nombre)
        print("Su genero es: ", self.genero)

    def comprobar(self):

        if self.genero == "F":
            if self.nombre.lower() < "m":
                grupo = "A"
            else:
                grupo = "B"
        else:
            if self.nombre.lower() > "n":
                grupo = "A"
            else:
                grupo = "B"
        print("Tu grupo es " + grupo)

alumno = conjunto()
alumno.imprimir()
alumno.comprobar()
