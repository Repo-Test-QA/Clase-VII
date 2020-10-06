# Viene con Python
import unittest

# Todas mis pruebas o subconjuntos de pruebas los voy a tener en una clase.
class PruebasDeStandars(unittest.TestCase):


    # Los asserts, el objetivo es verificar algo.
    # Por tanto, determinan si la prueba falló o paso.
    # A considerar, cada prueba dentro de mi clase va a ser un Método.
    # Es por ello, que el nombre de los métodos van a empezar
    # con la palabra test.
    def test_suma(self):
        # 1er assert => assertEqual, si dos cosas son iguales.
        # Devolverme True si el resultado de la comparación son iguales.
        # Voy a comparar dos expresiones, si son iguales OK.
        # Para el ejemplo => a y b son iguales?, si es True la
        # prueba paso, si son distintos la prueba no paso.
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        # 2do assert => assertNotEqual, si dos cosas son distintas.
        # Devolverme True si el resultado de la comparación no son iguales.
        # Voy a comparar dos expresiones, si son Diferentes OK.
        # Para el ejemplo => a y b son distintas?, si es True la
        # prueba paso, si son iguales la prueba no paso.
        a = 5 + 1
        b = 8 + 20
        self.assertNotEqual(a, b)

    def test_algo_es_verdadero(self):
        # 3er assert => assertTrue, si dos cosas son True.
        # Devolverme True si el resultado de la comparación es verdadera.
        # Voy a comparar las variables, si es True OK.
        # Para el ejemplo => a == b son iguales?, si es True la
        # prueba paso, si es Falsa la prueba no paso.
        # En caso de que falle, se puede agregar otro parámetro
        # que nos indique se manera clara que ha sucedido, es decir
        # un mensaje.
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a == b, "a y b deberían ser iguales")

    def test_algo_mas_es_verdadero(self):
        # También se puede hacer esto, para no trabajar con variables,
        # aplica para los métodos anteriores también.
        self.assertTrue(2+2 == 3+1, "a y b deberían ser iguales")

    def test_algo_es_falso(self):
        # 4to assert => assertFalse, si dos cosas son Falsas.
        # Devolverme True si el resultado de la comparación es False.
        # Voy a comparar las variables, si es Diferente OK.
        # Para el ejemplo => a y b son diferentes?, si, es True la
        # prueba paso, si es Falso la prueba no paso.
        # En caso de que falle, se puede agregar otro parámetro
        # que nos indique de manera clara que ha sucedido, es decir
        # un mensaje.
        self.assertFalse(2+1 == 3+5, "El resultado de la comparación debe ser Falso")

    def test_algo_es_mayor(self):
        # A debe ser mayor que B.
        a = 5
        b = 3
        self.assertTrue(a > b)

    def test_algo_es_mayor_dos(self):
        a = 5
        b = 3
        # 5to assert => assertGreater, si  A es mayor que B.
        # Devolverme True si el resultado de la comparación es True.
        # Voy a comparar las variables, si es True OK.
        # En caso de que falle, se puede agregar otro parámetro
        # que nos indique de manera clara que ha sucedido, es decir
        # un mensaje.
        self.assertGreater(a, b, "A debe ser mayor que B")

    def test_algo_es_mayor_igual(self):
        a = 5
        b = 5
        # 6to assert => assertGreaterEqual, si  A es mayor igual que B.
        # Devolverme True si el resultado de la comparación es True.
        # Voy a comparar las variables, si es True OK.
        # En caso de que falle, se puede agregar otro parámetro
        # que nos indique de manera clara que ha sucedido, es decir
        # un mensaje.
        self.assertGreaterEqual(a, b)

    def test_algo_es_menor(self):
        a = 3
        b = 5
        # 7mo assert => assertLess, si  A es menor que B.
        # Devolverme True si el resultado de la comparación es True.
        # Voy a comparar las variables, si es True OK.
        # En caso de que falle, se puede agregar otro parámetro
        # que nos indique de manera clara que ha sucedido, es decir
        # un mensaje.
        self.assertLess(a, b)

    def test_algo_es_menor_igual(self):
        a = 5
        b = 6
        # 6to assert => assertGreaterEqual, si  A es menor igual que B.
        # Devolverme True si el resultado de la comparación es True.
        # Voy a comparar las variables, si es True OK.
        # En caso de que falle, se puede agregar otro parámetro
        # que nos indique de manera clara que ha sucedido, es decir
        # un mensaje.
        self.assertLessEqual(a, b)

    def test_comparar_listas(self):
        a = [1, 2, 'fruta']
        b = [1, 2, 'fruta']
        # Comparar dos listas y verificar si son iguales.
        self.assertListEqual(a, b)

    def test_comparar_tuplas(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        # Comparar dos tuplas y verificar si son iguales.
        self.assertTupleEqual(a, b)

    def test_comparar_diccionarios(self):
        a = {"id": 1, "nombre": "pepe", "apellido": "suarez"}
        b = {"id": 1, "nombre": "pepe", "apellido": "suarez"}
        # Comparar dos diccionarios y verificar si son iguales.
        self.assertDictEqual(a, b)





# Para ejecutar el 1er assert, lo hacemos de la siguiente manera.
# Esto es un main.
if __name__ == '__main__':
    # Las pruebas que encuentre acá, las va a ir ejecutando.
    unittest.main()


