from numeros import Numeros


class App():

    def main(self):
        num_aleatorios=Numeros()
        num_aleatorios.setGenerar_numeros()
        self.imprimir(num_aleatorios.getGenerar_numeros())
    
    def imprimir(self,diccionario):
        valores=diccionario.values()
        valores=list(valores)
        valores.sort(reverse=True)
        print("NUMEROS: ",valores)
        print() 
        

if __name__ == "__main__":
    app=App()
    app.main()