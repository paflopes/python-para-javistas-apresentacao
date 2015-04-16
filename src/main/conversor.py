__author__ = 'phillipe'


class ConversorDeNumeroRomano:

    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def converte(self, numero):
        return self.tabela.get(numero)