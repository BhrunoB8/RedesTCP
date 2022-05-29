import socket
import psutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

def get_mem_info():
    swap = psutil.swap_memory()
    return (f"\nTotal:  {get_size(swap.total)} \nFree:  {get_size(swap.free)} \nUsed:  {get_size(swap.used)}\nPercentage:  {swap.percent}%")

HOST = "127.0.0.1"
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print("Connected to", addr)
            conn.sendall(bytes("Bem-vindo, para monitorar:\nCPU digite: Monitorar CPU\nMemória digite: Monitorar Memória", "utf-8"))
            while True:
                data = conn.recv(1024)
                if not data: break
                if(data.decode() == "Monitorar Memória"):
                    print("Received:\n", data.decode())
                    conn.sendall(bytes(get_mem_info(), "utf-8"))
                elif(data.decode() == "Monitorar CPU"):
                    print("Received:\n", data.decode())
                    conn.sendall(bytes(f"Total CPU Usage: {psutil.cpu_percent()}%", "utf-8"))   