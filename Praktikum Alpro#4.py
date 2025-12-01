##### 1. #####
Nama = 'Daffa CHandra Himawan' 
Nim = '128'
Tinggi = '1.60'
Berat = '42'
TahunLahir = '2007'
Aku = (TahunLahir, Berat, Tinggi, Nim, Nama)
Data = [TahunLahir, Berat, Tinggi, Nim, Nama]
##### 2. #####
type(Aku)
Aku[0]
a = int(Nim) % 4 ; Aku[a] # Perbaikan: Nim harus diubah ke integer
Aku[a] 
type(Aku[a])
Aku[a:4]
type(Aku[4])
# Aku[0] = 'ok'  # Tidak bisa assign pada tuple, jadi di-comment
##### 3. #####
type(Data)
type(Data[4])
Data[4][5]
type(Data[4][a:6])
Data[0] = 'ok'; Data
Data[-a]
range(a)

##### 1. Output #####
print('Nama:', Nama)
print('Nim:', Nim)
print('Tinggi:', Tinggi)
print('Berat:', Berat)
print('Tahun Lahir:', TahunLahir)
##### 2. Output #####
print('Tipe data Aku adalah', type(Aku))
print('Aku[0] =', Aku[0])
print('Nilai a =', a)   
print('tipe',type(Aku[a]))
print('Aku[a:4] =', Aku[a:4])
print('tipe',type(Aku[4]))
print('Aku[0] = ok tidak bisa diubah karena tipe data tuple')
##### 3. Output #####
print('Tipe data Data adalah', type(Data))
print('Tipe data Data[4] adalah', type(Data[4]))
print('Data[4][5] =', Data[4][5])
print('Tipe data Data[4][a:6] adalah', type(Data[4][a:6]))
print('Data[0] = ok; Data =', Data)
print('Data[-a] =', Data[-a])
print('range(a) =', list(range(a)))  # Agar hasilnya terlihat