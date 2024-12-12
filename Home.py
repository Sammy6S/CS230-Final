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
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(page_title="Global Volcanoes", page_icon=":volcano:")
st.sidebar.header("\t Toggle :gear:")

pg = st.navigation([st.Page("pages/_🗺_️Map.py")])
pg.run()

st.image("Augustine_volcano.jpg", width=500)
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

st.title(f"Volcanoes in {country_radio}")
st.write(volc_country)

st.title("Volcano Elevation")
def findMaxMin(lst, m = "max"):
  i = lst[0]
  if m.lower() == "max":
    for l in lst:
      if l >= i:
        i = l
    return i
  elif m.lower() == "min":
    for l in lst:
      if l <= i:
        i = l
    return i

elevation_slider = st.slider("Slide for Elevation (+/-50m)",findMaxMin(volc["Elevation (m)"], "min") , findMaxMin(volc["Elevation (m)"], "max"), 0, 100)
volc_elevation = volc[(volc["Elevation (m)"] >= (elevation_slider - 50)) & (volc["Elevation (m)"] <= (elevation_slider + 50))]
volc_elevation.insert(0, "Elevation (m)", volc_elevation.pop("Elevation (m)"))
st.write(volc_elevation.sort_values("Elevation (m)"))

column_select = st.multiselect("Select columns to be shown: ", volc.columns)
st.write(volc[column_select])

volcBar = volc[(volc.Country.isin([countries]))]
volcBar.plot(kind = "bar")
plt.xlabel("Year")
plt.ylabel("Sales Percentage")
plt.title("Volcano data for each country")
plt.legend(countries)
st.pyplot()
