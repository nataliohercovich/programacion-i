class curso():

    def __init__(self):
        self.lista = ['matematicas','fisica','quimica','lengua','historia']
        self.notas = []

    def ingresar(self):
        
        for i in self.lista:
            print ("¿ Que nota has sacado en",i,"?")
            if i == 'matematicas':
                m = input("")
                self.notas.append(m)
            if i == 'fisica':
                f = input("")
                self.notas.append(f)
            if i == 'quimica':
                q = input("")
                self.notas.append(q)
            if i == 'lengua':
                l = input("")
                self.notas.append(l)
            if i == 'historia':
                h = input("")
                self.notas.append(h)

        print ("En", self.lista[0],"has obtenido: ", self.notas[0])            
        print ("En", self.lista[1],"has obtenido: ", self.notas[1])
        print ("En", self.lista[2],"has obtenido: ", self.notas[2])
        print ("En", self.lista[3],"has obtenido: ", self.notas[3])
        print ("En", self.lista[4],"has obtenido: ", self.notas[4])


materias = curso()
materias.ingresar()