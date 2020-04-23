from billetes import *


class CajeroAutomatico():
    def __init__(self):
        self.total_dinero = 0
        self.cant_billetes = [
            ['$1000', 0, 1000],
            ['$500', 0, 500],
            ['$200', 0, 200],
            ['$100', 0, 100]
        ]
        self.bill_parcial = {
            '$100' : 0,
            '$200' : 0,
            '$500' : 0,
            '$1000' : 0
        }
        self.extraccion = []

    def agregar_dinero(self, dinero):
        for bill in dinero:
            for billete in self.cant_billetes:
                if billete[0] == bill.get_rep():
                    billete[1] += 1

    def contar_dinero(self):
        for billete in self.cant_billetes:
            valor = billete[1] * billete[2]
            self.total_dinero += valor
            self.bill_parcial[billete[0]] += valor

    def extraer_dinero(self, monto, r=False):
        num = 0
        self.correct_input(monto)
        if r:
            self.cant_billetes.reverse()
        for elem in self.cant_billetes:
            if monto != 0:
                if elem[1] != 0:
                    temp = int(monto/elem[2])
                    if elem[1] < temp:
                        rg = elem[1]
                    else:
                        rg = temp
                    for i in range(rg):
                        monto -= elem[2]
                        self.cant_billetes[num][1] -= 1
                        self.bill_parcial[elem[0]] -= elem[2]
                        self.extraccion.append(elem[0])
            num += 1
# ej2


    def extraer_dinero_cambio(self, monto, por):
        self.correct_input(monto)
        if (101 > por > 0) is False:
            raise Exception('El rango de porcentaje de cambio puede solo ir de 0 a 100')
        por = por/100
        cambio = monto * por
        self.calcular_cambio(por, cambio)
        self.extraer_dinero(int(monto))
        self.extraer_dinero(int(cambio), True)

    def correct_input(self, monto):
        if monto%100 != 0:
            raise Exception('El monto solicitado no es multiplo de 100')
        if self.total_dinero < monto:
            raise Exception(('El cajero solo tiene : {caja} y usted quiere retirar : {ext}').format(
        caja = self.total_dinero,
        ext = monto
        ))

    def calcular_cambio(self, por, monto):
        cambio = monto * (por / 100)
        cambio = int(100 * round(float(cambio)/100))

    def get_billetes_parciales(self):
        listado = []
        for key in self.bill_parcial:
            temp = [key, self.bill_parcial[key]]
            listado.append(temp)
        return listado

    def get_total_dinero(self):
        return self.total_dinero
        


if __name__ == "__main__":
    objeto = CajeroAutomatico()
    # objeto.agregar_dinero([
    #     Bill_100(),Bill_100(),Bill_1000(),Bill_200(),Bill_500(),Bill_1000(),
    #     Bill_100(),Bill_100(),Bill_1000(),Bill_200(),Bill_500(),Bill_1000(),
    #     Bill_100(),Bill_100(),Bill_1000(),Bill_200(),Bill_500(),Bill_1000(),
    #     Bill_100(),Bill_100(),Bill_1000(),Bill_200(),Bill_500(),Bill_1000(),
    #     Bill_100(),Bill_100(),Bill_1000(),Bill_200(),Bill_500(),Bill_1000(),
    #     Bill_100(),Bill_100(),Bill_1000(),Bill_200(),Bill_500(),Bill_1000()
    # ])
    objeto.contar_dinero()
#    objeto.extraer_dinero(1400)
    objeto.extraer_dinero_cambio(3600, 5)
    print(objeto.extraccion)
    print(objeto.bill_parcial)
    print(objeto.cant_billetes)