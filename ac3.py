import abc
from unittest2 import TestCase, main


class Operador:
    @abc.abstractclassmethod
    def executar(self, valor1, valor2):
        ...


class Soma:
    def executar(self, valor1, valor2):
        return valor1 + valor2


class Divisao:
    def executar(self, valor1, valor2):
        return valor1 / valor2


class Subtracao:
    def executar(self, valor1, valor2):
        return valor1 - valor2


class Multiplicacao:
    def executar(self, valor1, valor2):
        return valor1 * valor2


class OperacaoFabrica:
    def criar(self, operador):
        if operador == "soma":
            return Soma()
        elif operador == "subtracao":
            return Subtracao()
        elif operador == "divisao":
            return Divisao()
        elif operador == "multiplicacao":
            return Multiplicacao()


class Calculadora:
    def calcular(self, valor1, valor2, operador):
        operacao = OperacaoFabrica().criar(operador=operador)
        if not operacao:
            return 0
        return operacao.executar(valor1, valor2)


class Tests(TestCase):
    calculadora = Calculadora()

    def test_soma(self):
        result = self.calculadora.calcular(3, 5, "soma")
        self.assertEqual(result, 8, msg="Test OK")

    def test_subtracao(self):
        result = self.calculadora.calcular(5, 1, "subtracao")
        self.assertEqual(result, 4, msg="Test OK")

    def test_divisao(self):
        result = self.calculadora.calcular(10, 2, "divisao")
        self.assertEqual(result, 5, msg="Test OK")

    def test_multiplicacao(self):
        result = self.calculadora.calcular(2, 8, "multiplicacao")
        self.assertEqual(result, 16, msg="Test OK")


if __name__ == "__main__":
    main()
