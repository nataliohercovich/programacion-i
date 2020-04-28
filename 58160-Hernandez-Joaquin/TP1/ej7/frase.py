class Letra():
    def main(self):
        frase=input("Ingrese una frase: \n")
        letra=input("Ingrese la letra que quiere averiguar que mas se repita:  \n")

        a=frase.count(letra)
        print("La cantidad de veces que se repite",letra, "es:",a)

if __name__ == "__main__":
    app=Letra()
    app.main()