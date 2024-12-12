import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk
import streamlit as st

path = "volcanoes.csv"
volc = pd.read_csv(path, delimiter=",", comment="%")
volc.set_index("Volcano Number")

st.title("Volcano Map")
volcLat = volc[["Latitude","Longitude"]]
volcLat.rename(columns={"Latitude":"lat", "Longitude": "lon"}, inplace= True)
st.map(volcLat)
