def tampil_menu():
    print("Pilihan yang tersedia:")
    print("b - menampilkan bantuan (menu)")
    print("n - menampilkan NIM")
    print("m - menampilkan Nama")
    print("l - menampilkan Alamat")
    print("p - menampilkan Kode Pos")
    print("s - menampilkan Semua data")
    print("k - keluar")
####################
def tampil_nim():
    print("NIM : L200250028")
def tampil_nama():
    print("Nama : Daffa Chandra Himawan")
def tampil_alamat():
    print("Alamat : Surakarta")
def tampil_kodepos():
    print("Kode Pos : 57169")
def tampil_semua():
    tampil_nim()
    tampil_nama()
    tampil_alamat()
    tampil_kodepos()
####################
def tampil_pilihan():
    while True:
        pilihan = input("\nMasukkan pilihan): ")
        if pilihan == 'b':
            tampil_menu()
        elif pilihan == 'k':
            print("Keluar. Terima kasih.")
            break
        elif pilihan == 'n':
            tampil_nim()
        elif pilihan == 'm':
            tampil_nama()
        elif pilihan == 'l':
            tampil_alamat()
        elif pilihan == 'p':
            tampil_kodepos()
        elif pilihan == 's':
            tampil_semua()
        else:
            print("Perintah tidak dikenal.")

tampil_menu()
tampil_pilihan()
