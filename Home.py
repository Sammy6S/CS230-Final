import pandas as pd
import numpy as np
import streamlit as st

st.title("Global Volcanoes")
path = "volcanoes.csv"
volc = pd.read_csv(path)

st.write(volc)
