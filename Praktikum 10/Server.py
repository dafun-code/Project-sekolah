import socket 

host = "localhost"
port = 5050

data = {
    'nama' : 'Daffa',
    'NIM' : 'L200250028',
    'angkatan': 2025,
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()

print("SERVER AKTIF — MENUNGGU CLIENT...\n")

running = True

while running:
    client, addr = server.accept()
    print(f"Client datang: {addr}")

    pesan_user = client.recv(1024).decode().strip()
    print(f"Perintah dari client : {pesan_user}")

    if pesan_user == 'q':
        client.send(b"Server dihentikan.")
        client.close()
        running = False
        break

    if pesan_user in data:
        client.send(str(data[pesan_user]).encode())
        print(f"Respon : {data[pesan_user]}")
    else:
        client.send(b"Perintah tidak dikenal")
        print("Respon : Perintah tidak dikenal")

    client.close()

server.close()
print("Server OFF.")
