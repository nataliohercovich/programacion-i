from Cajero import *
import unittest

class TestSudoku(unittest.TestCase):
    
    def test_cargo1(self):
        cajero = Cajero()
        cajero.agregarDinero([
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000()
        ])

        self.assertAlmostEqual(cajero.contarDinero(), "Hay 0 billetes de 100\nHay 0 billetes de 200\nHay 0 billetes de 500\nHay 10 billetes de 1000\nTotal: 10000")
        self.assertAlmostEqual(cajero.extraerDinero(5000), ['$1000', '$1000', '$1000', '$1000','$1000'])
        self.assertAlmostEqual(cajero.extraerDinero(12000), "No hay suficientes fondos")
        self.assertAlmostEqual(cajero.extraerDinero(4520), "El monto no es multiplo de 100")


if __name__ == "__main__":
    unittest.main()
