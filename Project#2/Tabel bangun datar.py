bangun_datar = {
    "Segitiga"       : "L = 0.5 * a * t",
    "Persegi"        : "L = s ** 2",
    "Persegi Panjang": "L = p * l",
    "Lingkaran"      : "L = pi * r ** 2",
    "Jajar Genjang"  : "L = a * t"
}
print("No | Nama Bangun Datar    | Rumus Luas")
print("-- | -------------------- | ----------------")
No = 1
for nama, rumus in bangun_datar.items():
    print(f"{No:<2} | {nama:<20} | {rumus}")
    No += 1
