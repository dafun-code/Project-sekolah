#Nama: Daffa Chandra Himawan
#NIM : L200250028
Z = 'L200250028' # ganti L200101010 dengan NIM anda
m = Z[9:6:-1]
n = int(m[0])
p = int(m) + 19
q = 15 - n
r = p // 10
s = 2 * m
t = p % q
u = t ** 2
v = p - t
w = n < 6
#OUTPUT
print("NIM                :",                       Z)
print("tiga digit terakhir secara terbalik:",       m)
print("angka pertama ubah ke integer:",             n)
print("menjumlahkan m dengan 19:",                  p)
print("menghitung selisih antara 15 dan n:",        q)
print("pembagian bulat dari p dibagi 10",           r)
print("mengulang string m dua kali:",               s)
print("sisa hasil bagi dari p dibagi q:",           t)
print("pangkat dua dari nilai t:",                  u)
print("mengurangi p dengan t:",                     v)
print("mengecek apakah n kurang dari 6 (boolean):", w)
