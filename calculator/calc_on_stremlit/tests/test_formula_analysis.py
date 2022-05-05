from calc_on_stremlit.utils.formula_analysis import FormulaAnalysis

class TestFormulaAnalysis:
    def test_basic(self):
        fa = FormulaAnalysis()
        assert fa.factorization("11+1") == ['11', '+', '1']
        fa = FormulaAnalysis()
        assert fa.factorization("11+2-3x4/5") == ['11', '+', '2', '-', '3', 'x', '4', '/', '5']
        fa = FormulaAnalysis()
        assert fa.factorization("1.1+1") == ['1.1', '+', '1']