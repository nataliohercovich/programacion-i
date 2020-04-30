class fecha():
    
    def __init__(self):
        self.meses = ['','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        self.dia = ""

    def ingresar(self):
        self.dia = input("Ingrese una fecha en formato dd/mm/aaaa: ")
        lista = self.dia.split("/")
        mes = self.meses[int(lista[1])]
        print(lista[0],"de",mes,"de",lista[2])

numero = fecha()
numero.ingresar()