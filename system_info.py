import platform, psutil
from datetime import datetime
import json
import paramiko


f = open("C:/Users/kliens02/teszt.txt", "r")
choice = f.read()
print(choice)

if choice == "1":
    uname = platform.uname()
    sysinfo = {"System info": [
        {"System": uname.system, "Node Name": uname.node, "Release": uname.release, "Version": uname.version,
         "Machine": uname.machine, "Processor": uname.processor}]}
    sysJSON = json.dumps(sysinfo, indent=4, sort_keys=True)
    with open("C:/Users/kliens02/system_info.json", "w") as file:
        json.dump(sysinfo, file, indent=4)

if choice == "2":
    cpuinfo = {"CPU info": [
        {"Physical cores": psutil.cpu_count(logical=False), "Total cores": psutil.cpu_count(logical=True)}]}
    cpuJSON = json.dumps(cpuinfo, indent=4, sort_keys=True)
    with open("C:/Users/kliens02/system_info.json", "w") as file:
        json.dump(cpuinfo, file, indent=4)

if choice == "3":
    cpufreq = psutil.cpu_freq()
    freqinfo = {"Frequency info": [
        {"Max Frequency": str(cpufreq.max) + " Mhz", "Min Frequency": str(cpufreq.min) + " Mhz",
         "Current Frequency": str(cpufreq.current) + " Mhz"}]}
    freqJSON = json.dumps(freqinfo, indent=4, sort_keys=True)
    with open("C:/Users/kliens02/system_info.json", "w") as file:
        json.dump(freqinfo, file, indent=4)

if choice == "4":
    core = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=2)):
        core.append(percentage)

    data3 = psutil.cpu_percent()
    length = len(core)
    coreinfo = {"Core info": []}

    for i in range(length):
        coreinfo["Core info"].append({'Core' + str(i): str(core[i]) + "%"})
    coreinfo["Core info"].append({'Full usage': str(data3) + "%"})
    coreJSON = json.dumps(coreinfo, indent=4, sort_keys=True)
    with open("C:/Users/kliens02/system_info.json", "w") as file:
        json.dump(coreinfo, file, indent=4)

