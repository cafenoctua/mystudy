import pytest
from calc_on_stremlit.utils.calculator import TypeClac

class TestCalculation:
    calc = TypeClac()

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
        
