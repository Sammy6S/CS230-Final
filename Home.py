"""
Name 
"""

import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Global Volcanoes", page_icon=":volcano:")
st.sidebar.write("## Toggle :gear:")

st.title("Global Volcanoes")
path = "volcanoes.csv"
volc = pd.read_csv(path)

st.write(volc)
