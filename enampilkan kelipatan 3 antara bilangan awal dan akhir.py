print("Program menampilkan kelipatan 3 antara bilangan awal dan akhir.")
print("Dibuat oleh Daffa Chandra Himawan")
print("25 Oktober 2025")

awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))

print("Kelipatan 3 antara", awal, "dan", akhir, ":", end=" ")

bil = awal
while bil <= akhir:
    if bil % 3 == 0:
        print(bil, end=" ")
    bil = bil + 1
