nilai = [80, 90, 70]

with open("hasil_nilai.txt", "w") as file:
    for angka in nilai:
        file.write(f"{angka}\n")

print("Data nilai berhasil disimpan.")