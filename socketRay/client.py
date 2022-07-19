import socket

# O IP
HOST = "127.0.0.1"
# A porta do servidor
PORT = 1234

#
# AF_INET é o IPV4
# Protocolo TCP é o SOCK_STREAM
#
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Realiza a conexão com o servidor por meio do IP e Porta
    s.connect((HOST, PORT))

    # Recebe a mensagem do servidor e printa na tela para o cliente
    data = s.recv(1024)
    print("Recebendo do Servidor:\n", data.decode())

    # Mensagens que o cliente pode mandar ao servidor
    request = input()
    if request == "1":
        s.sendall((bytes("1", "utf-8")))
        data = s.recv(1024)
        print("Recebido do Servidor:\n", data.decode())
    elif request == "2":
        s.sendall((bytes("2", "utf-8")))
        data = s.recv(1024)
        print("Recebido do Servidor:\n", data.decode())
    elif request == "3":
        s.sendall((bytes("3", "utf-8")))
        data = s.recv(1024)
        print("Recebido do servidor:\n", data.decode())
    elif request == "4":
        s.sendall((bytes("4", "utf-8")))
        data = s.recv(1048576)
        print("Recebido do servidor:\n", data.decode())
