def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Budi"))
print(sapa(salam="hai", nama="budi"))

def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))