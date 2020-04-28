from asignatura import Asignatura
class App():

    def main(self):
        self.materias=["Matematicas","Fisica","Quimica","Historia","Lengua"]
        self.lista=[]

        for i in range(len(self.materias)):
            obj=Asignatura(self.materias[i])
            self.lista.append(obj)
            self.lista[i].setNota(self.lista[i].getNombre())
            print()

        for i in range(len(self.materias)):
            self.imprimir(self.lista[i].getNombre(), self.lista[i].getNota())
            print()
        
    def imprimir(self,materia,nota):
        print("En {} la nota es {}\n".format(materia,nota))

if __name__ == "__main__":
    app=App()
    app.main()
    