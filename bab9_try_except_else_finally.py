try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("Input harus berupa angka.")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")
else:
    print(f"hasil: {hasil}")
finally:
    print("Program selesai.")