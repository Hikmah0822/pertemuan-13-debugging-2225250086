def hitung_total(data):
    total = 0

    for angka in data:
        total += angka

    return total


nilai = [80, 90, 70]
hasil = hitung_total(nilai)

print("Total nilai:", hasil)