import geopandas as gpd
settlements = gpd.read_file("processed/settlements_ibadan_southwest.gpkg", layer="settlements_ibadan_southwest")

print("Invalid before:", (~settlements.is_valid).sum())
settlements["geometry"] = settlements.make_valid()
print("Invalid after:", (~settlements.is_valid).sum())