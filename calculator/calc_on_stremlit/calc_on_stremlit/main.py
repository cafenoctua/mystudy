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
		if len(get_items) < 3:
			if start == 0:
				return formula_items[0]
			else:
				return result
		else:
			if get_items[1] == '+':
				if start == 0:
					result = self.calc.add_int(int(get_items[0]), int(get_items[2]))
				else:
					self.calc.add_int(result, int(get_items[2]))
			elif get_items[1] == '-':
				if start == 0:
					result = self.calc.diff_int(int(get_items[0]), int(get_items[2]))
				else:
					self.calc.diff_int(result, int(get_items[2]))
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