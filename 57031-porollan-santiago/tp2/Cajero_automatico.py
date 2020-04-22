

class Cajero_automatico():
    def __init__(self):
        self.almacen_de_billetes = {'100': [], '200': [],
                                    '500': [], '1000': []}
        self.contar_dinero()

    def agregar_dinero(self, billetes):
        for billete in billetes:
            self.almacen_de_billetes[billete.denominacion].append(billete)
        self.contar_dinero()

    def contar_dinero(self):
        self.cantidades = {'100': self.almacen_de_billetes['100'].count(),
                           '200': self.almacen_de_billetes['200'].count(),
                           '500': self.almacen_de_billetes['500'].count(),
                           '1000': self.almacen_de_billetes['1000'].count()}
        self.valores = {'100': self.cantidades['100'] * 100,
                        '200': self.cantidades['200'] * 200,
                        '500': self.cantidades['500'] * 500,
                        '1000': self.cantidades['1000'] * 1000}
        self.valor_total = (self.valores['100'] + self.valores['200'] +
                            self.valores['500'] + self.valores['1000'])

    def extraer_dinero(self, monto):
        if monto % 100 != 0 or monto > self.valor_total:
            return "Error. Monto incorrecto"
        billetes = []
        while monto != 0:
            if monto >= 1000 and self.cantidades['1000'] > 0:
                billetes.append(self.__pop('1000'))
                monto -= 1000
            elif monto >= 500 and self.cantidades['500'] > 0:
                billetes.append(self.__pop('500'))
                monto -= 500
            elif monto >= 200 and self.cantidades['200'] > 0:
                billetes.append(self.__pop('200'))
                monto -= 200
            elif monto >= 100 and self.cantidades['100'] > 0:
                billetes.append(self.__pop('100'))
                monto -= 100
            else:
                self.agregar_dinero(billetes)
                return "Error. Monto incorrecto"
        return billetes

    def __pop(self, monto):
        self.cantidades[monto] -= 1
        self.valores[monto] -= int(monto)
        self.valor_total -= int(monto)
        return self.almacen_de_billetes[monto].pop(0)
