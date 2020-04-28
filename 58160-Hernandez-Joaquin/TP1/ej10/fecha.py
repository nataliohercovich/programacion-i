class Fecha():

    def __init__(self):
        self.dia=""
        self.mes=""
        self.año=""
    
    def setFecha(self):
        while True:
            fecha=input("Ingrese la fecha en el formate dd/mm/aaaa :")
            try:
                if(len(fecha)==10):
                    fecha=fecha.split("/")
                    if (int(fecha[0])<32 and int(fecha[1])<13 and int(fecha[2])):
                        self.dia=fecha[0]
                        self.mes=fecha[1]
                        self.año=fecha[2]
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Ingrese la fecha correta")

    def getFecha(self):
        return self.dia,self.mes, self.año