# Data notes

## GRID3 Nigeria Operational LGA Boundaries
- Source: https://data.grid3.org
- Downloaded: [date]
- 774 features, polygons (MultiPolygon)
- Columns: FID (integer, 64-bit), globalid (text), uniq_id (integer, 32-bit), timestamp (text), editor (text), lganame (text), lgacode (text), statename (text), statecode (text), source (text), amapcode (text)
- No nulls found
- Row count matches the known total of 774 LGAs in Nigeria — a good sanity check that this is the right dataset
- lgacode and statecode are stored as text, likely intentional (numeric codes with leading zeros would lose them if stored as numbers)
- Coverage looks complete

## OSM roads, extracted via QuickOSM
- Query: highway=* within Ibadan South-West extent
- Extracted: [date]
- 2,762 features, lines
- Columns: fid, full_id, osm_id, osm_type, highway, covered, tunnel, incline, access, service, horse, cycleway, lane_markings, shoulder, name:en, flood_prone, junction, layer, bridge, surface, ref, oneway, lanes, name
- All columns except fid are stored as text (expected — OSM tag values are always free text)
- Nulls present across several columns, most notably `surface`: reliably tagged on major named roads, largely blank on residential and service roads
- Coverage checked against Esri satellite imagery: approximately 99% match, no significant gaps found — Ibadan South-West appears to be a well-mapped area, consistent with it being part of a major city

## GRID3 Nigeria Settlement Extents v4.1
- Source: https://data.grid3.org
- Downloaded: [date]
- 2,546,560 features (nationwide), Polygon (MultiPolygon)
- Column types present: Integer (64-bit), Integer (32-bit), Text (string), Decimal (double) — full column list not itemised here due to dataset size, see raw file for schema
- Nulls: not checked at national scale — dataset too large to sort/scan column-by-column before clipping; to be checked on the clipped, study-area version
- Coverage checked against satellite imagery for the study area, looked complete

## Note on data quality → question adjustment (Week 1)
The original project question depended on the `surface` tag ("paved road within 2km"). Investigation showed `surface` is only consistently tagged on major named roads, not on the residential/service roads that make up most of the network. This matches a known OSM pattern: when a question depends on a tag that only a minority of features carry, the answer describes that minority, not the area as a whole.
The question was adjusted to rely on road classification and geometry (the `highway` tag) instead, which is complete and reliable across the dataset. Revised question: "Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?"

## CRS and preparation (Week 3)
- Source layers arrived in mixed CRS: GRID3 LGA boundaries and OSM roads in EPSG:4326 (WGS 84); GRID3 settlement extents in EPSG:3857 (Pseudo-Mercator)
- Confirmed EPSG:4326 is unsuitable for measurement: area calculated on LGA boundaries in native CRS returned a meaningless "square degrees" value, as expected
- Study area: Ibadan South-West, extracted as a single feature from GRID3 LGA boundaries, saved as study_area.gpkg
- All three layers (LGA boundaries, OSM roads, settlement extents) reprojected to EPSG:32631 (UTM zone 31N — correct zone for western Nigeria)
- Area check after reprojection: Ibadan South-West computed at 24.05 km², close to the published core urban footprint figure of 25.13 km² — sanity check passed
- All layers clipped to study_area boundary; visually confirmed no clipped features fall outside the study area
- Working files (reprojected, clipped) saved in data/processed/: lga_boundaries_utm31.gpkg, roads_utm31.gpkg, roads_ibadan_southwest.gpkg, settlements_utm31.gpkg, settlements_ibadan_southwest.gpkg, study_area.gpkg
- Raw files in data/raw/ left untouched throughout
