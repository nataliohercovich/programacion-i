from Billetes import *

class Cajero():
    def __init__(self):
        self.fondos = 0
        self.cantBilletes = {
            #[cantBill, valorTotal]
            "$100": [0, 0],
            "$200": [0, 0],
            "$500": [0, 0],
            "$1000": [0, 0]
        }

    def agregarDinero(self, cantDinero):
        for bill in cantDinero:
            if bill.representacion == "$100":
                self.cantBilletes["$100"][0] += 1
                self.cantBilletes["$100"][1] += bill.denominacion
                self.fondos += bill.denominacion

            elif bill.representacion == "$200":
                self.cantBilletes["$200"][0] += 1
                self.cantBilletes["$200"][1] += bill.denominacion
                self.fondos += bill.denominacion
            
            elif bill.representacion == "$500":
                self.cantBilletes["$500"][0] += 1
                self.cantBilletes["$500"][1] += bill.denominacion
                self.fondos += bill.denominacion

            elif bill.representacion == "$1000":
                self.cantBilletes["$1000"][0] += 1
                self.cantBilletes["$1000"][1] += bill.denominacion
                self.fondos += bill.denominacion

    def contarDinero(self):
        #100 200 500 1000
        cont = [0, 0, 0, 0]
        if self.cantBilletes["$100"][0] != 0:
            cont[0] = self.cantBilletes["$100"][0]
        if self.cantBilletes["$200"][0] != 0:
            cont[1] = self.cantBilletes["$200"][0]
        if self.cantBilletes["$500"][0] != 0:
            cont[2] = self.cantBilletes["$500"][0]
        if self.cantBilletes["$1000"][0] != 0:
            cont[3] = self.cantBilletes["$1000"][0]

        a = "Hay " + str(cont[0]) + " billetes de 100\n" + "Hay " + str(cont[1]) + " billetes de 200\n" +  "Hay " + str(cont[2]) + " billetes de 500\n" + "Hay " + str(cont[3]) + " billetes de 1000\n" + "Total: "+ str(self.fondos)

        return str(a)

        


    def extraerDinero(self, monto):
        if monto > self.fondos:
            return("No hay suficientes fondos")
        if monto%100 != 0:
            return("El monto no es multiplo de 100")
        
        salida = True
        exctraccion = []
        cantidad = monto

        while salida:
            if monto >= 1000 and self.cantBilletes["$1000"][0] != 0:
                self.cantBilletes["$1000"][0] -= 1
                self.cantBilletes["$1000"][1] += 1000
                self.fondos -= 1000
                monto -= 1000
                exctraccion.append("$1000")

            if monto >= 500 and self.cantBilletes["$500"][0] != 0:
                self.cantBilletes["$500"][0] -= 1
                self.cantBilletes["$500"][1] += 500
                self.fondos -= 500
                monto -= 500
                exctraccion.append("$500")

            if monto >= 200 and self.cantBilletes["$200"][0] != 0:
                self.cantBilletes["$200"][0] -= 1
                self.cantBilletes["$200"][1] += 100
                self.fondos -= 200
                monto -= 200
                exctraccion.append("$200")

            if monto >= 100 and self.cantBilletes["$100"][0] != 0:
                self.cantBilletes["$100"][0] -= 1
                self.cantBilletes["$100"][1] += 100
                self.fondos -= 100
                monto -= 100
                exctraccion.append("$100")

            if monto == 0:
                salida = False

        return(exctraccion)

if __name__ == "__main__":
    cajero = Cajero()
    cajero.agregarDinero([
    billete1000(), billete1000(), billete1000(), billete1000(),
    billete1000(), billete1000(), billete1000(), billete1000(),
    billete1000(), billete1000()
    ])

    cajero.contarDinero()