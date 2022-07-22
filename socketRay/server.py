import socket
import psutil
from _thread import *
import argparse

class Servidor:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        self.ServerSocket = socket.socket()
        self.ThreadCount = 0
        try:
            self.ServerSocket.bind((self.ip, self.port))
        except socket.error as e:
            print(str(e))

        print('Servidor inicializado. Esperando por conexões...')
        self.ServerSocket.listen(5)

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
        # Método utilizando o import de psutil juntamente da função get_size para pegar
        # as informações do total da memória, espaço disponível e a porcentagem de uso
        # return retorna os valores do Total, Used, Percentage
        #
        def get_mem_info():
            swap = psutil.swap_memory()
            return (f"\nTotal:  {get_size(swap.total)} \nFree:  {get_size(swap.free)} \nUsed:  {get_size(swap.used)}\nPercentage:  {swap.percent}%")

        #Método que realiza a conexão com o cliente, envia as informações que ele pode realizar e gera as informações
        #de monitoramento. Ainda realiza a questão de vários clientes conectados no mesmo servidor
        def threaded_client(connection):
            
            self.ThreadCount += 1
            print("Conectado com ", address)
            connection.sendall(bytes("\nBem-vindo, para monitorar digite um número:\n1. Monitorar CPU\n2: Monitorar Memória\n3: Monitorar Uso da Rede\n4: Monitorar Processos", "utf-8"))

            while True:
                data = connection.recv(2048)
                if not data: 
                    print("Cliente ",address," desconectado")
                    break
                decode = data.decode()

                # Se a mensagem recebida pelo cliente for "1" ele executa a função get_mem_info()
                # Usa o sendall para enviar a informação ao cliente sobre O USO DA MEMÓRIA
                if(decode == "1"):
                    print("Recebido do cliente:\n", data.decode())
                    connection.sendall(bytes(get_mem_info(), "utf-8"))
                
                # Se a mensagem recebida pelo cliente for "2" ele executa a função psutil.cpu_percent()
                # Usa o sendall para enviar a informação ao cliente sobre o USO DA CPU
                elif(decode == "2"):
                    print("Recebido do cliente::\n", data.decode())
                    connection.sendall(bytes(f"Total CPU Usage: {psutil.cpu_percent()}%", "utf-8"))

                # Se a mensagem recebida pelo cliente for "3" ele executa a função net_io_counters()
                # Usa o sendall para enviar a informação ao cliente sobre o USO DA REDE
                elif(decode == "3"):
                    print("Recebido do cliente:\n", data.decode())
                    connection.sendall(bytes(f"Estatísticas do uso da rede: {psutil.net_io_counters()}", "utf-8"))

                # Se a mensagem recebida pelo cliente for "4" ele executa a função process_iter()
                # Usa o sendall para enviar a informação ao cliente sobre os PROCESSOS ATIVOS
                elif(decode == "4"):
                    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
                    print("Recebido do cliente:\n", data.decode())
                    connection.sendall(bytes(f"Processos Ativos\n: {procs}", "utf-8"))
        
        while True:
            Client, address = self.ServerSocket.accept()
            start_new_thread(threaded_client, (Client, ))
            print('Número de thread: ' + str(self.ThreadCount))
        #print("Cliente desconectado.")
        ServerSocket.close()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ip', metavar='I', type=str,
                        help='IP')

    parser.add_argument('--port', metavar='P', type=int,
                        help='Porta')

    args = parser.parse_args()
    serv = Servidor(args.ip, args.port)
    serv.run()

if(__name__ == '__main__'):
    main()

    