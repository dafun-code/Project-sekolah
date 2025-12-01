import socket

host = "localhost"
port = 5030

print("Program komunikasi tentang server")

while True:
    cmd = input("Command: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    client.send(cmd.encode())

    respon = client.recv(1024).decode()
    print("Response:", respon)

    client.close()

    if cmd.lower() == "quit":
        break
