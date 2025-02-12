import unittest
from src.calculator import sum, substract, multiply, divide

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2,3) == 5

    def test_substract(self):
        assert substract(10, 5) == 5

    def test_multiply(self):
        assert multiply(2, 5) == 10

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_divide_zero(self):
        assert divide(10, 0) == "No se puede dividir por cero"