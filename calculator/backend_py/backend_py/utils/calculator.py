class BasicCalculator(object):
    def add(self, l, r):
        return l + r
        
    def diff(self, l, r):
        return l - r

    def multiplication(self, l, r):
        return l * r

    def division(self, l, r):
        if (r > 0):
            return l / r
        else:
            raise "Can't division by 0"
    
    def quotient(self, l, r):
        if (r > 0):
            return l % r
        else:
            raise "Can't division by 0"

class TypeCalculator(BasicCalculator):
    def add_int(self, l: int, r: int) -> int:
        return int(self.add(int(l), int(r)))
    
    def diff_int(self, l: int, r: int) -> int:
        return int(self.diff(int(l), int(r)))
