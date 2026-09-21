# Project brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Raphael  Oladokun

---

## 1. The question

> Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?

## 2. Why this question

Residents in parts of Ibadan report unreliable access to cabs and shared taxis, particularly in areas that feel physically cut off from major roads. Understanding which settlements are furthest from the connected road network helps explain where this problem is most likely to occur, and gives local transport planners or advocacy groups a starting point for identifying underserved areas.

## 3. Study area

Ibadan South-West Local Government Area, Oyo State, Nigeria. Boundary defined by the GRID3 Nigeria Operational LGA Boundaries dataset, filtered to the single LGA.

## 4. What I mean by the terms

**"Major road"** — a road tagged in OpenStreetMap with a `highway` classification of trunk, primary, or secondary (as opposed to residential, service, or unclassified roads).

**"Transport hub"** — a known motor park, taxi stop, or bus station, where mappable via OpenStreetMap tags.

The original question asked about "paved road" specifically, but this was revised after testing the data — see the note under Known risks.

## 5. Datasets

| S/N | Dataset | What it gives me | Source | Format | Size |
|---|---|---|---|---|---|
| 1 | GRID3 Nigeria Operational LGA Boundaries | Administrative boundary to define and clip the study area | https://data.grid3.org | GeoPackage | 4.2 MB | 
| 2 | GRID3 Nigeria Settlement Extents v4.1 | Built-up settlement polygons — the units of analysis | https://data.grid3.org | GeoPackage | ~1.9 GB (nationwide) |
| 3 | OpenStreetMap roads (via QuickOSM) | Road network with classification, used to measure distance to major roads | https://www.openstreetmap.org | GeoPackage | 996 KB |

## 6. What "done" looks like

A web map showing every settlement in Ibadan South-West, shaded by distance to the nearest major road.

## 7. Known risks

**Sparse `surface` tagging in OSM.** The original question depended on whether a road was "paved," using OSM's `surface` tag. Testing showed this tag is only reliably present on major named roads, largely blank on residential and service roads. Rather than answer a question the data couldn't honestly support, the question was revised to depend on road classification and geometry (the `highway` tag) instead, which is complete and reliable across the dataset.

**Large file sizes for national datasets.** GRID3 settlement extents is a nationwide file (~1.9GB, 2.5 million features), which caused download delays. Mitigated by working with the LGA boundary and OSM data first, and clipping settlement extents down to the study area as soon as the download completed.

---

**Status:** Week 1 complete. Data acquisition in Week 2, see
[02-data-notes.md](02-data-notes.md).
