# ARCGIS API FOR PYTHON

# This code works in python notebook 
# This code accesses my NFK Web Map in ArcGIS Online using web map id
# Written by HaKaN OGUZ

# Imports ArcGIS API for Python
from arcgis.gis import GIS

trees_id = "ENTER_WEB_MAP_ID"

gis = GIS()

park = gis.content.get(trees_id)
park

m = gis.map()
m.add_layer(park)

# NFK Park's central coordinates
m.center = [ 37.587782, 36.896656]  # [latitude, longitude]
m.zoom = 20

# Show the map
m