password_benar = "Daffa"
kesempatan = 3
while kesempatan > 0:
    password = input("Masukkan password: ")
    if password == password_benar:
        print("Anda berhasil login!")
        break
    else:
        kesempatan -= 1
        print("Maaf, anda salah memasukkan password.")
        if kesempatan > 0:
            print(f"Kesempatan tersisa: {kesempatan} kali\n")
        else:
            print("Anda telah mencoba 3 kali. Akses anda ditolak.")