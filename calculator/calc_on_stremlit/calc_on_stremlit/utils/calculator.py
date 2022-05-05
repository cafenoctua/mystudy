from typing import Union

Number = Union[int, float]

class BasicCalc(object):

    def _add(self, left, right):
        return left + right
    
    def diff(self, left, right):
        return left - right

    def multipl(self, left, right):
        return left * right
    
    def division(self, left, right):
        return left / right

class TypeCalc(BasicCalc):
    
    def int_check(self, value):
        return True if type(value) == int else False
    
    def float_check(self, value):
        return True if type(value) == float else False
        
    def add_int(self, left: int, right: int) -> int:
        if self.int_check(left) and self.int_check(right):
            return self._add(left, right)
        else:
            raise TypeError

    def add_float(self, left: Number, right: Number) -> float:
        if (self.int_check(left) or self.float_check(left)) and (self.int_check(right) or self.float_check(right)):
            return self._add(left, right)
        else:
            raise TypeError

    def diff_int(self, left: int, right: int) -> int:
        if self.int_check(left) and self.int_check(right):
            return self.diff(left, right)
        else:
            raise TypeError

    def diff_float(self, left: Number, right: Number) -> float:
        if (self.int_check(left) or self.float_check(left)) and (self.int_check(right) or self.float_check(right)):
            return self.diff(left, right)
        else:
            raise TypeError

    def multipl_int(self, left: int, right: int) -> int:
        if self.int_check(left) and self.int_check(right):
            return self.multipl(left, right)
        else:
            raise TypeError

    def multipl_float(self, left: Number, right: Number) -> float:
        if (self.int_check(left) or self.float_check(left)) and (self.int_check(right) or self.float_check(right)):
            return self.multipl(left, right)
        else:
            raise TypeError

    def division_int(self, left: int, right: int) -> int:
        if self.int_check(left) and self.int_check(right) and right != 0:
            return int(self.division(left, right))
        elif right == 0:
            raise ZeroDivisionError
        else:
            raise TypeError

    def division_float(self, left: Number, right: Number) -> float:
        if (self.int_check(left) or self.float_check(left)) and (self.int_check(right) or self.float_check(right)) and right != 0:
            return self.division(left, right)
        elif right == 0:
            raise ZeroDivisionError
        else:
            raise TypeError