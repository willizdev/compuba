import unittest
from solucion import resolver_cuenta

class Ej4Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej4Test, self).__init__(*args, **kwargs)
        self.method = resolver_cuenta

    def test_cuenta_comienza_con_caracter_negativo(self):
        result = resolver_cuenta('-1.1')
        self.assertAlmostEqual(result, -1.1)

    def test_cuenta_comienza_con_caracter_positivo(self):
        result = resolver_cuenta('+1.17')
        self.assertAlmostEqual(result, 1.17)

    def test_cuenta_comienza_con_digito(self):
        result = resolver_cuenta('4')
        self.assertAlmostEqual(result, 4.0)

    def test_cuenta_con_operacion_punto_con_multiple_digitos(self):
        result = resolver_cuenta('0.00007+1')
        self.assertAlmostEqual(result, 1.00007)

    def test_cuenta_resultado_positivo(self):
        result = resolver_cuenta('-10+15.5-23.5+23.4')
        self.assertAlmostEqual(result, 5.4)

    def test_cuenta_resultado_negativo(self):
        result = resolver_cuenta('+30-100+120.03-1000')
        self.assertAlmostEqual(result, -949.97)

    def test_cuenta_solo_sumas(self):
        result = resolver_cuenta('50+50+100')
        self.assertAlmostEqual(result, 200)
    
    def test_cuenta_solo_sumas_decimales(self):
        result = resolver_cuenta('50.25+50.255+100.277')
        self.assertAlmostEqual(result, 200.78199999999998)
    
    def test_cuenta_solo_restas(self):
        result = resolver_cuenta('-5010-90-900')
        self.assertAlmostEqual(result, -6000)

    def test_cuenta_solo_restas_decimales(self):
        result = resolver_cuenta('-500.12309-1250.5430-78894.4331')
        resultado_esperado = -80645.09919
        self.assertAlmostEqual(result, resultado_esperado)
if __name__ == '__main__':
    unittest.main(verbosity=2)