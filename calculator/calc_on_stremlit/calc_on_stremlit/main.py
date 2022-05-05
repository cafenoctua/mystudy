import string
import re
import streamlit as st
from interface.control_panel import ControlPanel
from utils.calculator import TypeCalc
from utils.formula_analysis import FormulaAnalysis

class Main(object):
	def __init__(self) -> None:
		if 'input' not in st.session_state:
			st.session_state.input = ''
		self.control_panel = ControlPanel()
		self.calc = TypeCalc()
	
	def input_panel(self) -> string:
		pushed_element = self.control_panel.base_panel()
		if pushed_element == "=":
			fa = FormulaAnalysis()
			fa_result = fa.factorization(st.session_state.input)
			st.session_state.input = ''
			return self.calculation(fa_result)
		else:
			st.session_state.input += pushed_element
	
	def calculation(self, formula_items: list, start: int = 0, end: int = 3, result = 0):
		get_items = formula_items[start:end]
		print(f"get_items: {get_items}")
		if len(get_items) < 3:
			if start == 0:
				return formula_items[0]
			else:
				return result
		else:
			if '.' in get_items[0] or '.' in get_items[2]:
				get_items[0] = float(get_items[0])
				get_items[2] = float(get_items[2])
			else:
				get_items[0] = int(get_items[0])
				get_items[2] = int(get_items[2])

			if get_items[1] == '+':
				if type(get_items[0]) == float:
					calc = self.calc.add_float
				else:
					calc = self.calc.add_int

				if start == 0:
					result = calc(get_items[0], get_items[2])
				else:
					result = self.calc.add_int(result, get_items[2])

			elif get_items[1] == '-':
				if type(get_items[0]) == float:
					calc = self.calc.diff_float
				else:
					calc = self.calc.diff_int

				if start == 0:
					result = calc(get_items[0], get_items[2])
				else:
					result = calc(result, get_items[2])

			elif get_items[1] == 'x':
				if type(get_items[0]) == float:
					calc = self.calc.multipl_float
				else:
					calc = self.calc.multipl_int

				if start == 0:
					result = calc(get_items[0], get_items[2])
				else:
					result = calc(result, get_items[2])

			elif get_items[1] == '/':
				if type(get_items[0]) == float:
					calc = self.calc.division_float
				else:
					calc = self.calc.division_int

				if start == 0:
					result = calc(get_items[0], get_items[2])
				else:
					result = calc(result, get_items[2])

			self.calculation(formula_items, start + 2, end + 2, result)
		return result

	def display(self, result) -> None:
		print(result)

if __name__ == "__main__":
	main = Main()
	# display

	# control panel
	result = main.input_panel()
	main.display(result)