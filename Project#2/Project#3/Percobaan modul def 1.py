data = {
    "NIM": "L200250028",
    "Nama": "Daffa Chandra Himawan",
    "Alamat": "Mendungan, JL.Merapi No 2",
    "Jurusan": "Teknik Informatika",
    "Fakultas": "Komunikasi dan Informatika",
    "Email": "daffachandra983@gmail.com",
    "TanggalLahir": "25 Maret 2007",
}
#################################
def tampil_nim():
    print("NIM  :", data["NIM"])
def tampil_nama():
    print("Nama :", data["Nama"])
def tampil_alamat():
    print("Alamat :", data["Alamat"])
def tampil_jurusan():
    print("Jurusan :", data["Jurusan"])
def tampil_fakultas():
    print("Fakultas :", data["Fakultas"])
def tampil_email():
    print("Email :", data["Email"])
def tampil_tgllahir():
    print("Tanggal Lahir :", data["TanggalLahir"])
def tampil_semua():
    for kunci, hasil in data.items():
        print(f"{kunci} : {hasil}")
tampil_semua()