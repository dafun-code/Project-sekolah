#Nama: Daffa Chandra Himawan
#NIM : L200250028

# Memasukkan harga dan jumlah
harga_buku = float(input("Masukkan harga satu buku: "))
jumlah_buku = int(input("Masukkan jumlah buku yang dibeli: "))

# Menghitung total harga
total_harga = harga_buku * jumlah_buku

# Mengecek apakah mendapat diskon
if jumlah_buku > 5:
    diskon = 0.15 * total_harga
else:
    diskon = 0

# Menghitung total bayar setelah diskon
total_bayar = total_harga - diskon

# Menampilkan hasil
print("Total harga sebelum diskon:", total_harga)
print("Diskon:", diskon)
print("Total yang harus dibayar:", total_bayar)