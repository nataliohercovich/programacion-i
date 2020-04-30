class creditos_materia():

    def __init__(self):
        self.materias = {'Matematicas':6,'Física': 4, 'Química': 5}
        self.suma = 0

    def imprimir(self):
        for materia,creditos in self.materias.items():
            print("%s tiene %s creditos"%(materia,creditos))
            self.suma += creditos    
        print("El total de creditos es: ", self.suma)

mat = creditos_materia()
mat.imprimir()