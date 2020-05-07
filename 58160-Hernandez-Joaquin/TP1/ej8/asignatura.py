class Asignatura():

    def __init__(self,nombre):
        self.nombre=nombre
        self.nota=0
    
    def getNombre(self):
        return self.nombre

    def setNota(self,materia):
        while True:
            try:
                self.nota=int(input("\nIngrese la nota de {}:".format(materia)))
                if self.nota<0 and self.nota>10:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nLa nota ingresada es invalida. Intente nuevamente")
    
    def getNota(self):
        return self.nota
