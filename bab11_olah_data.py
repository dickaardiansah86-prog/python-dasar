from pathlib import Path
import csv

csv_path = Path(__file__).with_name("nilai.csv")

with open(csv_path) as f:
    reader = csv.DictReader(f)
    data = []
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata nilai: {rata:.1f}")

lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])