import socket
import psutil

#
# Método utilizado para formatar a tamanho da memória, definindo se é KB, MB, GB, TB, PB
# @param bytes pegará o tamanho que irá definir qual das unidades será usado
# @param suffix sufixo que irá compor o diferentes tipos de tamanhos
# return retorna o valor em bytes juntamente da unidade com o sufixo montando por exemplo: 3 GB
#
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor


#
# Método utilizando o import de psutil juntamente da função get_size para pegar
# as informações do total da memória, espaço disponível e a porcentagem de uso
# return retorna os valores do Total, Used, Percentage
#
def get_mem_info():
    swap = psutil.swap_memory()
    return (f"\nTotal:  {get_size(swap.total)} \nFree:  {get_size(swap.free)} \nUsed:  {get_size(swap.used)}\nPercentage:  {swap.percent}%")

#IP do servidor
HOST = "127.0.0.1"
#Porta do servidor
PORT = 50000

#
# AF_INET é o IPV4
# Protocolo TCP é o SOCK_STREAM
#
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Definiou o servidor vinculando o HOST e PORT agrupados
    s.bind((HOST, PORT))

    # Modo de escuta, aguardando a conexão de um cliente
    s.listen()

    while True:
        # Método para aceitar a conexão
        conn, addr = s.accept()
        with conn:
            print("Connected to", addr)
            # Opções de monitoramentos disponíveis
            conn.sendall(bytes("\nBem-vindo, para monitorar:\nCPU digite: Monitorar CPU\nMemória digite: Monitorar Memória", "utf-8"))
            while True:
                # Dados que serão recebidos
                data = conn.recv(1024)

                # Utiliza o decode para decodificar a mensagem recebida
                if not data: break
                decode = data.decode()

                # Se a mensagem recebida pelo cliente for "Monitorar Memória" ele executa a função get_mem_info()
                # Usa o sendall para enviar a informação ao cliente
                if(decode == "Monitorar Memória"):
                    print("Received:\n", data.decode())
                    conn.sendall(bytes(get_mem_info(), "utf-8"))
                
                # Se a mensagem recebida pelo cliente for "Monitorar CPU" ele executa a função psutil.cpu_percent()
                # Usa o sendall para enviar a informação ao cliente
                elif(decode == "Monitorar CPU"):
                    print("Received:\n", data.decode())
                    conn.sendall(bytes(f"Total CPU Usage: {psutil.cpu_percent()}%", "utf-8"))   
                