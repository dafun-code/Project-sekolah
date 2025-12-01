import socket

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

params = {}

def hitung(p):
    s = float(p.get("sisi", 0))
    return s * s

conn, addr = s.accept()

while True:
    data = conn.recv(1024).decode()

    if data.startswith("set"):
        _, k, v = data.split()
        params[k] = v
        conn.send(b"ok")

    elif data == "hitung":
        hasil = hitung(params)
        conn.send(str(hasil).encode())

    elif data == "keluar":
        conn.send(b"bye")
        break

conn.close()
s.close()