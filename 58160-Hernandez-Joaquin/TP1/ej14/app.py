from texto import Texto

class App():

    
    def __init__(self):
        self.palabras=[]
        self.repeticiones=[]
        self.diccionario={}
        
    def main(self):
        texto=Texto()
        texto.setTexto()
        self.analizar_texto(texto.getTexto())
        self.imprimir()
        
    def analizar_texto(self,texto):
        self.palabras=texto
        for i in self.palabras:
            self.repeticiones.append(self.palabras.count(i))
        self.diccionario=dict(zip(self.palabras,self.repeticiones))
    
    def imprimir(self):
        lista=[]
        for key in self.diccionario:
            lista.append((self.diccionario[key],key))
        lista.sort(reverse=True)
        for i in range(len(lista)):
            if(i==0):
                print("Numero".center(8),"Palabra".center(14),"Repeticiones".center(14),end="\n\n")
            print(str(i+1).center(6),"{}{}".format(lista[i][1].center(17),str(lista[i][0]).center(15))) 
        print() 
        
if __name__ == "__main__":
    app=App()
    app.main()