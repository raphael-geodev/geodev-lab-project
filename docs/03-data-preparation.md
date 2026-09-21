# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Raphael

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** EPSG:32631 (UTM zone 31N)

**Why this one:** Ibadan South-West sits in western Nigeria, within UTM zone 31N. The project's core question depends on distance measurement (settlements to nearest major road), which requires a projected CRS in metres — EPSG:4326 (geographic, degrees) and EPSG:3857 (Web Mercator, distorted away from its design purpose) are both unsuitable for this.

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| GRID3 LGA boundaries | EPSG:4326 | EPSG:32631 | Reprojected |
| OSM roads | EPSG:4326 | EPSG:32631 | Reprojected |
| GRID3 settlement extents | EPSG:3857 | EPSG:32631 | Reprojected |

> Before reprojecting, area was deliberately calculated on the LGA boundaries layer in its native EPSG:4326 CRS to confirm the failure mode: this returned a meaningless "square degrees" value with no error or warning. This confirmed the need to reproject before any measurement.

## 2. Clipping to the study area

- **Boundary used:** Single feature exported from GRID3 LGA boundaries (Ibadan South-West), saved as `data/processed/study_area.gpkg`
- **Features before clipping:** Roads 2,762 (LGA extent from QuickOSM query); Settlements 2,546,560 (nationwide)
- **Features after clipping:** [to confirm exact counts from attribute tables]

Visual inspection confirmed no clipped features from either layer fall outside the study area boundary.

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | Confirmed — mixed CRS found (EPSG:4326, EPSG:3857) | Reprojected all layers to EPSG:32631 |
| Are there nulls in the fields I need? | Yes — `surface` on roads is sparse/inconsistent; not checked on settlement extents | Roads: acknowledged and worked around by not depending on `surface`. Settlements: not checked — file too large to sort without risking a system crash; flagged as an open gap |
| Are there duplicate features? | Not checked | Flagged as an open gap, not yet run on any layer |
| Is the geometry valid? | Not checked | Flagged as an open gap, not yet run on any layer |
| Does coverage span the whole study area? | Yes | Confirmed visually against satellite basemap; roads matched ~99% |

## 4. Problems found, and what I did

**Sparse and inconsistent `surface` tagging on OSM roads.** Only a minority of road features (mostly major named roads) carry a `surface` value. This made the original "paved road" question unanswerable honestly with this data. Fixed by revising the question in Week 1 to depend on road classification (`highway` tag) instead, which is complete and reliable.

**Settlement extents too large to fully quality-check.** At 2.5 million features nationwide, sorting columns for nulls, duplicates, or invalid geometry risked crashing the working machine. Not fixed — flagged honestly as an unresolved gap, to be revisited on the clipped study-area version now that the file is much smaller.

## 5. The analysis-ready output

- **File:** `data/processed/roads_ibadan_southwest.gpkg`, `data/processed/settlements_ibadan_southwest.gpkg`, `data/processed/study_area.gpkg`
- **Format:** GeoPackage
- **CRS:** EPSG:32631
- **Features:** [to confirm exact clipped counts]
- **Produced by:** Manually in QGIS (Reproject Layer, Clip)

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
