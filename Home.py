import pandas as pd

import streamlit as st

st.write("Global Volcanoes")
path = "volcanoes.csv"
volc = pd.read_csv(path)

st.write(volc)
