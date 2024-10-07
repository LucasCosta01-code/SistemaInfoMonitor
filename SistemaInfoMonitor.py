import tkinter as tk
from tkinter import ttk
import psutil
import platform
import GPUtil

# Função para obter informações detalhadas do sistema
def get_system_info():
    # Coleta informações do sistema operacional
    uname = platform.uname()
    system_info = {
        "Sistema": uname.system,  # Sistema operacional
        "Nome do usuário do sistema": uname.node,  # Nome do computador
        "Versão": uname.version,  # Versão do sistema operacional
        "Máquina": uname.machine,  # Arquitetura do processador
        "Processador": uname.processor,  # Modelo do processador
        "Memória Total (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # Memória total em GB
        "Memória Disponível (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2),  # Memória disponível em GB
        "Uso da CPU (%)": psutil.cpu_percent(interval=1),  # Uso da CPU em porcentagem
        "Uso da Memória (%)": psutil.virtual_memory().percent,  # Uso da memória em porcentagem
    }
    
    # Informações sobre o disco
    disk_info = psutil.disk_usage('/')
    system_info["Uso do Disco (%)"] = disk_info.percent  # Uso do disco em porcentagem
    system_info["Espaço Total do Disco (GB)"] = round(disk_info.total / (1024 ** 3), 2)  # Espaço total do disco em GB
    system_info["Espaço Usado do Disco (GB)"] = round(disk_info.used / (1024 ** 3), 2)  # Espaço usado do disco em GB
    system_info["Espaço Livre do Disco (GB)"] = round(disk_info.free / (1024 ** 3), 2)  # Espaço livre do disco em GB
    
    # Informações sobre a rede
    net_info = psutil.net_io_counters()
    system_info["Bytes Enviados (MB)"] = round(net_info.bytes_sent / (1024 ** 2), 2)  # Bytes enviados em MB
    system_info["Bytes Recebidos (MB)"] = round(net_info.bytes_recv / (1024 ** 2), 2)  # Bytes recebidos em MB
    
    # Informações sobre a GPU (se disponível)
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        system_info["Placa de Vídeo"] = gpu.name  # Nome da placa de vídeo
        system_info["Memória da GPU (GB)"] = gpu.memoryTotal  # Memória total da GPU em GB
        
    return system_info

# Função para atualizar as informações exibidas na interface gráfica
def update_info():
    info = get_system_info()
    for key, value in info.items():
        info_labels[key].config(text=f"{key}: {value}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Informações do Sistema")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

info_labels = {}
row = 0
# Cria rótulos para exibir as informações do sistema
for key in get_system_info().keys():
    label = ttk.Label(mainframe, text=f"{key}: ")
    label.grid(row=row, column=0, sticky=tk.W)
    value_label = ttk.Label(mainframe, text="")
    value_label.grid(row=row, column=1, sticky=tk.W)
    info_labels[key] = value_label
    row += 1

# Botão para atualizar as informações
update_button = ttk.Button(mainframe, text="Atualizar", command=update_info)
update_button.grid(row=row, column=0, columnspan=2)

update_info()  # Atualiza as informações ao iniciar o programa

root.mainloop()  # Inicia o loop principal da interface gráfica
