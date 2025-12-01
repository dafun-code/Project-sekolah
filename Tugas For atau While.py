#TUGAS FOR ATAU WHILE
#1. buat program yang menampilkan deret bilangan ganjil dan genap dari 1 hingga angka yang dimasukkan pengguna

##input 
n = int(input("Masukkan angka batas: "))

##ganjil
print("Bilangan ganjil dari 1 hingga", n, ":")
for i in range(1, n+1):
    if i % 2 != 0:
        print(i, end=" ")

print("\n") #baris baru

##genap
print("Bilangan genap dari 1 hingga", n, ":")
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")

################################################################################################################################
#2. buat pola segitiga bintang berdasarkan jumlah baris yang dimasukkan pengguna.

baris = int(input("Masukkan jumlah baris: "))

for i in range(1, baris+1):
    print("*"*i)

###########################################################################################################################################
#3. Tampilkan deret fibonanci hingga batas suku tertentu
n= int(input("Masukkan jumlah suku fibonacci: "))

##inisialisasi dua suku pertama
a, b = 0, 1

print("Deret fibonacci sebanyak", n, "suku:")

##Menampilkan deret fibbonacci
for i in range(n):
    print(a, end=" ")
    a, b= b, a+b