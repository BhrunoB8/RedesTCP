import psutil

# def get_cpu():
#     print("="*40, "CPU Info", "="*40)

#     print("Physical cores:", psutil.cpu_count(logical=False))
#     print("Total cores: ", psutil.cpu_count(logical=True))

#     cpufreq = psutil.cpu_freq()
#     print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
#     # print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
#     print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

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
    print("="*40, "Memory Information", "="*40)

    swap = psutil.swap_memory()
    print(f"Total:  {get_size(swap.total)}")
    print(f"Free:  {get_size(swap.free)}")
    print(f"Used:  {get_size(swap.used)}")
    print(f"Percentage:  {swap.percent}%")
