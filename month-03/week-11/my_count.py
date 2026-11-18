import geopandas as gpd

settlements = gpd.read_file("processed/settlements_ibadan_southwest.gpkg", layer="settlements_ibadan_southwest").to_crs(epsg=32631)
lga = gpd.read_file("processed/lga_boundaries_utm31.gpkg", layer="lga_boundaries_utm31").to_crs(epsg=32631)

points = settlements.copy()
points["geometry"] = settlements.centroid

joined = gpd.sjoin(points, lga[["lganame", "geometry"]], how="inner", predicate="within")
counts = joined.groupby("lganame").size().rename("settlement_count").reset_index()

lga = lga.merge(counts, on="lganame", how="left")
lga["settlement_count"] = lga["settlement_count"].fillna(0).astype(int)

print(lga[["lganame", "settlement_count"]][lga["settlement_count"] > 0])
print("Total counted:", lga["settlement_count"].sum(), "of", len(points))