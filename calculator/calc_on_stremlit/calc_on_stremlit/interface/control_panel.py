import string
import streamlit as st

class ControlPanel(object):
    def base_panel_elements(self, col: object, num_elements: list) -> string:
        pushed_num = ""
        with col:
            for num_element in num_elements:
                if st.button(num_element):
                    pushed_num = num_element
        return pushed_num

    def base_panel(self) -> string:
        # define panel elements
        cols = st.columns(4)
        num_elements_list = [
            ["7", "4", "1", "0"],
            ["8", "5", "2", "."],
            ["9", "6", "3", "="],
            ["/", "x", "-", "+"]
            ]

        # make panel elements
        pushed_num = ""
        for col, num_elements in zip(cols, num_elements_list):
            num = self.base_panel_elements(col, num_elements)
            if num != "":
                pushed_num = num
        return pushed_num