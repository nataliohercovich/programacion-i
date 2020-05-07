from numero import Numero

class App():

    def main(self):
        numero=Numero()
        numero.setNumero()
        numero.getNumero()
        for i in range(numero.getNumero()):
            print()
            for j in range(i+1):
                print("*",end="")
            print("")
        print()


if __name__ == "__main__":
    app=App()
    app.main()