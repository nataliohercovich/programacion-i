#!/usr/bin/python
import math


class CantidadError(Exception):
    pass


class MultiplicidadError(Exception):
    pass


class Cajero_automatico:

    def __init__(self):
        self.billetes_mil = []
        self.billetes_quinientos = []
        self.billetes_doscientos = []
        self.billetes_cien = []
        self.total = 0

    def agregar_dinero(self, lista_billetes):
        for x in lista_billetes:
            if x.denominacion == 100:
                self.billetes_cien.append(x)
            elif x.denominacion == 200:
                self.billetes_doscientos.append(x)
            elif x.denominacion == 500:
                self.billetes_quinientos.append(x)
            else:
                self.billetes_mil.append(x)

    def contar_dinero(self):
        mil = len(self.billetes_mil)
        quinientos = len(self.billetes_quinientos)
        doscientos = len(self.billetes_doscientos)
        cien = len(self.billetes_cien)
        self.total = mil * 1000 + quinientos * 500
        self.total += doscientos * 200 + cien * 100
        print("\nTenemos {} billetes de 1000\n".format(mil) +
              "Tenemos {} billetes de 500\n".format(quinientos) +
              "Tenemos {} billetes de 200\n".format(doscientos) +
              "Tenemos {} billetes de 100\n".format(cien) +
              "En total hay {}\n\n".format(self.total))

    def extraer_dinero(self, monto):
        error = False
        dar = []
        billetes = []
        dispo = [len(self.billetes_mil),
                 len(self.billetes_quinientos),
                 len(self.billetes_doscientos),
                 len(self.billetes_cien)]
        self.total = dispo[0] * 1000 + dispo[1] * 500
        self.total += dispo[2] * 200 + dispo[3] * 100
        try:
            if monto > self.total:
                raise CantidadError
        except CantidadError:
            error = True
            print("No se puede extraer esa cantidad")
        try:
            if monto % 100 != 0:
                raise MultiplicidadError
        except MultiplicidadError:
            error = True
            print("No se pueden extraer montos que no son multiplos de 100")
        lista = [1000, 500, 200, 100]
        for x in range(len(lista)):
            billetes.append(math.trunc(monto/lista[x]))
            monto = monto % lista[x]
        while not error:
            for x in range(len(lista)):
                while billetes[x] > 0:
                    if dispo[x] > 0:
                        if x == 0:
                            elem = self.billetes_mil.pop()
                            dar.append(elem)
                        elif x == 1:
                            elem = self.billetes_quinientos.pop()
                            dar.append(elem)
                        elif x == 2:
                            elem = self.billetes_doscientos.pop()
                            dar.append(elem)
                        else:
                            elem = self.billetes_cien.pop()
                            dar.append(elem)
                        billetes[x] -= 1
                        dispo[x] -= 1
                    else:
                        if x == 0 or x == 2:
                            billetes[x+1] += 2 * billetes[x]
                            billetes[x] -= 1
                        elif x == 1:
                            billetes[x+1] += 2 * billetes[x]
                            billetes[x+2] += billetes[x]
                            billetes[x] -= 1
                        else:
                            print("No hay suficientes billetes")
                            dar = []
                            error = True
                            break
                if lista[x] == 100:
                    dar = dar[::-1]
                    error = True
                else:
                    continue
        return dar
