from fecha import Fecha

class App():

    def main(self):
        fecha=Fecha()
        fecha.setFecha()
        mes=self.setMeses()
        self.imprimir(fecha,mes)


    def setMeses(self):
        mes={}
        mes["01"]="Enero"
        mes["02"]="Febrero"
        mes["03"]="Marzo"
        mes["04"]="Abril"
        mes["05"]="Mayo"
        mes["06"]="Junio"
        mes["07"]="Julio"
        mes["08"]="Agosto"
        mes["09"]="Septiembre"
        mes["10"]="Octubre"
        mes["11"]="Noviembre"
        mes["12"]="Diciembre"
        return mes
    

    def imprimir(self,fecha,meses):
        dia,mes,año=fecha.getFecha()
        mes=meses[mes]
        print("Fecha: {} de {} de {}".format(dia,mes,año))

if __name__ == "__main__":
    app=App()
    app.main()