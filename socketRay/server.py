import socket
from time import sleep
import psutil

# def get_cpu():
#     cpufreq = psutil.cpu_freq()
#     print("CPU Usage Per Core: ")
#     for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
#         print(f"Core {i}: {percentage}%")
#     print(f"Total CPU Usage: {psutil.cpu_percent()}%")

   

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

def get_mem_info():
    swap = psutil.swap_memory()
    return (f"Total:  {get_size(swap.total)} \nFree:  {get_size(swap.free)} \nUsed:  {get_size(swap.used)}\nPercentage:  {swap.percent}%")

HOST = "127.0.0.1"
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print("Connected to", addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                if(data.decode() == "Memória"):
                    print("Received:\n", data.decode())
                    while True:
                        print("Received:\n", data.decode())
                        conn.sendall(bytes(get_mem_info(), "utf-8"))
                        sleep(5)
                #         if data.decode() == "Pare": break
                elif(data.decode() == "CPU"):
                    print("Received:\n", data.decode())
                    while True:
                        print("Received:\n", data.decode())
                        conn.sendall(bytes(f"Total CPU Usage: {psutil.cpu_percent()}%", "utf-8"))
                        sleep(5)   
                else:
                    print("Received:\n", data.decode())
                    sent = input("> ".encode)
                    conn.sendall(bytes(sent, "utf-8"))