from texto import Texto

class App():

    def main(self):
        texto=Texto()
        texto.setTexto()
        self.imprimir(texto.getTexto())

    def imprimir(self,lista):
        for i in range(len(lista)):   
            for j in range(len(lista[i])):
                if(j==0):
                    print(str(i+1).center(6),end="")
                print(lista[i][j].center(20),end="")
            print("\n")
                
if __name__ == "__main__":
    app=App()
    app.main()
