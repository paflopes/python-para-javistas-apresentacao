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
        acumulador = 0
        ultimo_vizinho_da_direita = 0

        for letra in reversed(numero):
            # pega o inteiro referente ao simbolo atual
            atual = self.tabela[letra]

            # se o da direita for menor, o multiplicaremos
            # por -1 para torná-lo negativo
            multiplicador = 1
            if atual < ultimo_vizinho_da_direita:
                multiplicador = -1

            acumulador += atual * multiplicador

            # atualiza o vizinho da direita
            ultimo_vizinho_da_direita = atual

        return acumulador