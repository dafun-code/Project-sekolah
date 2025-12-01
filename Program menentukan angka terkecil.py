print("Program menentukan angka terkecil.")
print("Dibuat oleh Daffa Chandra Himawan")
print("25 Oktober 2025")

terkecil = 0

for i in range(1, 9):
    angka = int(input("Masukkan bilangan ke-" + str(i) + ": "))
    if i == 1:
        terkecil = angka
    elif angka < terkecil:
        terkecil = angka

print("Bilangan terkecil adalah", terkecil)
