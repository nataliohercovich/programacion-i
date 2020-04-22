class Cajero():

    def __init__(self):
        self.dinero = {}

    def agregar_dinero(self, lista_billetes):

        lista_billetes.sort(key=lambda valor: valor.getDenominacion(),
                            reverse=True)

        for item in lista_billetes:

            moneda = item.getMoneda()

            if moneda in self.dinero.keys():
                self.dinero[moneda].append(item)

            else:
                self.dinero[moneda] = []
                self.dinero[moneda].append(item)

    def contar_dinero(self):
        contado = {}
        for keys in self.dinero.keys():
            subtotales = {}
            total = 0

            for billete in self.dinero[keys]:

                valor = billete.getDenominacion()
                total += valor

                if valor in subtotales.keys():
                    subtotales[valor] += valor
                else:
                    subtotales[valor] = valor

            contado[keys] = (subtotales, total)

        return contado

    def extraer_dinero(self, monto):
        total = self.contar_dinero()["pesos"][1]

        extraction = []

        if monto > total or monto % 100 != 0:
            raise Exception

        for billete in self.dinero["pesos"]:
            denominacion = billete.getDenominacion()

            if monto/denominacion >= 1:
                extraction.append(billete)
                monto -= denominacion

        for item in extraction:
            self.dinero["pesos"].remove(item)

        return extraction, self.dinero["pesos"]


"""
from billetes import Billete100
from billetes import Billete200
from billetes import Billete500
from billetes import Billete1000

aa = Cajero()

b1 = Billete100()
b2 = Billete200()
b3 = Billete500()
b4 = Billete1000()
b5 = Billete200()

billetera = [b1, b2, b3, b4, b5]

aa.agregar_dinero(billetera)
# ------------------------------
print("Dinero en el cajero:")
for i in aa.dinero["pesos"]:
    print(i.getRepresentacion())
print("\n\n")
# ------------------------------
print(aa.contar_dinero())
print("\n\n")
# ------------------------------
x = aa.extraer_dinero(400)

print("Dinero extraido:")
for i in x[0]:
    print(i.getRepresentacion())

print("\n\nDinero en el cajero:")

for i in x[1]:
    print(i.getRepresentacion())
"""
