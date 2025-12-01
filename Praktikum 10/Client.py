import socket

host = "localhost"
port = 5050

while True:
    pesan = input("Masukkan perintah (nama / NIM / angkatan / q): ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    client.send(pesan.encode())

    balasan = client.recv(1024).decode()
    print("Balasan server:", balasan)

    client.close()

    if pesan == 'q':
        break
