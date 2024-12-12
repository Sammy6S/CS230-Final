import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.write("Global Volcanoes")
path = "volcanoes.csv"
volc = pd.read_csv(path)

st.write(volc)
