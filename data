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

## Note on data quality → question adjustment (Week 1)
The original project question depended on the `surface` tag ("paved road within 2km"). Investigation showed `surface` is only consistently tagged on major named roads, not on the residential/service roads that make up most of the network. This matches a known OSM pattern: when a question depends on a tag that only a minority of features carry, the answer describes that minority, not the area as a whole.
The question was adjusted to rely on road classification and geometry (the `highway` tag) instead, which is complete and reliable across the dataset. Revised question: "Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?"

## GRID3 Nigeria Settlement Extents v4.1
- Source: https://data.grid3.org
- Status: download incomplete due to network issues, to be finished and logged separately
