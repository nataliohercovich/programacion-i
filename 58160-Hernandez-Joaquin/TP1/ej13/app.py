from numeros import Numeros
from statistics import mean

class App():

    def main(self):
        num=Numeros()
        num.setGenerarNumeros()
        self.imprimir(num.getGenerarNumeros())
    
    def imprimir(self,lista):
        valores=lista
        prom=mean(valores)
        print("NUMEROS:",valores)        
        print("\nEl promedio de los numeros es: ",prom)

if __name__ == "__main__":
    app=App()
    app.main()