import pandas as pd

import streamlit as st

st.write("Hello World")
path = "volcanoes.csv"
dfpct = pd.read_csv(path)

st.write(dfpct)
