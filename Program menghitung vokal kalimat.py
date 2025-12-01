print("Program menghitung vokal.")
print("Dibuat oleh Daffa Chandra Himawan")
print("23 Oktober 2025")

teks = "Pembunuhan rakyat sipil adalah kejahatan perang."

jumlah_vokal = 0
vokal = "aiueoAIUEO"

for huruf in teks:
    if huruf in vokal:
        jumlah_vokal += 1

print("Pada teks ini:", teks)
print("Terdapat", jumlah_vokal, "huruf vokal.")
