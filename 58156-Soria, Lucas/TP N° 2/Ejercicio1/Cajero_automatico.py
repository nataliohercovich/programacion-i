#!/usr/bin/python
import math


class CantidadError(Exception):
    pass


class MultiplicidadError(Exception):
    pass


class BilleteError(Exception):
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
        billetes = [len(self.billetes_mil), len(self.billetes_quinientos),
                    len(self.billetes_doscientos), len(self.billetes_cien)]
        parcial = [1000 * billetes[0], 500 * billetes[1],
                   200 * billetes[2], 100 * billetes[3]]
        texto = ""
        for x in range(len(billetes)):
            if billetes[x] != 0:
                texto += "{} billetes de ".format(billetes[x])
                if x == 0:
                    valor = 1000
                elif x == 1:
                    valor = 500
                elif x == 2:
                    valor = 200
                else:
                    valor = 100
                texto += "${}, ".format(valor)
                texto += "parcial ${}\n".format(parcial[x])
        texto += "Total: ${}".format(sum(i for i in parcial))
        return texto

    def extraer_dinero(self, monto):
        dar = [0, 0, 0, 0]
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
            return "Error. Quiero sacar mas dinero de lo que puedo"
        try:
            if monto % 100 != 0:
                raise MultiplicidadError
        except MultiplicidadError:
            return "Error. El monto es incorrecto"
        lista = [1000, 500, 200, 100]
        for x in range(len(lista)):
            billetes.append(math.trunc(monto/lista[x]))
            monto = monto % lista[x]
        for x in range(len(lista)):
            while billetes[x] > 0:
                if dispo[x] > 0:
                    if x == 0:
                        self.billetes_mil.pop()
                    elif x == 1:
                        self.billetes_quinientos.pop()
                    elif x == 2:
                        self.billetes_doscientos.pop()
                    else:
                        self.billetes_cien.pop()
                    dar[x] += 1
                    dispo[x] -= 1
                    billetes[x] -= 1
                else:
                    try:
                        if x == 0 or x == 2:
                            billetes[x+1] += 2 * billetes[x]
                        elif x == 1:
                            billetes[x+1] += 2 * billetes[x]
                            billetes[x+2] += billetes[x]
                        else:
                            raise BilleteError
                        billetes[x] = 0
                    except BilleteError:
                        return ("Error. No hay una combinación de" +
                                " billetes que nos permita extraer " +
                                "ese monto")
        texto = ""
        for x in range(4):
            if dar[x] != 0:
                texto += "{} billetes de ${}\n".format(dar[x], lista[x])
        return texto
