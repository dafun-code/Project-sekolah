print("Program menjumlah angka negatif.")
print("Dibuat oleh Daffa Chandra Himawan")
print("23 Oktober 2025")

bilangan = [1, 2, -3, 4, -5, 6, 7, 8, -9, 10, 11, 12]

print("Ada 12 bilangan yaitu", bilangan)

jumlah = 0

for angka in bilangan:
    if angka < 0:
        jumlah = jumlah + angka

print("Jumlah semua angka negatif adalah", jumlah)
