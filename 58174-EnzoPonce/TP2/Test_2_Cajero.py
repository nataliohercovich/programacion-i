import unittest
from Cajero import billete, billete_100, billete_200, billete_500, billete_1000
from cajeroautomatico import Cajero_automatico
from Main import Main

class Test_Cajero_2(unittest.TestCase):
    def setUp(self):
        self.ingreso = Cajero_automatico()
        mil = billete_1000(1000,"pesos","$1000")
        quinientos = billete_500(500,"pesos","$500")
        self.list = []
        for i in range (10):
            self.list.append(mil)
            self.list.append(quinientos)
            self.list.append(quinientos)
        self.ingreso.agregar_dinero(self.list)

    def test_a(self):
        contar = self.ingreso.contar_dinero()
        self.assertEqual(contar, "\nbilletes de $1000: 10" + "\nbilletes de $500: 20" + "\nLa cantidad de dinero disponible en el cajero es de: $20000")

    def test_b(self):
        b = self.ingreso.extraer_dinero(5000,0)
        self.assertEqual(b,"5 billetes de $1000\n")

    def test_c(self):
        c = self.ingreso.extraer_dinero(12000,0)
        self.assertEqual(c,"10 billetes de $1000\n"+"4 billetes de $500\n")

    def test_d(self):
        d = self.ingreso.extraer_dinero(12100,0)
        self.assertEqual(d,"Error. No hay una combinación de billetes que nos permita extraer ese monto")

    def test_e(self):
        self.ingreso.extraer_dinero(7000, 10)
        e = self.ingreso.extraer_dinero_cambio()
        self.assertEqual(e,"2 billetes de $500\n"+"6 billetes de $1000\n")


if __name__=="__main__":
    unittest.main()
