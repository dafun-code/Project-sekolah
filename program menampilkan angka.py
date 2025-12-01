print("Program menampilkan angka.")
print("Dibuat oleh Daffa Chandra Himawan")
print("23 Oktober 2025")
for i in range(1, 31):
    if i % 3 == 0 and i % 4 == 0:
        print(i, "snack and drink")
    elif i % 3 == 0:
        print(i, "snack")
    elif i % 4 == 0:
        print(i, "drink")
    else:
        print(i)