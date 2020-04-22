from Billetes import *

class Cajero():
    def __init__(self):
        self.fondos = 0
        self.exctraccion = []
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

        


    def extraerDinero(self, monto, cambio, porcentaje):
        if monto > self.fondos:
            return("No hay suficientes fondos")
        if monto%100 != 0:
            return("El monto no es multiplo de 100")
        
        salida = True
        cantidad = monto

        while salida:
            if cambio == True:
                self.calcularCambio(porcentaje, monto)

            if monto >= 1000 and self.cantBilletes["$1000"][0] != 0:
                self.cantBilletes["$1000"][0] -= 1
                self.cantBilletes["$1000"][1] -= 1000
                self.fondos -= 1000
                monto -= 1000
                self.exctraccion.append("$1000")

            if monto >= 500 and self.cantBilletes["$500"][0] != 0:
                self.cantBilletes["$500"][0] -= 1
                self.cantBilletes["$500"][1] -= 500
                self.fondos -= 500
                monto -= 500
                self.exctraccion.append("$500")

            if monto >= 200 and self.cantBilletes["$200"][0] != 0:
                self.cantBilletes["$200"][0] -= 1
                self.cantBilletes["$200"][1] -= 200
                self.fondos -= 200
                monto -= 200
                self.exctraccion.append("$200")

            if monto >= 100 and self.cantBilletes["$100"][0] != 0:
                self.cantBilletes["$100"][0] -= 1
                self.cantBilletes["$100"][1] -= 100
                self.fondos -= 100
                monto -= 100
                self.exctraccion.append("$100")

            if monto == 0:
                salida = False

            return(self.exctraccion)

        def cambio(self, cambio, monto):
            if cambio >= 100 and self.cantBilletes["$100"][0] != 0:
                while self.cantBilletes["$100"][0] != 0 and cambio != 0:
                    self.cantBilletes["$100"][0] -= 1
                    self.cantBilletes["$100"][1] -= 100
                    self.fondos -= 100
                    cambio -= 100
                    monto -= 100
                    self.exctraccion.append("$100")

            if cambio >= 200 and self.cantBilletes["$200"][0] != 0:
                while self.cantBilletes["$200"][0] != 0 and cambio != 0:
                    self.cantBilletes["$200"][0] -= 1
                    self.cantBilletes["$200"][1] -= 200
                    self.fondos -= 200
                    cambio -= 200
                    monto -= 200
                    self.exctraccion.append("$200")

            if cambio >= 500 and self.cantBilletes["$500"][0] != 0:
                while self.cantBilletes["$500"][0] != 0 and cambio != 0:
                    self.cantBilletes["$500"][0] -= 1
                    self.cantBilletes["$500"][1] -= 500
                    self.fondos -= 500
                    cambio -= 500
                    monto -= 500
                    self.exctraccion.append("$500")

            if cambio >= 1000 and self.cantBilletes["$1000"][0] != 0:
                while self.cantBilletes["$1000"][0] != 0 and cambio != 0:
                    self.cantBilletes["$1000"][0] -= 1
                    self.cantBilletes["$1000"][1] -= 100
                    self.fondos -= 1000
                    cambio -= 1000
                    monto -= 1000
                    self.exctraccion.append("$1000")

            if cambio != 0:
                cambio += 100
                self.cambio(cambio, monto)
                
            self.extraerDinero(monto, False, 0)

        def calcularCambio(self, porcentaje, monto):
            cambio = monto * (1 - (porcentaje / 100))
            cambio = int(100 * round(float(cambio)/base))
            self.cambio(cambio, monto)