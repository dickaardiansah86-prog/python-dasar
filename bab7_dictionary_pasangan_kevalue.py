siswa = {"nama": "sari", "umur": 19}
siswa["kota"] = "bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(k, ":", v)