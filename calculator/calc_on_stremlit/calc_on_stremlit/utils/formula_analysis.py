import re

class FormulaAnalysis(object):
    def __init__(self) -> None:
        self.results = []

    def factorization(self, formula, results = []) -> list:
        result = re.search(r'[\+, \-, x, /]+', formula)
        if result is None:
            if self.results is None:
                return list(formula)
            self.results.append(formula)
            return self.results
        left_equation_item = formula[:result.start()]
        operator = formula[result.start()]
        right_equation_item = formula[result.end():]
        self.results.append(left_equation_item)
        self.results.append(operator)
        self.factorization(right_equation_item, self.results)
        return self.results