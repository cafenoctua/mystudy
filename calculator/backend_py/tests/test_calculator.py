import pytest
from backend_py.utils.calculator import BasicCalculator

class TestCalculation:
    calculator = BasicCalculator()

    def test_add(self):
        assert self.calculator.add(1,1) == 2
        assert self.calculator.add("1", "1") != 2

    def test_diff(self):
        assert self.calculator.diff(1,1) == 0

    def test_multiplication(self):
        assert self.calculator.multiplication(1, 2) == 2
    
    def test_division(self):
        assert self.calculator.division(1, 1) == 1
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(1, 0)

    def test_quotient(self):
        assert self.calculator.quotient(1, 1) == 0
        with pytest.raises(ZeroDivisionError):
            self.calculator.quotient(1, 0)