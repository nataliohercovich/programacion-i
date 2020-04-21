#!/usr/bin/python
import math


class CantidadError(Exception):
    pass


class MultiplicidadError(Exception):
    pass


class PorcentajeError(Exception):
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

    def extraer_dinero_cambio(self, monto, porc):
        try:
            if porc > 100 or porc < 0:
                raise PorcentajeError
        except PorcentajeError:
            return "Error. El porcentaje es incorrecto"
        porc = math.trunc(monto * porc / 100)
        sacar = porc
        sacar = str(sacar)[::-1]
        if len(sacar) <= 2:
            sacar = 100
        else:
            sacar = sacar[::-1][:2]
            sacar = (int(sacar[::-1]) + 1) * 100
        if sacar - porc >= 100 or sacar - porc <= 0:
            sacar = porc
        dar = [0, 0, 0, 0]
        suma = 0
        billetes = [math.trunc(sacar / 100), 0, 0, 0]
        dispo = [len(self.billetes_cien),
                 len(self.billetes_doscientos),
                 len(self.billetes_quinientos),
                 len(self.billetes_mil)]
        self.total = dispo[0] * 100 + dispo[1] * 200
        self.total += dispo[2] * 500 + dispo[3] * 1000
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
        lista = [100, 200, 500, 1000]
        for x in range(len(lista)):
            while billetes[x] > 0 and suma <= sacar:
                if dispo[x] > 0:
                    if x == 3:
                        self.billetes_mil.pop()
                    elif x == 2:
                        self.billetes_quinientos.pop()
                    elif x == 1:
                        self.billetes_doscientos.pop()
                    else:
                        self.billetes_cien.pop()
                    dar[x] += 1
                    dispo[x] -= 1
                    billetes[x] -= 1
                else:
                    try:
                        if x < 3:
                            billetes[x+1] += billetes[x]
                        else:
                            raise BilleteError
                        billetes[x] = 0
                    except BilleteError:
                        return ("Error. No hay una combinación de" +
                                " billetes que nos permita extraer " +
                                "ese monto")
                suma = 0
                for i in range(4):
                    suma += dar[i] * lista[i]
        texto1 = self.extraer_dinero(monto - suma)
        for x in texto1.strip("\n").split("\n"):
            renglon = x.split(" ")
            if renglon[-1] == "$1000":
                dar[3] += int(renglon[0])
            elif renglon[-1] == "$500":
                dar[2] += int(renglon[0])
            elif renglon[-1] == "$200":
                dar[1] += int(renglon[0])
            else:
                dar[0] += int(renglon[0])
        texto = ""
        for x in range(4):
            if dar[x] != 0:
                texto += "{} billetes de ${}\n".format(dar[x], lista[x])
        return texto
