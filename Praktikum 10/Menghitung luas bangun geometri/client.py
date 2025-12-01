import socket

s = socket.socket()
s.connect(("localhost", 5000))

while True:
    msg = input("Pesan: ")

    s.send(msg.encode())
    data = s.recv(1024).decode()
    print("Respon:", data)

    if msg == "keluar":
        break

s.close()