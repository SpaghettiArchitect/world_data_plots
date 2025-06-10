import json
from pathlib import Path

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path(r"eq_data\eq_data_1_day_m1.geojson")
contents = path.read_text("utf8")
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

# Store the magnitude, longitude, and latitude of each earthquake.
magnitudes, longitudes, latitudes = [], [], []
for eq_dict in all_eq_dicts:
    magnitude = eq_dict["properties"]["mag"]
    longitude = eq_dict["geometry"]["coordinates"][0]
    latitude = eq_dict["geometry"]["coordinates"][1]
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

# Build a simple world map that displays the location of earthquakes.
title = "Global Earthquakes"
fig = px.scatter_geo(lat=latitudes, lon=longitudes, title=title)
fig.show()
