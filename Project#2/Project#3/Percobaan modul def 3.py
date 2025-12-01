def konversiSuhu(nilai, skala):
    if skala == 'C' or skala == 'c':
        F = (nilai * 9/5) + 32
        print(f"{nilai}°C = {int(F)}°F")

    elif skala == 'F' or skala == 'f':
        C = (nilai - 32) * 5/9
        print(f"{nilai}°F = {int(C)}°C")
konversiSuhu(50, 'C')
konversiSuhu(34, 'f')