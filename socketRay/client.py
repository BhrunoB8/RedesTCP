import socket
HOST = "127.0.0.1"
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print("Received:\n", data.decode())
    request = input()
    if request == "Monitorar Memória":
        s.sendall((bytes("Monitorar Memória", "utf-8")))
        data = s.recv(1024)
        print("Received:\n", data.decode())
    elif request == "Monitorar CPU":
        s.sendall((bytes("Monitorar CPU", "utf-8")))
        data = s.recv(1024)
        print("Received:\n", data.decode())
