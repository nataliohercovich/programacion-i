class Pizza:
    def eleccion(self, ingrediente, pizza):
        if pizza == 1:
            if ingrediente == 1:
                return("Su pedido es:\nPizza vegetariana con muzzarela, tomate y pimiento")
            else:
                return("Su pedido es:\nPizza vegetariana con muzzarela, tomate y tofu")
        else:
            if ingrediente == 1:
                return("Su pedido es:\nPizza no vegetariana con muzzarela, tomate y peperoni")
            elif ing == 2:
                return("Su pedido es:\nPizza no vegetariana con muzzarela, tomate y jamon")
            else:
                return("Su pedido es:\nPizza no vegetariana con muzzarela, tomate y salmon")


def main():
    pizza = int(input("Ingrese 1 si quiere pizza vegetariana y 2 si quiere pizza no vegetariana \n"))
    print("Elija un ingrediente extra")
    if pizza == 1:
        ing = int(input("Ingrese 1 para PIMIENTO \nIngrese 2 para TOFU\n"))
    else:
        ing = int(input("Ingrese 1 para PEPERONI\nIngrese 2 para JAMON\nIngrese 3 para SALMON\n"))

    info = Pizza()
    print(info.eleccion(ing, pizza))


if __name__ == "__main__":
    main()
