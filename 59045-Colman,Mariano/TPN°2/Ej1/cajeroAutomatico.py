from billete import Billetes, Billete100, Billete200, Billete500, Billete1000

class Cajero():
    def __init__(self):
        self.total = 0
        self.lista1 = []

    def agregarDinero(self, listaP):
        for i in listaP:
            self.lista1.append(i)

    def contarDinero(self):
        self.total100 = 0
        self.total200 = 0
        self.total500 = 0
        self.total1000 = 0

        self.cantidad100 = 0
        self.cantidad200 = 0
        self.cantidad500 = 0
        self.cantidad1000 = 0

        for i in self.lista1:
            if i.moneda_valor == 100:
                self.total100 = self.total100+100
                self.cantidad100 += 1
            elif i.moneda_valor == 200:
                self.total200 = self.total200+200
                self.cantidad200 += 1
            elif i.moneda_valor == 500:
                self.total500 = self.total500+500
                self.cantidad500 += 1
            elif i.moneda_valor == 1000:
                self.total1000 = self.total1000+1000
                self.cantidad1000 += 1

        self.total = self.total100+self.total200+self.total500+self.total1000

        print(self.cantidad100, self.cantidad200, self.cantidad500, self.cantidad1000, self.total100, self.total200, self.total500, self.total1000, self.total)

    def extraerDinero(self, extraccion):
        lExtraidos = []
        if extraccion % 100 == 0:
            if self.total > extraccion:
                while extraccion >= 1000 and self.cantidad1000 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 1000:
                            extraccion = extraccion - 1000
                            lExtraidos.append(i.representacion)
                            self.lista1.remove(i)
                            self.cantidad1000 = self.cantidad1000-1
                            print(i.representacion)
                            break

                while extraccion >= 500 and self.cantidad500 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 500:
                            extraccion = extraccion - 500
                            lExtraidos.append(i.representacion)
                            self.lista1.remove(i)
                            self.cantidad500 = self.cantidad500-1
                            print(i.representacion)
                            break

                while extraccion >= 200 and self.cantidad200 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 200:
                            extraccion = extraccion - 200
                            lExtraidos.append(i.representacion)
                            self.lista1.remove(i)
                            self.cantidad200 = self.cantidad200-1
                            print(i.representacion)
                            break

                while extraccion >= 100 and self.cantidad100 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 100:
                            extraccion = extraccion - 100
                            lExtraidos.append(i.representacion)
                            self.lista1.remove(i)
                            self.cantidad100 = self.cantidad100-1
                            print(i.representacion)
                            break

            else:
                print("El cajero no cuenta con el dinero suficiente")
        else:
            print("Ingrese un monto valido")

"""pruebas
def main():
    a = Billete1000()
    aa = Billete1000()
    aaa = Billete1000()
    aaaa = Billete1000()
    aaaaa = Billete1000()
    b = Billete500()
    c = Billete200()
    d = Billete100()
    listaP = [a,aa,aaa,aaaa,aaaaa,b,c,d]
    cajero = Cajero()
    cajero.agregarDinero(listaP)
    cajero.contarDinero()
    cajero.extraerDinero(3500)
    cajero.contarDinero()

main()