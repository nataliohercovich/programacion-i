def cant(frase, letra):
    j = 0
    for i in frase:
        if letra.upper() == i.upper():
            j += 1

    return j

f = input("Ingrese una frase:\n>>")
l = input("Ingrese letra a contar:\n>>")
print("La letra aparece %s veces" % cant(f, l))