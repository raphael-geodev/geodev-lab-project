# Ibadan South-West Transport Access

A web map showing which settlements in Ibadan South-West, Oyo State, are furthest from the connected road network — built to explore why some areas report unreliable cab and shared-taxi access.

**GeoDev Lab Africa, Cohort One.** Raphael Oladokun

---

## The question

> Which settlements in Ibadan South-West Local Government Area are more than 2 km from the nearest major road or transport hub?

## What's in here

```
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

## Progress

- [x] Week 1, project brief with a source link for every dataset
- [x] Week 2, data downloaded, opened and described
- [x] Week 3, reprojected, clipped and quality checked
- [x] Week 4, first spatial analysis, checked four ways

---

Raphael Oladokun · GeoDev Lab Africa
Learn. Build. Collaborate. Transform.
