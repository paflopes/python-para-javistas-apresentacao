import unittest
from src.main.conversor import ConversorDeNumeroRomano

__author__ = 'phillipe'


class ConversorNumeroRomanoTest(unittest.TestCase):

    def testDeveEntenderOSimboloI(self):
        conversor = ConversorDeNumeroRomano()
        numero = conversor.converte("I")
        self.assertEqual(1, numero)