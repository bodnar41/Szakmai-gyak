import SCP_conn
import SSH_conn

ip = input("IP address:")
user = input("Username:")
pwd = input("Password:")
info = input("Number of info: \n1. Sysinfo \n2. CPU info \n3.Frequency info \n4. Core info\n")


file = open('C:/Users/kliens01/teszt.txt', 'w')
file.write(info)
file.close()

SCP_conn.scp_conn(ip, user, pwd, "put")
SSH_conn.ssh_conn(ip, user, pwd)
SCP_conn.scp_conn(ip, user, pwd, "get")

