import socket
import sys

import paramiko, time

print("="*40, "System Information", "="*40)

def ssh_conn(ip = None, user = None, pwd = None):
    if ip is None:
        ip = input('[*]Enter Server IP Address :')
    if user is None:
        user = input('[*]Enter Username :')
    if pwd is None:
        pwd = input('[*]Enter Password :')
    try:
        print("Creating SSH Client..")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connection..")
        ssh_client.connect(hostname=ip, username=user, password=pwd)
        cmd = input('[*]Enter Command :')
        print("Command execution..")
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        time.sleep(10)
        print("Command executed..")
        stdout = stdout.readlines()
        print(stdout)
        ssh_client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Username: " + user + "\t or password invalid.")
        ssh_conn(ip, None, None)
    except socket.gaierror:
        print(ip + " invalid.")
        ssh_conn(None, user, pwd)
    except:
        print("Unexpected error: ", sys.exc_info())


ssh_conn()