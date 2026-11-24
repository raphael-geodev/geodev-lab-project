# Ibadan South-West Transport Access

A web map showing which settlements in Ibadan South-West, Oyo State, are furthest from the connected road network — built to explore why some areas report unreliable cab and shared-taxi access.

**GeoDev Lab Africa, Cohort One.** Raphael Oladokun

---

## The question

> Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?

## What's in here

```md
ibadan-transport-access/
├── docs/
│   ├── 01-project-brief.md                  Week 1
│   ├── 02-data-notes.md                     Week 2
│   ├── 03-data-preparation.md               Week 3
|   ├── 04-spatial-analysis.md               Week 4
|   ├── ibadan_transport_access_map_.pmg     final map
|   └── month-1-summary.md.                  month 1's summary
|       
├── data/
│   ├── raw/                     downloads, not committed
│   └── processed/              clipped and reprojected data,  committed
├── scripts/
└── requirements.txt
```

## How to run it

```bash
git clone https://github.com/raphael-geodev/geodev-lab-project.git
cd ibadan-transport-access

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The data is not in this repository. Every source is linked in
[the project brief](docs/01-project-brief.md), so anyone can fetch it. The processed data are  in [processed data](processed)

Access all what have been done from week 1 to week 4 here

- [Week 1](docs/01-project-brief.md)
- [Week 2](docs/02-data-notes.md)
- [Week 3](docs/03-data-preparation.md)
- [Week 4](docs/04-spatial-analysis.md)
- [Month 1 Summary](docs/month-1-summary.md)

## Month 2: Development and early python

- Week 5: development environment set up, hello.py proven working
- Week 6: set up the project with uv and added pandas. check.py prints the pandas version
- Week 7: analyse.py reads wards.csv, converts each area and clasifies each ward.
- Week 8: inspect_data.py summarizes the perimeter and area of blocks in my settlements_ibadan_southwest.csv data
- Week 9: summary.py is a refactored version of inspect_data.py

### Month 2 reflection

The biggest lesson this month was to check my output against what I expect, not just whether the script runs. In Week 8, two bugs didn't crash anything: an `append` outside my loop, and a return written with commas that built a set instead of a dictionary. Refactoring hasn't clicked yet, so I'll keep practising by rewriting my own scripts into small functions. My capstone on the Ibadan South-West settlements data shows how the settlements there are sized in blocks, from the smallest block to the largest.

## Month 3: Geospatial python and automation

- week 10: Geopandas. Loaded, checked, joined and mapped in code

## Week 11: CRS and spatial operations

### Coordinate reference system

- EPSG code used: **EPSG:32631** (WGS 84 / UTM zone 31N).
- Why: Ibadan lies between 0° and 6°E, which is UTM zone 31N. `estimate_utm_crs()` returned the same code.
- My settlements and roads layers were already in EPSG:32631, so `to_crs` changed nothing. I kept it in the scripts so the measurements are always in metres.
- Settlement footprint area: 24.0 km².

### Scripts

- `my_crs.py`: prints each layer's CRS, confirms the UTM zone, and measures area and road length in km² and km.
- `my_validity.py`: 0 invalid geometries before and after `make_valid`, so no repairs were needed.
- `my_count.py`: counted settlement centre points per LGA with `sjoin` (`within`) and `groupby`, then merged back so every LGA has a count, including zeros. Total counted: **1,536 of 1,536**. 1,515 fall in Ibadan South West and 21 fall in neighbouring LGAs.
- `my_reach.py`: measured the straight-line distance from each settlement's centre point to the nearest road with `sjoin_nearest`.

### Result

110 of 1,536 settlements (about 7%) are more than 2 km from the nearest road. Median distance is 0.44 km and the farthest settlement is 2.78 km away. I chose 2 km because it is the threshold in my project question.

Roads used: [file name and which road types are in it, e.g. "major_roads_ibadan_southwest, primary and secondary roads"].

Map: `my_reach_map.png`. Result layer: `data/processed/settlements_road_distance.gpkg`.

### Limitation

Distance is measured in a straight line from each settlement's centre point to the nearest road. It is not travel distance along roads, and a centre point is only a rough stand-in for where people live. Real access may be worse than these numbers show.
The settlements layer is also not clipped to the LGA: 21 of 1,536 settlements sit in neighbouring LGAs, so the study area is slightly larger than Ibadan South West. This i because I used the unclipped version of my file I committed to github.

## Week 12: Rasters

- Computed NDVI for Ibadan South West and summarised it.

## Progress

- [x] Week 1, project brief with a source link for every dataset
- [x] Week 2, data downloaded, opened and described
- [x] Week 3, reprojected, clipped and quality checked
- [x] Week 4, first spatial analysis, checked four ways
- [x] Week 5, development environment set up
- [x] Week 6, development environment set up
- [x] Week 7, wrote python code to analyse wards in csv file
- [x] Week 8, wrote a python code to summarize two columns
- [x] Week 9, wrote a cleaner version of week 8 code
- [x] Week 10, explored geopandas
- [x] Week 11, reprojection and spatial operations
- [x] Week 12, Raster with Rasterio

---

Raphael Oladokun · GeoDev Lab Africa
Learn. Build. Collaborate. Transform.
