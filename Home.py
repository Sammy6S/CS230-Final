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

st.title("Global Volcanoes")
path = "volcanoes.csv"
volc = pd.read_csv(path, delimiter=",", comment="%")
volc.set_index("Volcano Number")

st.write(volc)

countries=[]
for c in volc.Country:
  if c not in countries:
    countries.append(c)

country_radio = st.sidebar.radio("Please select a Country: ", sorted(countries))
volc_country = volc[(volc.Country.isin([country_radio]))]

st.title("Selected Country")
st.write(volc_country)
