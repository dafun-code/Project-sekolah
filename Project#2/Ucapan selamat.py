waktu = ('pagi', 'siang', 'sore', 'malam')
nama = input("Masukkan nama: ")
jam = float(input("Pukul berapa sekarang? "))
if 0 <= jam < 11:
    ucapan = waktu[0]  # pagi
elif 11 <= jam < 15:
    ucapan = waktu[1]  # siang
elif 15 <= jam < 18:
    ucapan = waktu[2]  # sore
else:
    ucapan = waktu[3]  # malam
print(f"Selamat {ucapan} {nama}.")