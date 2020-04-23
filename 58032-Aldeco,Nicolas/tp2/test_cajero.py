import unittest
from cajero import *


# Solo billetes de $1000
class TestCajero1(unittest.TestCase):

    def setUp(self):
        self.value = CajeroAutomatico()
        self.value.agregar_dinero([
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
        ])
        self.value.contar_dinero()
    
    def test_contar_dinero(self):
        value = self.value.get_billetes_parciales()
        self.assertEqual(value,
        [['$100',0],['$200',0],['$500',0],['$1000',10000]])
    
    def test_total_dinero(self):
        total = self.value.get_total_dinero()
        self.assertEqual(total, 10000)

    def test_extraer_5000(self):
        self.value.extraer_dinero(5000)
        temp = self.value.cant_billetes[0][1]
        self.assertEqual(temp, 5)

    def test_error_more_money(self):
        with self.assertRaises(Exception) as context:
            self.value.extraer_dinero(12000)
        self.assertTrue(
            'El cajero solo tiene : 10000 y usted quiere retirar : 12000' in str(context.exception)
        )

    def test_error_not_m100(self):
        with self.assertRaises(Exception) as context:
            self.value.extraer_dinero(5520)
        self.assertTrue(
            'El monto solicitado no es multiplo de 100' in str(context.exception)
        )

# 10 billetes de $1000, 20 billetes de $500.
class TestCajero2(unittest.TestCase):

    def setUp(self):
        self.value = CajeroAutomatico()
        self.value.agregar_dinero([
            Bill_1000(),Bill_1000(),Bill_1000(),Bill_1000(),Bill_1000(),
            Bill_1000(),Bill_1000(),Bill_1000(),Bill_1000(),Bill_1000(),
            Bill_500(),Bill_500(),Bill_500(),Bill_500(),Bill_500(),
            Bill_500(),Bill_500(),Bill_500(),Bill_500(),Bill_500(),
            Bill_500(),Bill_500(),Bill_500(),Bill_500(),Bill_500(),
            Bill_500(),Bill_500(),Bill_500(),Bill_500(),Bill_500()
        ])
        self.value.contar_dinero()

    # def test_contar_dinero(self):



if __name__ == "__main__":
    unittest.main()
