from pathlib import Path
import csv

csv_path = Path(__file__).with_name("nilai.csv")

data = []
with csv_path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        try:
            baris["nilai"] = int(baris["nilai"])
            data.append(baris)
        except (TypeError, ValueError):
            print("Data tidak valid:", baris)

print(len(data), "baris")
if data:
    print(data[0])
