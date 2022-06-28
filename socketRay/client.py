import socket

# O IP
HOST = "127.0.0.1"
# A porta do servidor
PORT = 50000

#
# AF_INET é o IPV4
# Protocolo TCP é o SOCK_STREAM
#
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Realiza a conexão com o servidor por meio do IP e Porta
    s.connect((HOST, PORT))

    # Recebe a mensagem do servidor e printa na tela para o cliente
    data = s.recv(1024)
    print("Received:\n", data.decode())

    # Mensagens que o cliente pode mandar ao servidor
    request = input()
    if request == "Monitorar Memória":
        s.sendall((bytes("Monitorar Memória", "utf-8")))
        data = s.recv(1024)
        print("Received:\n", data.decode())
    elif request == "Monitorar CPU":
        s.sendall((bytes("Monitorar CPU", "utf-8")))
        data = s.recv(1024)
        print("Received:\n", data.decode())
