from numero import Numero

class App():

    def main(self):
        numero=Numero()
        numero.setNumero()
        numero.calcular_impares(numero.getNumero())
        lista=numero.calcular_impares(numero.getNumero())

        for i in range(numero.getNumero()):
            print()
            lista[i].sort(reverse=True)
            for j in range(len(lista[i])):
                print(lista[i][j],end=" ")
            print()


if __name__ == "__main__":
    app=App()
    app.main()