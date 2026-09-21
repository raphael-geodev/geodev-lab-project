# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Raphael Oladokun

What I downloaded, where it came from, what is in it, and what is wrong
with it.

---

## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | GRID3 Nigeria Operational LGA Boundaries | Vector (polygon) | 3/9/2026 | OK |
| 2 | OSM roads (Ibadan South-West, via QuickOSM) | Vector (line) |  3/9/2026 | OK |
| 3 | GRID3 Nigeria Settlement Extents v4.1 | Vector (polygon) |  14/9/2026 | OK |

---

## 1. GRID3 Nigeria Operational LGA Boundaries

- **Source:** https://data.grid3.org
- **Retrieved:**  3/9/2026
- **File:** `data/raw/nga_lga_boundaries.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Polygon (MultiPolygon)
- **Feature count:** 774
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `lganame` | Name of the LGA | 0 |
| `lgacode` | LGA code (text, preserves leading zeros) | 0 |
| `statename` | Name of the state | 0 |
| `statecode` | State code (text) | 0 |
| `globalid`, `uniq_id`, `timestamp`, `editor`, `source`, `amapcode` | Metadata fields | 0 |

**What I noticed**

Row count (774) matches the known total number of LGAs in Nigeria — a useful sanity check that this is the correct, complete dataset. No nulls found across any column. Coverage looked complete against the map.

---

## 2. OSM roads (Ibadan South-West, via QuickOSM)

- **Source:** https://www.openstreetmap.org (extracted via QuickOSM plugin in QGIS)
- **Retrieved:**  3/9/2026
- **File:** `data/raw/ibadan_highway.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Line
- **Feature count:** 2,762
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `highway` | Road classification (trunk, primary, residential, etc.) | Low |
| `surface` | Road surface material | High — see below |
| `name`, `name:en`, `ref` | Road naming | Variable |
| `oneway`, `lanes`, `access`, `bridge`, `tunnel`, and others | OSM tag fields | Variable |

**What I noticed**

All columns except `fid` are stored as text, expected for OSM tag values. The `surface` column is reliably filled in on major named roads (e.g. Ring Road, Old Abeokuta Road) but largely blank on residential and service roads — this directly affected the project question (see project brief, Known risks). Coverage checked against Esri satellite imagery: approximately 99% match, no significant gaps found.

---

## 3. GRID3 Nigeria Settlement Extents v4.1

- **Source:** https://data.grid3.org
- **Retrieved:**  14/9/2026
- **File:** `data/raw/nga_settlement_extents_v4_1.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Polygon (MultiPolygon)
- **Feature count:** 2,546,560 (nationwide)
- **CRS as downloaded:** EPSG:3857

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| Numerous Columns| Mix of Integer (64-bit), Integer (32-bit), Text, and Decimal (double) fields | Not checked at national scale |

**What I noticed**

Full column-by-column inspection wasn't practical at the national scale — the file is large enough that sorting/scanning risked crashing the working machine. This is flagged as an open gap rather than assumed clean; it was revisited on the clipped, study-area version in Week 3. Coverage checked against satellite imagery for the study area and looked complete. Downloaded in EPSG:3857 (Web Mercator), unlike the other two datasets, which arrived in EPSG:4326.

---

## Cross-cutting problems

**Inconsistent `surface` tagging in OSM roads.** Only a minority of road features carry this tag reliably, which meant the original project question (dependent on "paved vs unpaved") wasn't answerable as written. Addressed in Week 1 by revising the question to depend on road classification instead.

**Mixed coordinate reference systems across datasets.** LGA boundaries and OSM roads arrived in EPSG:4326; settlement extents arrived in EPSG:3857. All three needed reprojecting to a common working CRS before any spatial operations (clipping, distance calculations) could be done — addressed in Week 3.

---

**Status:** Week 2 complete. Reprojection and quality checks in Week 3,
see [03-data-preparation.md](03-data-preparation.md).
