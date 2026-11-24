import rasterio

with rasterio.open("data/raw/output_hh.tif") as src:
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("Nodata:", src.nodata)
    print("Transform:")
    print(src.transform)
    print("Width x pixel size:", src.width * src.res[0], "| right - left:", src.bounds.right - src.bounds.left)
    print("Height x pixel size:", src.height * src.res[1], "| top - bottom:", src.bounds.top - src.bounds.bottom)