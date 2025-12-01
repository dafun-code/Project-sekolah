for i in range (0, 10):
    print (i)


#percobaan 1
a = int(input("masukkan nilai awal: "))
b = int(input("masukkan nilai akhir: "))
for i in range (a, b):
    print (i)

#percobaan 2
buah = ["jeruk", "apel", "manggis"]
for enak in buah:
    print ("buah", enak)
    print(enak,",", end="")

#percobaan 3
for i in "Dapa":
    print (i)

#percobaan 4
a = int(input("masukkan ketinggian segitiga: "))
for i in range (1,a):
    print("*"*i)

#percobaan 5
a =int (input("masukkan ketinggian segitiga: "))
for i in range (a, 0, -1):
    print ("*"*i)

#percobaan 6
for i in range (1,6):
    for j in range (1,6):
        print (i,j)

#percobaan 7
for i in range (1,a):
    for j in range (i):
        print("*",end="")
    print()

#Latihan 1
for i in range (1, 20, 2):
    print (i)

#Latihan 2
for i in range (5):
    for j in range (5):
        print("#",end="")
    print()

#Latihan 3
for i in range (1,6):
    print (i,i**2)

        #perulangan while
#Percobaan 1
i = 1
while i <=5:
    print ("Perulangan ke-", i)
i+=1

#Percobaan 2
count = 5
while count > 0:
    print("Hitung mundur:", count)
print("Waktu Habis!")

#Percobaan 3
password_benar = "infor kece"
percobaan = 1
while percobaan <= 3:
    password = input("Masukkan Password: ")
    if password == password_benar:
        print ("Login Berhasil")
        break
    else:
        print ("Password Salah, coba lagi")
        percobaan += 1
else:
    print ("Proses login di tolak terlalu banyak percobaan")