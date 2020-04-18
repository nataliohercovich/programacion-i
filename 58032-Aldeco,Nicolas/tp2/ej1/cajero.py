from billetes import *


class CajeroAutomatico():
    def __init__(self):
        b100 = Bill_100()
        b200 = Bill_200()
        b500 = Bill_500()
        b1000 = Bill_1000()
        self.dinero = [b100, b200, b500, b1000]

    def agregar_dinero(self):
        for bill in self.dinero:
            pass
