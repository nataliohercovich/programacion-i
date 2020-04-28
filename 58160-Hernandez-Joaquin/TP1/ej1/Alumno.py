class Alumno():
    
    def __init__(self):
        self.nombre = " "
        self.sexo = " "

    def setNombre(self):
        self.nombre = input("Ingrese su nombre\n ")
        self.nombre = self.nombre.upper()
    
    def getNombre(self):
        return self.nombre
    
    def setSexo(self):
        while True:
            try:
                self.sexo = input("Ingrese su sexo (M/F):\n")
                self.sexo = self.sexo.upper()
                if (self.sexo!= "M" and self.sexo != "F"):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Ingrese la letra correcta\n")

    def getSexo(self):
        return self.sexo

