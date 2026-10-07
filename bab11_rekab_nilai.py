from pathlib import Path
import csv

csv_path = Path(__file__).with_name("nilai.csv")

with open(csv_path) as f:
    reader = csv.DictReader(f)
    data = []
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'kelas':<6}{'jumlah':>8}{'rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")