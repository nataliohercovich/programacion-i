class CombinacionError(Exception):
    pass


class MultplicidadError(Exception):
    pass


class CantidadError(Exception):
    pass


class Cajero():
    def __init__(self):
        self.cant100 = []
        self.cant200 = []
        self.cant500 = []
        self.cant1000 = []
        self.montos_p = []
        self.monto_total = 0
        self.b_extr = [0, 0, 0, 0]
        self.cantidades = []
        self.sacado = []
        self.total = 0

    def agregar_dinero(self, billetes):
        for i in billetes:
            if i.denominacion == 1000:
                self.cant1000.append(i.denominacion)
            elif i.denominacion == 500:
                self.cant500.append(i.denominacion)
            elif i.denominacion == 200:
                self.cant200.append(i.denominacion)
            else:
                self.cant100.append(i.denominacion)

    def contar_dinero(self):
        text1 = ""
        self.cantidades = [len(self.cant1000), len(self.cant500),
                           len(self.cant200), len(self.cant100)]
        self.montos_p = [self.cantidades[0] * 1000, self.cantidades[1] * 500,
                         self.cantidades[2] * 200, self.cantidades[3] * 100]
        self.monto_total = int(self.montos_p[0] + self.montos_p[1] +
                               self.montos_p[2] + self.montos_p[3])
        for i in range(len(self.cantidades)):
            if i == 0:
                if len(self.cant1000) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $1000,"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
            elif i == 1:
                if len(self.cant500) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $500,"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
            elif i == 2:
                if len(self.cant200) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $200,"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
            else:
                if len(self.cant100) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $100"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
        text1 += "Total $" + str(self.monto_total)
        return text1

    def extraer_dinero(self, monto):
        tx = ""
        tx2 = ""
        self.caja = [len(self.cant1000), len(self.cant500),
                     len(self.cant200), len(self.cant100)]
        self.total += (len(self.cant1000) * 1000) + (len(self.cant500) * 500)
        self.total += (len(self.cant200) * 200) + (len(self.cant100) * 100)
        try:
            if monto % 100 != 0:
                raise MultplicidadError
        except MultplicidadError:
            return "Error. El monto es incorrecto"
        try:
            if monto >= self.total:
                raise CantidadError
        except CantidadError:
            return "Error. Quiere sacar mas dinero de lo que se puede"
        val = [1000, 500, 200, 100]
        for i in range(len(val)):
            while self.caja[i] > 0 and monto >= val[i]:
                monto -= val[i]
                self.caja[i] -= 1
                self.b_extr[i] += 1
        try:
            if monto != 0:
                raise CombinacionError
        except CombinacionError:
            tx += "Error. No hay una combinacion de billetes que nos permita "
            tx += "extraer ese monto."
            return tx
        for i in range(len(self.b_extr)):
            if i == 0:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $1000\n"
            elif i == 1:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $500\n"
            elif i == 2:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $200\n"
            else:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $100\n"
        return tx2


if __name__ == "__main__":
    main = Cajero()
