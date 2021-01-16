import qrcode
from PIL import Image
import platform
import psutil
from datetime import datetime

#OS and client name
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")

# let's print CPU information
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
# number of cores
print("Total cores:", psutil.cpu_count(logical=True))

# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")

#RAM info
print("Memory info")
total = round(psutil.virtual_memory().total * (9.91*10**-10))
print(f"{total} GB")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(f"System: {uname.system}\n")
qr.add_data(f"Node Name: {uname.node}\n")
qr.add_data(f"Node Release: {uname.release}\n")
qr.add_data(f"Machine: {uname.machine}\n")
qr.add_data(f"Processor: {uname.processor}\n")
qr.add_data(f"Total cores: {psutil.cpu_count(logical=True)}\n")
qr.add_data(f"Max Frequency: {cpufreq.max:.2f}Mhz\n")
qr.add_data(f"Memory: {total} GB")

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("1.png")