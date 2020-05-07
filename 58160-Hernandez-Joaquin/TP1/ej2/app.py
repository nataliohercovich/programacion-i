from pizza import Pizza
from tipo import Tipo

class App():

    def main(self):
        pizza=Pizza()
        pizza.setTipo()
        tipo1=Tipo()
        tipo1.setIngredientes(pizza.getTipo())
        
        print("Pizza elegida: " ,pizza.getTipo())
        print("Ingredientes: ",end="")
        lista=tipo1.getIngredientes()
        for i in range(len(lista)):
            if i==0:
                print(lista[i],end="")
            else:
                print(",",lista[i],end="")
        print()
if __name__ == '__main__':
    app=App()
    app.main()