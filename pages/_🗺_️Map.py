import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk
import streamlit as st

path = "volcanoes.csv"
volc = pd.read_csv(path, delimiter=",", comment="%")
volc.set_index("Volcano Number")
