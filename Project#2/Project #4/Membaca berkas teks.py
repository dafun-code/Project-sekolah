berkas = open("L200250028", "r")
nim = berkas.readline().strip()
tgl_lahir = berkas.readline().strip()
nama = berkas.readline().strip()
berkas.close()

dd, mm, yyyy = tgl_lahir.split("-")
tgl_baru = f"{mm}/{dd}/{yyyy[2:]}"

print(nama)
print("Sampit,", tgl_baru)  
print(nim)