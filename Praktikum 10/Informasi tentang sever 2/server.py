import socket
import platform

host = "localhost"
port = 5030

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("SERVER AKTIF – MENUNGGU CLIENT...\n")

running = True
while running:
    client, addr = server.accept()
    print(f"Client datang: {addr}")

    perintah = client.recv(1024).decode().strip()
    print(f"Perintah dari client : {perintah}")

    if perintah.lower() == "machine":
        respon = platform.machine()
    elif perintah.lower() == "release":
        respon = platform.release()
    elif perintah.lower() == "system":
        respon = platform.system()
    elif perintah.lower() == "version":
        respon = platform.version()
    elif perintah.lower() == "node":
        respon = platform.node()
    elif perintah.lower() == "quit":
        respon = "Server dihentikan"
        running = False
    else:
        respon = "unknown command"

    client.send(respon.encode())
    client.close()

server.close()
print("Server telah berhenti.")
