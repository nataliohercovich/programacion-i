class Pizza():
    def __init__(self):
        self.tipo = ""
        self.ingrediente = ""
    
    def vegetariana (self,ing):
        self.tipo = "vegetariana"
        if ing.lower() == "pimiento":
            self.ingrediente = "pimiento"
        elif ing.lower() == "tofu":
            self.ingrediente = "tofu"
        else:
            return "Ingrese un ingrediente valido"
    
    def noVegetariana (self,ing):
        self.tipo = "No vegetariana"
        if ing.lower() == "jamon":
            self.ingrediente = "jamon"
        elif ing.lower() == "peperoni":
            self.ingrediente = "peperoni"
        elif ing.lower() == "salmon":
            self.ingrediente = "salmon"
        else:
            return "Ingrese un ingrediente valido"

def selector():
    pizza = Pizza()
    pregunta = str(input("Ingrese si quiere una pizza vegetaria o no (s o n): "))
    if pregunta.lower() != "s" and pregunta.lower() != "n":
        return "Ingrese un valor valido"
    if pregunta == "s":
        ing = str(input("Ingrese un solo ingrediente de la lista\nPimiento\nTofu\n: "))
        pizza.vegetariana(ing)
    if pregunta == "n":
        ing = str(input("Ingrese un solo ingrediente de la lista\nJamon\nSalmon\nPeperoni\n: "))
        pizza.noVegetariana(ing)
    print("Su pizza es " +pizza.tipo+" y tiene los siguientes ingredientes: Mozzarella, salsa y "+pizza.ingrediente)

selector()