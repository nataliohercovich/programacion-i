from Cajero import *

if __name__ == "__main__":
    cajero = Cajero()

    cajero.agregarDinero([
        #Total: 4400
        billete500(), billete500(), billete500()
        ])

    print(cajero.contarDinero() + "\n")
    print(cajero.extraerDinero(1200, False, 0))
    print(cajero.contarDinero())