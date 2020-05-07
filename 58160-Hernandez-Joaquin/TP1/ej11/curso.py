class Curso():

    def __init__(self):
        self.asignaturas={}

    def main(self):        
        self.asignaturas={'Matematica':6,"Fisica":4,"Quimica":5}
        total_creditos=0
        
        for key in self.asignaturas:
            print (key, "tiene",self.asignaturas[key],"creditos")
            total_creditos=total_creditos+self.asignaturas[key]
        
        print("Numero total de creditos:",total_creditos)
        print() 

if __name__ == "__main__":
    app=Curso()
    app.main()

