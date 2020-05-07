from texto import Texto

class App():

    def main(self):
        texto=Texto()
        texto.setTexto()
        self.imprimir(texto.getTexto())

    def imprimir(self,lista):
        for i in range(len(lista)):
            if(i==0):
                print("Venta".center(6),"Nombre".center(18),"Monto".center(20),"Descripcion".center(18),"Forma de pago".center(20))
                print ()
            for j in range(len(lista[i])):
                if(j==0):
                    print(str(i+1).center(6),end="")
                print(lista[i][j].center(20),end="")
            print()
                
if __name__ == "__main__":
    app=App()
    app.main()
