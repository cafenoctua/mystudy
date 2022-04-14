from sys import exit
import string
from utils.calculator import TypeCalculator

class InterfaceElement(object):
    def input_number(self) -> float:
        print('number: ', end='')
        number = input()
        self.exit_calculation(number)
        return float(number)
    
    def input_type(self) -> string:
        print('calculator type: ', end='')
        cul_type = input()
        self.exit_calculation(cul_type)
        return cul_type

    def exit_calculation(self, exit_chr: string) -> None:
        if exit_chr == 'q':
            exit()

class Interface(InterfaceElement):
    def __init__(self):
        print('***Caculator**')
        self.calculator = TypeCalculator()
    
    def interface(self) -> None:
        l = self.input_number()
        mode = self.input_type()
        r = self.input_number()

        if mode == "+":
            print(self.calculator.add_int(l, r))
        elif mode == "-":
            print(self.calculator.diff_int(l, r))
        else:
            raise "Input currect elements."

        return None
