from numero import Numero

class App():

    def main(self):
        numero=Numero()
        numero.setNumero()
        if(numero.numero_primo(numero.getNumero())):
            print ("ES UN NUMERO PRIMO !!")
        else:
            print("NO ES UN NUMERO PRIMO !!")

if __name__ == "__main__":
    app=App()
    app.main()