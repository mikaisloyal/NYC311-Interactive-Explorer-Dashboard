import csv
import sys
from datetime import datetime

csv.field_size_limit(10**9)
path = sys.argv[1]
FMT = "%m/%d/%Y %I:%M:%S %p"

with open(path, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    names = [h.strip().lower().replace(" ", "_") for h in header]
    col = names.index("created_date")
    rows = 0
    first = last = None
    bad = 0
    for row in reader:
        rows += 1
        try:
            d = datetime.strptime(row[col], FMT)
        except (ValueError, IndexError):
            bad += 1
            continue
        if first is None or d < first:
            first = d
        if last is None or d > last:
            last = d

print("columns:", len(header))
print("rows (without header):", rows)
print("first created:", first)
print("last created:", last)
print("rows with unreadable created date:", bad)
