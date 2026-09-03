# Project Brief

**Project:** Transport Access Mapping — Ibadan South-West, Oyo State
**Author:** Oladokun Raphael Ayode
**Cohort:** GeoDev Lab Africa, Cohort One
**Date:** 3/9/2026

---

## 1. The Question

Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?

## 2. Why This Matters

Residents in parts of Ibadan report unreliable access to cabs and shared taxis, particularly in areas that feel physically cut off from major roads. Understanding which settlements are furthest from the connected road network helps explain where this problem is most likely to occur, and gives local transport planners or advocacy groups a starting point for identifying underserved areas. It also lays the groundwork for a system that could eventually flag these areas automatically as the project grows.

## 3. The Data I Need

- LGA administrative boundary for Ibadan South-West
- Settlement extents within Ibadan South-West
- Road network with classification (highway type: trunk, primary, secondary, tertiary, etc.) for Ibadan South-West

## 4. Where Each Dataset Comes From

| Data item | Source | Link |
|---|---|---|
| LGA administrative boundary | GRID3 Data Hub | https://data.grid3.org |
| Settlement extents | GRID3 Data Hub | https://data.grid3.org |
| Road network with classification | OpenStreetMap (via QuickOSM in QGIS) | https://www.openstreetmap.org |

## 5. What You Would Build

A web map showing every settlement in Ibadan South-West, shaded by distance to the nearest major road.

---

## Note on Data Quality (from Week 1 testing)

Before settling on this question, an OSM road extract for Ibadan South-West was pulled via QuickOSM and checked for a `surface` tag. Result: `surface` is reliably tagged on major named roads, but largely blank on residential and service roads. This ruled out a strict "paved road" version of the question and led to the version above, which relies on road classification and geometry — both of which are complete and reliable across the dataset.
