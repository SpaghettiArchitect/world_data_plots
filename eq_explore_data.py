import json
from pathlib import Path

import plotly.express as px


def main() -> None:
    """The main function of the script."""
    # Read data as a string and convert to a Python object.
    path = Path(r"eq_data\eq_data_30_day_m1.geojson.json")
    contents = path.read_text("utf8")
    all_eq_data = json.loads(contents)

    # Examine all earthquakes in the dataset.
    all_eq_dicts = all_eq_data["features"]

    # Store the magnitude, longitude, latitude and title of each earthquake.
    magnitudes, longitudes, latitudes, eq_titles = [], [], [], []
    for eq_dict in all_eq_dicts:
        magnitudes.append(eq_dict["properties"]["mag"])
        longitudes.append(eq_dict["geometry"]["coordinates"][0])
        latitudes.append(eq_dict["geometry"]["coordinates"][1])
        eq_titles.append(eq_dict["properties"]["title"])

    # Build a simple world map that displays the location of earthquakes.
    title = "Global Earthquakes"
    fig = px.scatter_geo(
        lat=latitudes,
        lon=longitudes,
        size=magnitudes,
        title=title,
        color=magnitudes,
        color_continuous_scale="temps",
        labels={"color": "Magnitude"},
        projection="natural earth",
        hover_name=eq_titles,
    )
    fig.show()


if __name__ == "__main__":
    main()
