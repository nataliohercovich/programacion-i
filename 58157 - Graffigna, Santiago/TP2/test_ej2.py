from billetes import Billete_100, Billete_200, Billete_500, Billete_1000
from ej2 import Cajero_Automatico
import unittest

class TestCajero_Automatico(unittest.TestCase):

    def setUp(self):

        self.doscientos = Billete_200()
        self.quinientos = Billete_500()
        self.mil = Billete_1000()

        self.atm_a = Cajero_Automatico()
        self.atm_b = Cajero_Automatico()
        self.atm_c = Cajero_Automatico()

        self.diezK = [self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil]
        self.veinteK = [self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos]
        self.veintitresK = [self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos]
        
        self.atm_a.agregar_billetes(self.diezK)
        self.atm_b.agregar_billetes(self.veinteK)
        self.atm_c.agregar_billetes(self.veintitresK)


    #Primer set de pruebas
    def test_contar_billetes_diezK(self):
        contar = self.atm_a.contar_billetes()
        self.assertEqual(contar, (0, 0, 0, 0, 0, 0, 10, 10000, 10000))


    def test_extraer_5K(self):
        cincomil = [self.mil, self.mil, self.mil, self.mil, self.mil]
        self.assertEqual(self.atm_a.extraer_dinero(5000), cincomil)

    def test_extraer_mas_de_lo_que_hay(self):
        no_money = self.atm_a.extraer_dinero(12000)
        self.assertEqual(no_money, ('Fondos insuficientes'))

    def test_extraer_monto_no_valido(self):
        no_multiplo = self.atm_a.extraer_dinero(5520)
        self.assertEqual(no_multiplo, ('Fondos insuficientes'))


    #Segundo set de pruebas
    def test_contar_billetes_diezK_B(self):
        contar = self.atm_b.contar_billetes()
        self.assertEqual(contar, (0, 0, 0, 0, 20, 10000, 10, 10000, 20000))

    def test_extraer_5K_B(self):
        extraer_cinco = self.atm_b.extraer_dinero(5000)
        fin = [i.denominacion for i  in extraer_cinco]
        self.assertEqual(fin, [1000, 1000, 1000, 1000, 1000])

    def test_extraer_12K_B(self):
        extraer_cinco = self.atm_b.extraer_dinero(12000)
        fin = [i.denominacion for i  in extraer_cinco]
        self.assertEqual(fin, [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 500, 500, 500, 500])

    def test_extraer_monto_no_valido_B(self):
        no_money = self.atm_b.extraer_dinero(12100)
        self.assertEqual(no_money, ('Fondos insuficientes'))

    #def test_extraer_con_10_cambio_B(self):
    #    change = self.atm_b.extraer_dinero_cambio(7000, 10)
    #    fin = [i.denominacion for i  in change]
    #    self.assertEqual(fin, [500, 500, 1000, 1000, 1000, 1000, 1000, 1000])


    #Tercer set de pruebas
    def test_contar_billetes_C(self):
        money = self.atm_c.contar_billetes()
        self.assertEqual(money, (0, 0, 15, 3000, 20, 10000, 10, 10000, 23000))
        (0, 0, 15, 3000, 20, 10000, 10, 10000, 23000)

    def test_extraer_C(self):
        extraer_cinco = self.atm_c.extraer_dinero(5000)
        fin = [i.denominacion for i in extraer_cinco]
        self.assertEqual(fin, [1000, 1000, 1000, 1000, 1000])
        

if __name__ == "__main__":
    unittest.main()