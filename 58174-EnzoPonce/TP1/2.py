class restaurant():

    def __init__(self):
        self.tipo = " "
        self.ingrediente = " "

    def imprimir(self):

        print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
        self.tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")

    def comprobar(self):

        if self.tipo == "1":
            print("\nLa pizza vegetariana puede llevar:\n1-Pimiento\n2-tofu\n")
            self.ingrediente = input("Coloque el número del ingrediente a eleccion: ")
            if self.ingrediente == "1":
                print("\nSu pizza es vegetaria y lleva tomate, muzarella y pimiento")
            else:
                print("\nSu pizza es vegetaria y lleva tomate, muzarella y tofu")
        else:
            print("\nLa pizza no vegetariana puede llevar:\n1-Peperoni\n2-Jamón\n3-Salmón\n")
            self.ingrediente = input("Coloque el número del ingrediente a eleccion: ")
            if self.ingrediente == "1":
                print("\nSu Pizza no es vegetariana y lleva tomate, muzarella y peperoni")
            elif self.ingrediente == "2":
                print("\nSu Pizza no es vegetariana y lleva tomate, muzarella y jamón")
            else:
                print("\nSu Pizza no es vegetariana y lleva tomate, muzarella y salmón")
            
        
pizza = restaurant()
pizza.imprimir()
pizza.comprobar()