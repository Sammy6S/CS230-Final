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
import pydeck as pdk
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

volc_elevation.plot()
st.pyplot()

st.title("Volcano Map")
volcLat = volc[["Latitude","Longitude"]]
volcLat.rename(columns={"Latitude":"lat", "Longitude": "lon"}, inplace= True)
st.map(volcLat)

# Create a view of the map: https://pydeck.gl/view.html
    view_state = pdk.ViewState(
        latitude=volcLat["lat"].mean(), # The latitude of the view center
        longitude=volcLat["lon"].mean(), # The longitude of the view center
        zoom=11, # View zoom level
        pitch=0) # Tilt level

    # Create a map layer with the given coordinates
    layer1 = pdk.Layer(type = 'ScatterplotLayer', # layer type
                      data=volcLat, # data source
                      get_position='[lon, lat]', # coordinates
                      get_radius=500, # scatter radius
                      get_color=[0,200,0],   # scatter color
                      pickable=True # work with tooltip
                      )

    # Can create multiple layers in a map
    # For more layer information
    # https://deckgl.readthedocs.io/en/latest/layer.html
    # Line layer https://pydeck.gl/gallery/line_layer.html
    layer2 = pdk.Layer('ScatterplotLayer',
                      data=volcLat,
                      get_position='[lon, lat]',
                      get_radius=300,
                      get_color=[0,0,255],
                      pickable=True
                      )


   # stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
    tool_tip = {"html": "<b>{Elevation (m)}</b>",
                "style": { "backgroundColor": "orange",
                            "color": "white"}
              }

    # Create a map based on the view, layers, and tool tip
    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v12', # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
        initial_view_state=view_state,
        layers=[ layer1, layer2], # The following layer would be on top of the previous layers
        tooltip= tool_tip
    )

    st.pydeck_chart(map) # Show the map in your app
