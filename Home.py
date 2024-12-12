"""
Name: Zixian (Sammy) Bai
CS230: Section 4
Data: Volcanoes
URL: https://cs230-final-sk2jws3eebfx6pvniywl89.streamlit.app/

Description:
This program is takes the cvs data of volcanoes and presents them in different ways.
"""

import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Global Volcanoes", page_icon=":volcano:")
st.sidebar.title("\t Toggle :gear:")
country_radio = st.radio("Please select a Country: ", langs)
st.sidebar.write(country_radio)

st.title("Global Volcanoes")
path = "volcanoes.csv"
volc = pd.read_csv(path, comment="-", delimiter=",")
volc.set_index("Volcano Number", inplace=True)

st.write(volc)
