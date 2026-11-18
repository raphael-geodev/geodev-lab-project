import geopandas as gpd

settlements = gpd.read_file("processed/settlements_ibadan_southwest.gpkg", layer="settlements_ibadan_southwest")
roads = gpd.read_file("processed/major_roads_ibadan_southwest.gpkg", layer="major_roads_ibadan_southwest")

print("Settlements CRS:", settlements.crs)
print("Roads CRS:", roads.crs)
print("Suggested UTM:", settlements.estimate_utm_crs())

settlements = settlements.to_crs(epsg=32631)
roads = roads.to_crs(epsg=32631)

print("Settlement area km2:", round(settlements.area.sum() / 1_000_000, 1))
print("Road length km:", round(roads.length.sum() / 1000, 1))
print(len(roads))