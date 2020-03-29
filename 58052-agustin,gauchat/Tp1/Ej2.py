try:
    tp = int(input("Ingrese su tipo de pizza:\n[1]Pizza vegetariana\n[2]Pizza no vegetariana\n>>"))
    if tp != 1 and tp != 2:
        print("Ingrese un valor valido")

    if tp == 1:
        t = "vegetariana"
        i = int(input("Ingrese igredientes:\n[1]Pimiento\n[2]Tofu\n>>"))
        if i == 1:
            ing = "pimiento"
        if i == 2:
            ing = "tofu"
        if i != 1 and i != 2:
            print("Ingrese un valor valido")

    if tp == 2:
        t = "no vegetariana"
        i = int(input("Ingrese igredientes:\n[1]Peperoni\n[2]Jamon\n[3]Salmon\n>>"))
        if i == 1:
            ing = "peperoni"
        if i == 2:
            ing = "jamon"
        if i == 3:
            ing = "salmon"
        if i != 1 and i != 2 and i != 3:
            print("Ingrese un valor valido")

    print("Su pizza " + t + " contiene tomate, queso y " + ing)
except:
    print("Ingrese un valor valido")
