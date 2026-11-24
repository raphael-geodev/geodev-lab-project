import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("data/processed/my_ndvi.tif") as src:
    areas = gpd.read_file("processed/lga_boundaries_utm31.gpkg", layer="lga_boundaries_utm31").to_crs(src.crs)
    areas = areas[areas["lganame"] == "Ibadan South West"].copy()
    means = []
    for geom in areas.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

areas["mean_ndvi"] = np.round(means, 3)
print(areas[["lganame", "mean_ndvi"]])
areas.drop(columns="geometry").to_csv("month-03/week-12/my_zonal_stats.csv", index=False)