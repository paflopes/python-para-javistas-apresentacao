import unittest
from src.main.conversor import ConversorDeNumeroRomano

__author__ = 'phillipe'


class ConversorNumeroRomanoTest(unittest.TestCase):
    def setUp(self):
        self.conversor = ConversorDeNumeroRomano()

    def testDeveEntenderOSimboloI(self):
        numero = self.conversor.converte("I")
        self.assertEqual(1, numero)

    def testDeveEntenderOSimboloV(self):
        numero = self.conversor.converte("V")
        self.assertEqual(5, numero)
