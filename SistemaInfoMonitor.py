import tkinter as tk
from tkinter import ttk
import psutil
import platform
import GPUtil

def get_system_info():
    uname = platform.uname()
    system_info = {
        "Sistema": uname.system,
        "Nome do Dono": uname.node,
        "Versão": uname.version,
        "Máquina": uname.machine,
        "Processador": uname.processor,
        "Memória Total (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Memória Disponível (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Uso da CPU (%)": psutil.cpu_percent(interval=1),
        "Uso da Memória (%)": psutil.virtual_memory().percent,
    }
    
    # Informações sobre discos
    disk_info = psutil.disk_usage('/')
    system_info["Uso do Disco (%)"] = disk_info.percent
    system_info["Espaço Total do Disco (GB)"] = round(disk_info.total / (1024 ** 3), 2)
    system_info["Espaço Usado do Disco (GB)"] = round(disk_info.used / (1024 ** 3), 2)
    system_info["Espaço Livre do Disco (GB)"] = round(disk_info.free / (1024 ** 3), 2)
    
    # Informações sobre a rede
    net_info = psutil.net_io_counters()
    system_info["Bytes Enviados (MB)"] = round(net_info.bytes_sent / (1024 ** 2), 2)
    system_info["Bytes Recebidos (MB)"] = round(net_info.bytes_recv / (1024 ** 2), 2)
    
    # Informações sobre a GPU
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        system_info["Placa de Vídeo"] = gpu.name
        system_info["Memória da GPU (GB)"] = gpu.memoryTotal
    
    return system_info

def update_info():
    info = get_system_info()
    for key, value in info.items():
        info_labels[key].config(text=f"{key}: {value}")

root = tk.Tk()
root.title("Informações do Sistema")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

info_labels = {}
row = 0
for key in get_system_info().keys():
    label = ttk.Label(mainframe, text=f"{key}: ")
    label.grid(row=row, column=0, sticky=tk.W)
    value_label = ttk.Label(mainframe, text="")
    value_label.grid(row=row, column=1, sticky=tk.W)
    info_labels[key] = value_label
    row += 1

update_button = ttk.Button(mainframe, text="Atualizar", command=update_info)
update_button.grid(row=row, column=0, columnspan=2)

update_info()  # Atualiza as informações na inicialização

root.mainloop()