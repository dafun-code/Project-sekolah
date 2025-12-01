print("Program menampilkan bilangan ganjil.")
print("Dibuat oleh Daffa Chandra Himawan")
print("23 Oktober 2025")
awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))
print("Bilangan ganjil antara:", awal, "dan", akhir)

bil = awal
while bil <= akhir:
    if bil % 2 != 0:
        print(bil, end=" ")
    bil += 1
