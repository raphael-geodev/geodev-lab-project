import geopandas as gpd

settlements = gpd.read_file("processed/settlements_ibadan_southwest.gpkg", layer="settlements_ibadan_southwest")
roads = gpd.read_file("processed/major_roads_ibadan_southwest.gpkg", layer="major_roads_ibadan_southwest")

centres = settlements.copy()
centres["geometry"] = settlements.centroid

nearest = gpd.sjoin_nearest(
    centres, roads[["geometry"]], how="left", distance_col="distance_m"
)
nearest = nearest[~nearest.index.duplicated()]   # removes ties
nearest["distance_km"] = nearest["distance_m"] / 1000

print(nearest["distance_km"].describe())
print("Over 2 km:", (nearest["distance_km"] > 2).sum(), "of", len(nearest))

settlements["distance_km"] = nearest["distance_km"]
settlements.to_file("processed/settlements_road_distance.gpkg", layer="settlements_distance")

settlements["distance_km"] = nearest["distance_km"]
settlements.to_file("data/processed/settlements_road_distance.gpkg", layer="settlements_distance")

import matplotlib.pyplot as plt
ax = settlements.plot(column="distance_km", legend=True, cmap="Reds", figsize=(8, 8))
ax.set_axis_off()
plt.savefig("month-03/week-11/my_reach_map.png", dpi=150, bbox_inches="tight")