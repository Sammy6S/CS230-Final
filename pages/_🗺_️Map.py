import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk
import streamlit as st

path = "volcanoes.csv"
volc = pd.read_csv(path, delimiter=",", comment="%")
volc.set_index("Volcano Number")

st.title("Volcano Map")
volcLat = volc[["Latitude","Longitude","Elevation (m)","Volcano Name"]]
volcLat.rename(columns={"Latitude":"lat", "Longitude": "lon"}, inplace= True)
st.map(volcLat)

view_state = pdk.ViewState(latitude=volcLat["lat"].mean(), longitude=volcLat["lon"].mean(), zoom=5, pitch=25) 

layer1 = pdk.Layer(type = 'ScatterplotLayer', data=volcLat, get_position='[lon, lat]', get_radius=2000, get_color=[200,200,0],   pickable=True)

layer2 = pdk.Layer('ScatterplotLayer', data=volcLat, get_position='[lon, lat]', get_radius=300, get_color=[0,0,255], pickable=True)

tool_tip = {"html": "<b>{Volcano Name}</b>", "style": { "backgroundColor": "orange", "color": "white"}}

map = pdk.Deck(map_style='mapbox://styles/mapbox/streets-v12', initial_view_state=view_state, layers=[ layer1, layer2], tooltip= tool_tip)

st.pydeck_chart(map)
