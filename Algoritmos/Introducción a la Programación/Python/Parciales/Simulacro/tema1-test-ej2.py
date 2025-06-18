import unittest
from solucion import maxima_cantidad_primos

class Ej2Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        self.method = maxima_cantidad_primos


    def test_matriz_con_un_primo(self):
        entrada = [[2]]
        entrada_copia = entrada.copy()
        salida_esperada = 1
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)
    
    def test_matriz_con_un_no_primo(self):
        entrada = [[4]]
        entrada_copia = entrada.copy()
        salida_esperada = 0
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_matriz_cuadrada(self):
        entrada = [[1, 2], 
                   [1, 2]]
        entrada_copia = entrada.copy()
        salida_esperada = 2
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_columnas_con_distinta_longitud_que_fila(self):
        entrada = [[1, 2, 3], 
                   [1, 1, 1]]
        entrada_copia = entrada.copy()
        salida_esperada = 1
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_unica_columna(self):
        entrada = [[1],
                   [2],
                   [3], 
                   [121]]
        entrada_copia = entrada.copy()
        salida_esperada = 2
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_unica_fila_con_primos(self):
        entrada = [[4, 6, 7, 14, 121, 5]]
        entrada_copia = entrada.copy()
        salida_esperada = 1
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)
        
    def test_unica_fila_sin_primos(self):
        entrada = [[4, 6, 8, 14, 9, 21]]
        entrada_copia = entrada.copy()
        salida_esperada = 0
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_negativos(self):
        entrada = [[-2, 4, 5], 
                   [-5, 3, 2], 
                   [-7, 1, 1]]
        entrada_copia = entrada.copy()
        salida_esperada = 2
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_max_primos_en_el_medio(self):
        entrada = [[1, 2, 3, 4], 
                   [6, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [5, 14, 13, 16],
                   [0, 0, 0, 0]]
        entrada_copia = entrada.copy()
        salida_esperada = 4
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)
        
    def test_max_primos_en_el_medio_en_2_columas(self):
        entrada = [[1, 2, 3, 4], 
                   [6, 6, 7, 8], 
                   [9, 7, 11, 12], 
                   [5, 14, 12, 16],
                   [0, 19, 0, 0]]
        entrada_copia = entrada.copy()
        salida_esperada = 3
        self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

if __name__ == '__main__':
    unittest.main(verbosity=2)