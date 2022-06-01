import pytest
from calc_on_stremlit.utils.calculator import TypeCalc

class TestCalculation:
    calc = TypeCalc()

    def test_add_int(self):
        assert self.calc.add_int(1, 1) == 2
        assert type(self.calc.add_int(1, 1)) == int
        with pytest.raises(TypeError):
            self.calc.add_int("1", 1)
        with pytest.raises(TypeError):
            self.calc.add_int(1.1, 1)

    def test_add_float(self):
        assert self.calc.add_float(1.0, 1) == 2.0
        with pytest.raises(TypeError):
            self.calc.add_float("1", 1)

    def test_diff_int(self):
        assert self.calc.diff_int(1, 1) == 0
        assert self.calc.diff_int(1, 2) == -1
        with pytest.raises(TypeError):
            self.calc.diff_int("1", 1)
        with pytest.raises(TypeError):
            self.calc.diff_int(1.1, 1)

    def test_diff_float(self):
        assert self.calc.diff_float(1.0, 1) == 0
        assert self.calc.diff_float(1.1, 2) == (1.1 - 2)
        with pytest.raises(TypeError):
            self.calc.diff_float("1", 1)

    def test_multipl_int(self):
        assert self.calc.multipl_int(1, 1) == 1
        assert self.calc.multipl_int(1, 2) == 2
        with pytest.raises(TypeError):
            self.calc.multipl_int("1", 1)
        with pytest.raises(TypeError):
            self.calc.multipl_int(1.1, 1)

    def test_multipl_float(self):
        assert self.calc.multipl_float(1.0, 1) == 1.0
        assert self.calc.multipl_float(1.0, 2) == 2.0
        with pytest.raises(TypeError):
            self.calc.multipl_float("1", 1)

    def test_division_int(self):
        assert self.calc.division_int(1, 1) == 1
        assert self.calc.division_int(1, 2) == 0
        with pytest.raises(TypeError):
            self.calc.division_int("1", 1)
        with pytest.raises(TypeError):
            self.calc.division_int(1.1, 1)
        with pytest.raises(ZeroDivisionError):
            self.calc.division_int(1, 0)

    def test_division_float(self):
        assert self.calc.division_float(1.0, 1) == 1.0
        assert self.calc.division_float(1.0, 2) == 0.5
        with pytest.raises(TypeError):
            self.calc.division_float("1", 1)
        with pytest.raises(ZeroDivisionError):
            self.calc.division_float(1.0, 0)