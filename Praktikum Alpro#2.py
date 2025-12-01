## Program Akun
## Dibuat Daffa Chandra Himawan L200250028

Nama = "Daffa Chandra Himawan"
TanggalLahir = "25 Maret 2007"

print("Data Akun")
print("Nama Lengkap:", Nama)
print("Tanggal Lahir:", TanggalLahir)
NamaSingkat = Nama[0] + "." + Nama[6] + "." + Nama[14:]
print("Nama Singkat   :", NamaSingkat)
Username = Nama[0] + Nama[6] + TanggalLahir[0:2] + TanggalLahir[3:8] + TanggalLahir[9:]
print("Username:", Username)
Password = Nama[18:]+TanggalLahir[9:]
print("Password Sementara:", Password)