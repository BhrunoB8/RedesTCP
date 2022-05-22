import socket
from time import sleep
HOST = "127.0.0.1"
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    if input() == "Memória":
        s.sendall((bytes("Memória", "utf-8")))
        data = s.recv(1024)
        print("Received:\n", data.decode())
        while True:
            s.sendall(bytes("Memória", "utf-8"))
            data = s.recv(1024)
            print("Received:\n", data.decode())
            sleep(5)
    if input() == "CPU":
        s.sendall((bytes("CPU", "utf-8")))
        data = s.recv(1024)
        print("Received:\n", data.decode())
        while True:
            s.sendall(bytes("CPU", "utf-8"))
            data = s.recv(1024)
            print("Received:\n", data.decode())
            sleep(5)

        # sent = input().encode()
        # s.sendall(sent)
        # data = s.recv(1024)
        # print("Received:\n", data.decode())

    # while True:
    #     sent = input("> ").encode()
    #     s.sendall(sent)
    #     data = s.recv(1024)
    #     print("Received: ", data.decode())
        