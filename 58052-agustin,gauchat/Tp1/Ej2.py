class Pizza():
    def __init__(self):
        self.tipo = ""
        self.ing = ""

    def vegetariana(self, i):
        self.tipo = "vegetariana"
        if i == 1:
            self.ing = "pimiento"
        if i == 2:
            self.ing = "tofu"
        if i != 1 and i != 2:
            return("Ingrese un valor valido")

    def no_vegetariana(self, i):
        self.tipo = "no vegetariana"
        if i == 1:
            self.ing = "peperoni"
        if i == 2:
            self.ing = "jamon"
        if i == 3:
            self.ing = "salmon"
        if i != 1 and i != 2 and i != 3:
            return("Ingrese un valor valido")

def main():
    pizza = Pizza()
    try:
        tp = int(input("Ingrese su tipo de pizza:\n[1]Pizza vegetariana\n[2]Pizza no vegetariana\n>>"))
        if tp != 1 and tp != 2:
            print("Ingrese un valor valido")

        if tp == 1:
            i = int(input("Ingrese igredientes:\n[1]Pimiento\n[2]Tofu\n>>"))
            pizza.vegetariana(i)

        if tp == 2:
            i = int(input("Ingrese igredientes:\n[1]Peperoni\n[2]Jamon\n[3]Salmon\n>>"))
            pizza.no_vegetariana(i)

        print("Su pizza " + pizza.tipo + " contiene tomate, queso y " + pizza.ing)
    except:
        print("Ingrese un valor valido")
main()