
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Test case rata-rata
print("T1:", hitung_rata_rata([80, 60, 90, 70]))
print("T2:", hitung_rata_rata([100, 80]))

# Test case status kelulusan
print("T3:", status(60))
print("T4:", status(59))

# Test case nilai tertinggi
print("T5:", nilai_tertinggi([80, 60, 90, 70]))
