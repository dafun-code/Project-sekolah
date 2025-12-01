print("Program menghitung kata")
print("Dibuat oleh Daffa Chandra Himawan")
print("23 Oktober 2025")

kalimat = input("Masukkan kalimat: ")

daftar_kata = kalimat.split()
jumlah_kata = 0
for kata in daftar_kata:
    jumlah_kata += 1

print("Kalimat di atas memiliki", jumlah_kata, "kata.")