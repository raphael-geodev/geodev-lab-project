import csv 

def inspect_column(filename, column):
    with open("settlements_ibadan_southwest.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "" :
            continue
    values.append(float(raw))
    return {
    "Smallest":  min(values),
    "Largest": max(values),
    "Count": len(values),
  }

area_result = inspect_column("settlements_ibadan_southwest.csv", "block_area_sqm")
perimeter_result = inspect_column("settlements_ibadan_southwest.csv", "block_perimeter")

print("Area:", area_result) 
print("Perimeter: ", perimeter_result)