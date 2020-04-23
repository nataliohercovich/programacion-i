from Cajero_automatico import Cajero_automatico
import Billete as B
import unittest
from parameterized import parameterized


class Test_cajero(unittest.TestCase):
    def setUp(self):
        self.cajero = Cajero_automatico()
        self.billetes = []

    @parameterized.expand([
        ((0, 0, 0, 10), (0, 0, 0, 10000)),
        ((0, 0, 20, 10), (0, 0, 10000, 10000)),
        ((0, 15, 20, 10), (0, 3000, 10000, 10000))
    ])
    def test_contar_a(self, cantidades_iniciales, valores_parciales):
        # set up
        billetes_de_100 = cantidades_iniciales[0]
        billetes_de_200 = cantidades_iniciales[1]
        billetes_de_500 = cantidades_iniciales[2]
        billetes_de_1000 = cantidades_iniciales[3]
        for _ in range(billetes_de_100):
            billete = B.Billete_de_100()
            self.billetes.append(billete)
        for _ in range(billetes_de_200):
            billete = B.Billete_de_200()
            self.billetes.append(billete)
        for _ in range(billetes_de_500):
            billete = B.Billete_de_500()
            self.billetes.append(billete)
        for _ in range(billetes_de_1000):
            billete = B.Billete_de_1000()
            self.billetes.append(billete)
        self.cajero.agregar_dinero(self.billetes)

        # contar
        for idx, tipo_billete in enumerate(['100', '200', '500', '1000']):
            self.assertEqual(self.cajero.valores[tipo_billete],
                             valores_parciales[idx])
        self.assertEqual(self.cajero.valor_total, sum(valores_parciales))

    @parameterized.expand([
        ((0, 0, 0, 10), 5000, [0, 0, 0, 5]),
        ((0, 0, 20, 10), 5000, [0, 0, 0, 5]),
        ((0, 15, 20, 10), 5000, [0, 0, 0, 5])
    ])
    def test_extraccion_b(self, cantidades_iniciales,
                          monto_extraer, ext_esperado):
        # set up
        billetes_de_100 = cantidades_iniciales[0]
        billetes_de_200 = cantidades_iniciales[1]
        billetes_de_500 = cantidades_iniciales[2]
        billetes_de_1000 = cantidades_iniciales[3]
        for _ in range(billetes_de_100):
            billete = B.Billete_de_100()
            self.billetes.append(billete)
        for _ in range(billetes_de_200):
            billete = B.Billete_de_200()
            self.billetes.append(billete)
        for _ in range(billetes_de_500):
            billete = B.Billete_de_500()
            self.billetes.append(billete)
        for _ in range(billetes_de_1000):
            billete = B.Billete_de_1000()
            self.billetes.append(billete)
        self.cajero.agregar_dinero(self.billetes)

        # extraer
        extraccion = [0, 0, 0, 0]
        billetes_ext = self.cajero.extraer_dinero(monto_extraer)
        try:
            for billete in billetes_ext:
                if billete.denominacion == '100':
                    extraccion[0] += 1
                if billete.denominacion == '200':
                    extraccion[1] += 1
                if billete.denominacion == '500':
                    extraccion[2] += 1
                if billete.denominacion == '1000':
                    extraccion[3] += 1
        except AttributeError:
            extraccion = billetes_ext
        self.assertEqual(extraccion, ext_esperado)

    @parameterized.expand([
        ((0, 0, 0, 10), 12000, "Error. Quiero sacar mas dinero de lo que puedo"),
        ((0, 0, 20, 10), 12000, [0, 0, 4, 10]),
        ((0, 15, 20, 10), 12000, [0, 0, 4, 10])
    ])
    def test_extraccion_c(self, cantidades_iniciales,
                          monto_extraer, ext_esperado):
        # set up
        billetes_de_100 = cantidades_iniciales[0]
        billetes_de_200 = cantidades_iniciales[1]
        billetes_de_500 = cantidades_iniciales[2]
        billetes_de_1000 = cantidades_iniciales[3]
        for _ in range(billetes_de_100):
            billete = B.Billete_de_100()
            self.billetes.append(billete)
        for _ in range(billetes_de_200):
            billete = B.Billete_de_200()
            self.billetes.append(billete)
        for _ in range(billetes_de_500):
            billete = B.Billete_de_500()
            self.billetes.append(billete)
        for _ in range(billetes_de_1000):
            billete = B.Billete_de_1000()
            self.billetes.append(billete)
        self.cajero.agregar_dinero(self.billetes)
        # extraer
        extraccion = [0, 0, 0, 0]
        billetes_ext = self.cajero.extraer_dinero(monto_extraer)
        try:
            for billete in billetes_ext:
                if billete.denominacion == '100':
                    extraccion[0] += 1
                if billete.denominacion == '200':
                    extraccion[1] += 1
                if billete.denominacion == '500':
                    extraccion[2] += 1
                if billete.denominacion == '1000':
                    extraccion[3] += 1
        except AttributeError:
            extraccion = billetes_ext
        self.assertEqual(extraccion, ext_esperado)

    @parameterized.expand([
        ((0, 0, 0, 10), 5520, "Error. El monto es incorrecto"),
        ((0, 0, 20, 10), 12100, "Error. No hay una combinacion de billetes que nos permita extraer ese monto"),
        ((0, 15, 20, 10), 12100, "Error. No hay una combinacion de billetes que nos permita extraer ese monto")
    ])
    def test_extraccion_d(self, cantidades_iniciales,
                          monto_extraer, ext_esperado):
        # set up
        billetes_de_100 = cantidades_iniciales[0]
        billetes_de_200 = cantidades_iniciales[1]
        billetes_de_500 = cantidades_iniciales[2]
        billetes_de_1000 = cantidades_iniciales[3]
        for _ in range(billetes_de_100):
            billete = B.Billete_de_100()
            self.billetes.append(billete)
        for _ in range(billetes_de_200):
            billete = B.Billete_de_200()
            self.billetes.append(billete)
        for _ in range(billetes_de_500):
            billete = B.Billete_de_500()
            self.billetes.append(billete)
        for _ in range(billetes_de_1000):
            billete = B.Billete_de_1000()
            self.billetes.append(billete)
        self.cajero.agregar_dinero(self.billetes)
        # extraer
        extraccion = [0, 0, 0, 0]
        billetes_ext = self.cajero.extraer_dinero(monto_extraer)
        try:
            for billete in billetes_ext:
                if billete.denominacion == '100':
                    extraccion[0] += 1
                if billete.denominacion == '200':
                    extraccion[1] += 1
                if billete.denominacion == '500':
                    extraccion[2] += 1
                if billete.denominacion == '1000':
                    extraccion[3] += 1
        except AttributeError:
            extraccion = billetes_ext
        self.assertEqual(extraccion, ext_esperado)

    @parameterized.expand([
        ((0, 0, 20, 10), 7000, 10, [0, 0, 2, 6]),
        ((0, 15, 20, 10), 7000, 10, [0, 5, 0, 6])
    ])
    def test_extraer_e(self, cantidades_iniciales, monto_extraer,
                       cambio, ext_esperado):
        # set up
        billetes_de_100 = cantidades_iniciales[0]
        billetes_de_200 = cantidades_iniciales[1]
        billetes_de_500 = cantidades_iniciales[2]
        billetes_de_1000 = cantidades_iniciales[3]
        for _ in range(billetes_de_100):
            billete = B.Billete_de_100()
            self.billetes.append(billete)
        for _ in range(billetes_de_200):
            billete = B.Billete_de_200()
            self.billetes.append(billete)
        for _ in range(billetes_de_500):
            billete = B.Billete_de_500()
            self.billetes.append(billete)
        for _ in range(billetes_de_1000):
            billete = B.Billete_de_1000()
            self.billetes.append(billete)
        self.cajero.agregar_dinero(self.billetes)
        # extraer
        extraccion = [0, 0, 0, 0]
        billetes_ext = self.cajero.extraer_dinero_cambio(monto_extraer, cambio)
        try:
            for billete in billetes_ext:
                if billete.denominacion == "100":
                    extraccion[0] += 1
                if billete.denominacion == '200':
                    extraccion[1] += 1
                if billete.denominacion == '500':
                    extraccion[2] += 1
                if billete.denominacion == '1000':
                    extraccion[3] += 1
        except AttributeError:
            extraccion = billetes_ext
        self.assertEqual(extraccion, ext_esperado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
