from pizza import Pizza

class Tipo(): 
 
    def __init__(self):
        self.ingredientes=[] 
        self.ingredientes.append("Mozzarella")
        self.ingredientes.append("Tomate") 
        


    def setIngredientes(self,tipo):
        if tipo=='No Vegetariana':
            while True:
                try:
                    self.eleccion=int(input("""
                        1-Peperoni
                        2-Jamon
                        3-Salmon\n
                        Elija su ingrediente: """))

                    if(self.eleccion==1):
                        self.ingredientes.append("Peperoni")
                        break
                    elif(self.eleccion==2):
                        self.ingredientes.append("Jamon")
                        break
                    elif(self.eleccion==3):
                        self.ingredientes.append("Salmon")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("\nIntroduzca una opcion valida") 
        else:
            while True:
                try:
                    self.eleccion = int(input("""
                        1-Pimiento
                        2-Tofu\n
                        Elija su ingrediente: """))
                    if(self.eleccion==1):
                        self.ingredientes.append("Pimiento")
                        break
                    elif(self.eleccion==2):
                        self.ingredientes.append("Tofu")
                        break
                    else:
                            raise ValueError
                except ValueError:
                    print("\nIntroduzca una opcion valida")
                              
    def getIngredientes(self):
        return self.ingredientes
