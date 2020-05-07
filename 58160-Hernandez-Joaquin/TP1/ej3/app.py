from numero import Numero
class App():

    def main(self):
        numero=Numero()
        numero.setNumero()
        impares=numero.calculo(numero.getNumero())
        print("\nLos numeros impares hasta el numero elejido son: ",end="")
        for i in range(len(impares)):
            if i==0:
                print("",impares[i],end="")
            else:
                print(",",impares[i],end="")
        print("\n\n")

if __name__ == "__main__":
    app=App()
    app.main()