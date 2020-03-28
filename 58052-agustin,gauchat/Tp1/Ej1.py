def mujer(nombre):
    if nombre[0].upper() == "A" or nombre[0].upper() == "B" or nombre[0].upper() == "C" or nombre[0].upper() == "D" or nombre[0].upper() == "E" or nombre[0].upper() == "F" or nombre[0].upper() == "G" or nombre[0].upper() == "H" or nombre[0].upper() == "I" or nombre[0].upper() == "J" or nombre[0].upper() == "K" or nombre[0].upper() == "L" or nombre[0].upper() == "M":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")

def hombre(nombre):
    if nombre[0].upper() == "N" or nombre[0].upper() == "O" or nombre[0].upper() == "P" or nombre[0].upper() == "Q" or nombre[0].upper() == "R" or nombre[0].upper() == "S" or nombre[0].upper() == "T" or nombre[0].upper() == "U" or nombre[0].upper() == "V" or nombre[0].upper() == "W" or nombre[0].upper() == "X" or nombre[0].upper() == "Y" or nombre[0].upper() == "Z":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")

s = input("Ingrese sexo, M o F\n")
n = input("Ingrese nombre\n")

if s.upper() == "F":
    mujer(n)

if s.upper() == "M":
    hombre(n)

if s.upper() != "M" or s.upper() != "F":
    print("Sexo invalido")