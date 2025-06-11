import csv
from pathlib import Path

import plotly.express as px


def main() -> None:
    # Load and read data from file.
    file_path = Path(r"eq_data\MODIS_C6_1_Global_7d.csv")
    file_lines = file_path.read_text().splitlines()
    csv_reader = csv.DictReader(file_lines)

    # Store the data that we need on lists.
    latitudes, longitudes, confidence = [], [], []
    for row in csv_reader:
        latitudes.append(row["latitude"])
        longitudes.append(row["longitude"])
        confidence.append(f"Conficence: {row['confidence']}")

    # Create the plot and show it.
    title = "Global Fires"
    fig = px.scatter_geo(
        lat=latitudes,
        lon=longitudes,
        title=title,
        hover_name=confidence,
        projection="natural earth",
    )

    fig.show()


if __name__ == "__main__":
    main()
