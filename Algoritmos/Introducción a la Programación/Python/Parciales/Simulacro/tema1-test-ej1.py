import unittest
from solucion import maximas_cantidades_consecutivos

class Ej1Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = maximas_cantidades_consecutivos

    def test_sec_vacia(self):
        entrada = []
        entrada_copia = entrada.copy()
        self.assertEqual(maximas_cantidades_consecutivos(entrada), {})
        self.assertEqual(entrada, entrada_copia)

    def test_todos_aparecen_una_sola_vez(self):
        entrada = list(range(0, 10))
        entrada_copia = entrada.copy()
        salida_esperada = {0:1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        # self.assertEqual(entrada, entrada_copia)

    def test_un_unico_elemento(self):
        entrada = [1]*20
        entrada_copia = entrada.copy()
        salida_esperada = {1: 20}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        # self.assertEqual(entrada, entrada_copia)

    def test_maxima_aparicion_al_final(self):
        entrada = [1, 1, 1, 2, 1, 1, 1, 1]
        entrada_copia = entrada.copy()
        salida_esperada = {1: 4, 2: 1}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        # self.assertEqual(entrada, entrada_copia)

    def test_maxima_aparicion_al_medio(self):
        entrada = [1, 1, 1, 97, 1, 1, 1, 1, 54, 54, 101]
        entrada_copia = entrada.copy()
        salida_esperada = {1: 4, 54: 2, 97: 1, 101: 1}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_maxima_aparicion_al_inicio(self):
        entrada = [30, 30, 30, 30, 2, 30, 30, 30]
        entrada_copia = entrada.copy()
        salida_esperada = {30: 4, 2: 1}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_multiples_sec_con_igual_longitud(self):
        entrada = [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2]
        entrada_copia = entrada.copy()
        salida_esperada = {1: 4, 2: 2}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_numeros_negativos(self):
        entrada = [-1, -2, -2, -3, -3, -1, -1]
        entrada_copia = entrada.copy()
        salida_esperada = {-1: 2, -2: 2, -3: 2}
        self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

if __name__ == '__main__':
    unittest.main(verbosity=2)