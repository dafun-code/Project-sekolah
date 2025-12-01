print("20 bilangan bulat pada sebuah koleksi, ada yang positif, nol, dan negatif.")
print("Dibuat oleh Daffa Chandra Himawan")
print("23 Oktober 2025")

bilangan = [5, -8, 0, 4, -3, 9, -1, 7, 0, -5, 6, -10, 2, -7, 3, 8, 0, -9, 1, -4]
for angka in bilangan:
    if angka > 0:
        print(angka, "positif")
    elif angka == 0:
        print(angka, "nol")
    else:
        print(angka, "negatif")
