# Month 1 summary

**Week 4 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Raphael

---

## The question

Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?

## Which operation I ran, and why

A **distance join** (settlement polygons to nearest major road), not a buffer. A buffer only gives a binary inside/outside answer at one fixed threshold, whereas the project's stated deliverable — a map shaded by distance — needed a continuous distance value per settlement. Computing the actual distance also meant a threshold-based answer (e.g. "more than 2km") could be derived afterward as a simple filter, at no extra cost.

Before running the join, roads were filtered down to major classifications only (`highway` = trunk, primary, secondary — 58 of 2,762 total road features), since the question specifically concerns major roads, not the full road network.

The join itself was run using QGIS's "Join attributes by nearest" tool (found via the Processing Toolbox, `nearest` search — the version installed did not have it under the Vector menu), matching each settlement polygon to its nearest major road and recording the distance.

## What I expected, and what I got

Expected one output row per settlement (1,536, matching the clipped settlement count), each with a distance value in metres.

What I got instead: 1,643 rows — 107 more than expected.

## What surprised me

The row count mismatch turned out to be caused by multipart settlement geometries. The settlements layer is stored as Polygon (MultiPolygon), and the nearest-join operation appears to process multipart features part-by-part internally, producing a separate output row for each part of a settlement rather than one row per settlement.

This was caught only because the row count was checked against expectation (Step 4 of the practical: "does that match your expectation from Step 2?"). An initial attempt to find duplicate rows using the `fid` field found nothing, which could easily have been mistaken for a clean result — but `fid` is an auto-generated row ID, not a real attribute, so checking against it proved nothing. Switching to `block_id`, a genuine identifier from the original GRID3 data, correctly surfaced the duplicates. This was fixed using "Statistics by Categories," grouping by `block_id` and taking the minimum distance across each settlement's parts, which brought the row count back to the expected 1,536.

A second lesson followed directly from this: the corrected output of "Statistics by Categories" was a plain attribute table with no geometry, since aggregation does not preserve spatial data by default. The minimum-distance values had to be joined back onto the original settlement polygons (via `block_id`) and exported permanently before the result could be mapped at all.

## Result

| Threshold | Settlements exceeding it | % of 1,536 total |
|---|---|---|
| > 800 m | 378 | ~24.6% |
| > 1 km | 300 | ~19.5% |
| > 2 km | 96 | ~6.3% |

Full distance range across all settlements: 0 m to 2,777 m, mean approximately 1,390 m.

Reporting a single threshold risked understating or overstating the problem depending on which number was chosen — 2 km, borrowed from the project's original example question, is a fairly conservative cut relative to the data's actual range, while 800 m is closer to a widely used urban-planning standard for walkable access to transport (a 10–15 minute walk). Reporting all three together gives a more honest picture of the problem's scale than any single cutoff would.

## What data I still need

None identified yet for this specific question. The current analysis uses road classification and geometry only; it does not account for road surface quality, walkability of the route itself (e.g. unpaved or broken inner roads noted anecdotally), or actual transport frequency/availability, all of which were flagged in Week 1 as real contributing factors this project's data cannot directly measure.
