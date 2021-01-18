import socket
import sys
import paramiko, time


def ssh_conn(ip = None, user = None, pwd = None, cmd = None):
    if ip is None:
        ip = input("Enter Server IP Address:")
    if user is None:
        user = input("Enter Username:")
    if pwd is None:
        pwd = input("Enter Password:")
    if cmd is None:
        cmd = input("Enter command:")
    try:
        print("Creating SSH Client..")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connection..")
        ssh_client.connect(hostname=ip, username=user, password=pwd)
        print("Command execution..")
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        time.sleep(5)
        print("Command executed..")
        stdout = stdout.readlines()
        print(stdout)
        ssh_client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Username: " + user + "\t or password invalid.")
        ssh_conn(ip, None, None, cmd)
    except socket.gaierror:
        print(ip + " invalid.")
        ssh_conn(None, user, pwd, cmd)
    except:
        print("Unexpected error: ", sys.exc_info())


