titik = (3, 7)
warna = (255, 128, 0)

x, y = titik
print(f"x={x}, y={y}")
print(warna[0], len(warna))

try:
    titik[0] = 10
except TypeError as e:
    print(f"Error: {e}")