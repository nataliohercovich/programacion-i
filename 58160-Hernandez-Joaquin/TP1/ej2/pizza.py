class Pizza():

    def __init__(self):
        self.tipo = " "
        
        
    def setTipo(self):
        while True:
            try:
                self.tipo = input("Ingrese el tipo de pizza deseada V(Vegetariana)- NV(No Vegetariana):  ")
                self.tipo = self.tipo.upper()
                if self.tipo== "NV":
                    self.tipo = "No Vegetariana"
                    break
                elif self.tipo == "V":
                    self.tipo = "Vegetariana"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error!!! Ingrese un tipo de pizza correcto")

    def getTipo(self):
        return self.tipo
