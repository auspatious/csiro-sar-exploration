import json
from shapely.geometry import shape

# A bounding box over all Australia
bbox = [112.0, -44.0, 155.0, -11.0]


def get_australia_coords():
    with open("australia.geojson") as f:
        australia = json.load(f)
        return australia["features"][0]["geometry"]["coordinates"][0]


def get_australia_geometry():
    with open("australia.geojson") as f:
        australia = json.load(f)
        return shape(australia["features"][0]["geometry"])
