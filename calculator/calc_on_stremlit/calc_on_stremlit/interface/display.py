import streamlit as st
from typing import Union

Number = Union[int, float] 

class Display(object):
    def display_result(self, result) -> None:
        st.write(f'Result: {result}')