class frase_letra():

    def __init__(self):
        self.frase = ""
        self.letra = ""

    def ingresar(self):
        self.frase = input("Ingrese una frase: \n")
        self.letra = input("Ingrese la letra que desea buscar: \n")

    def metodo(self):
        contador = 0
        for i in self.frase:
            if i == self.letra:
                contador += 1
        print("La letra '%s' aparece '%i' veces" % (self.letra,contador))

cuenta = frase_letra()
cuenta.ingresar()
cuenta.metodo()