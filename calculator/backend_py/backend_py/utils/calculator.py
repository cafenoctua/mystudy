class BasicCalculator(object):
    def add(self, l, r):
        return l + r
        
    def diff(self, l, r):
        return l - r

    def multiplication(self, l, r):
        return l * r

    def division(self, l, r):
        try:
            return l / r
        except ZeroDivisionError:
            print("Can't division by 0")
            raise
    
    def quotient(self, l, r):
        try:
            return l % r
        except ZeroDivisionError:
            print("Can't division by 0")
            raise

class TypeCalculator(BasicCalculator):
    def add_int(self, l: int, r: int) -> int:
        return int(self.add(int(l), int(r)))
    
    def diff_int(self, l: int, r: int) -> int:
        return int(self.diff(int(l), int(r)))
