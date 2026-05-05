import time
import json
import socket
import shutil

def get_cpu_usage():
    with open("/proc/stat", "r") as f:
        line = f.readline()
    values = [float(x) for x in line.strip().split()[1:]]
    idle = values[3]
    total = sum(values)
    return round((1 - idle / total) * 100, 2)

def get_memory():
    mem = {}
    with open("/proc/meminfo", "r") as f:
        for line in f:
            key, value = line.split(":")
            mem[key] = int(value.strip().split()[0])

    total = mem["MemTotal"]
    free = mem["MemAvailable"]
    used = total - free

    return {
        "mem_total_mb": round(total / 1024, 2),
        "mem_used_mb": round(used / 1024, 2)
    }

def get_disk():
    total, used, free = shutil.disk_usage("/")
    return round(free / (1024**3), 2)

def get_data():
    data = {
        "device": socket.gethostname(),
        "cpu_usage_percent": get_cpu_usage(),
        "memory": get_memory(),
        "disk_free_gb": get_disk()
    }
    return data

while True:
    data = get_data()
    print("Enviado:", json.dumps(data))
    time.sleep(5)
