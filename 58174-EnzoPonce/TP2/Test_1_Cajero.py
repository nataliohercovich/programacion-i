import unittest
from Cajero import billete, billete_100, billete_200, billete_500, billete_1000
from cajeroautomatico import Cajero_automatico
from Main import Main

class Test_Cajero1(unittest.TestCase):
    def setUp(self):
        self.ingreso = Cajero_automatico()
        mil = billete_1000(1000,"pesos","$1000")
        self.ingreso.agregar_dinero([mil, mil,mil,
                                     mil, mil,mil,
                                     mil, mil,mil,mil])


    #TEST 1:
    def test_a(self):
        self.contar = self.ingreso.contar_dinero()
        self.assertEqual(self.contar,"\nbilletes de $1000: 10"+"\nLa cantidad de dinero disponible en el cajero es de: $10000")

    def test_b(self):
        b = self.ingreso.extraer_dinero(5000,0)
        self.assertEqual(b,"5 billetes de $1000\n")

    def test_c(self):
        c = self.ingreso.extraer_dinero(12000,0)
        self.assertEqual(c,"Error.Debe retirar un monto menor al que hay en el cajero")
    
    def test_d(self):
        d =  self.ingreso.extraer_dinero(5520,0)
        self.assertEqual(d,"Error.El monto es incorrecto")

        
        


  
if __name__=="__main__":
    unittest.main()
