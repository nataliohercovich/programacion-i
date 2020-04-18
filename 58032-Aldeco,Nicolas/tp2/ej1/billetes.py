#!/bin/usr/python3
# Billetes
class Billete():
    def __init__(self):
        self.denominacion = None
        self.moneda = None
        self.representacion = None


class Bill_100(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.denominacion = 100
        self.moneda = 'pesos'
        self.representacion = '$100'

class Bill_200(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.denominacion = 200
        self.moneda = 'pesos'
        self.representacion = '$200'


class Bill_500(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.denominacion = 500
        self.moneda = 'pesos'
        self.representacion = '$500'


class Bill_1000(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.denominacion = 100
        self.moneda = 'pesos'
        self.representacion = '$100'