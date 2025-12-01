def menu():
    while True:
        print("========= Bangun Datar dan Ruang =========")
        print("""Pilih bangun:
1. Persegi
2. Persegi Panjang
3. Segitiga
4. Balok
5. Kubus
6. Bola
7. Keluar
""")
        pilihan = input("Masukkan pilihan bangun (1/2/3/4/5/6/7): ")
        if pilihan == "1":
            persegi()
        elif pilihan == "2":
            persegi_panjang()
        elif pilihan == "3":
            segitiga()
        elif pilihan == "4":
            balok()
        elif pilihan == "5":
            kubus()
        elif pilihan == "6":
            bola()
        elif pilihan == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.\n")
            break

def persegi():
    sisi = int(input("Masukkan panjang sisi persegi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print(f"Luas persegi: {luas}")
    print(f"Keliling persegi: {keliling}\n")

def persegi_panjang():
    panjang = int(input("Masukkan panjang persegi panjang: "))
    lebar = int(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas persegi panjang: {luas}")
    print(f"Keliling persegi panjang: {keliling}\n")

def segitiga():
    alas = int(input("Masukkan panjang alas segitiga: "))
    tinggi = int(input("Masukkan tinggi segitiga: "))
    luas = (alas * tinggi) // 2  
    sisi_miring = int((alas*2 + tinggi*2)*0.5)  
    keliling = alas + tinggi + sisi_miring
    print(f"Luas segitiga: {luas}")
    print(f"Keliling segitiga: {keliling}\n")

def balok():
    panjang = int(input("Masukkan panjang balok: "))
    lebar = int(input("Masukkan lebar balok: "))
    tinggi = int(input("Masukkan tinggi balok: "))
    volume = panjang * lebar * tinggi
    print(f"Volume balok: {volume}\n")

def kubus():
    sisi = int(input("Masukkan panjang sisi kubus: "))
    volume = sisi**3
    print(f"Volume kubus: {volume}\n")

def bola():
    jari_jari = int(input("Masukkan jari-jari bola: "))
    volume = (4 // 3) * 3 * (jari_jari**3)  
    print(f"Volume bola: {volume}\n")

menu()