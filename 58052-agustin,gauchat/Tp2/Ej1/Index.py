from Cajero import *

if __name__ == "__main__":
    cajero = Cajero()

    cajero.agregarDinero([
        #Total: 7400
        billete1000(), billete1000(),
        billete500(), billete500(), billete500(),
        billete200(), billete200(),
        billete100(), billete100(), billete100(), billete100(), billete100()
        ])

    print(cajero.extraerDinero(1200))
    print(cajero.contarDinero())